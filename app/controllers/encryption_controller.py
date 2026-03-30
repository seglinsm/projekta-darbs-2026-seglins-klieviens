"""Failu šifrēšanas kontroliera skelets."""

from __future__ import annotations

from pathlib import Path

from app.models.encryption_result import EncryptionResult
from app.models.operation_request import OperationRequest
from app.services.crypto_service import CryptoService
from app.services.file_service import FileService
from app.services.key_service import KeyService
from app.services.log_service import LogService
from app.services.validation_service import ValidationService
from app.utils.exceptions import (
    AppError,
    EncryptionProcessError,
    FileAccessError,
    KeyErrorInvalid,
    ValidationError,
)


class EncryptionController:
    """Savieno GUI slāni ar failu apstrādes un šifrēšanas servisiem."""

    def __init__(
        self,
        crypto_service: CryptoService,
        file_service: FileService,
        key_service: KeyService,
        validation_service: ValidationService,
        log_service: LogService,
    ) -> None:
        """Inicializē kontrolieri ar visiem nepieciešamajiem servisiem.

        Args:
            crypto_service: Serviss datu šifrēšanai un atšifrēšanai.
            file_service: Serviss darbam ar failiem.
            key_service: Serviss atslēgu ģenerēšanai un glabāšanai.
            validation_service: Serviss ievades validācijai.
            log_service: Serviss darbību žurnālam.
        """

        self.crypto_service = crypto_service
        self.file_service = file_service
        self.key_service = key_service
        self.validation_service = validation_service
        self.log_service = log_service

    def encrypt_file(self, request: OperationRequest) -> EncryptionResult:
        """Veic pilna faila šifrēšanas procesa koordinēšanu.

        Args:
            request: Lietotāja pieprasījums šifrēšanas darbībai.

        Returns:
            Standartizēts darbības rezultāts.
        """

        return self._process_request(request, operation="encrypt")

    def decrypt_file(self, request: OperationRequest) -> EncryptionResult:
        """Veic pilna faila atšifrēšanas procesa koordinēšanu.

        Args:
            request: Lietotāja pieprasījums atšifrēšanas darbībai.

        Returns:
            Standartizēts darbības rezultāts.
        """

        return self._process_request(request, operation="decrypt")

    def generate_new_key(self) -> bytes:
        """Izsauc atslēgu servisu jaunas atslēgas iegūšanai.

        Returns:
            Jauna šifrēšanas atslēga baitos.
        """

        key = self.key_service.generate_key()
        self.log_service.info("Izveidota jauna šifrēšanas atslēga.")
        return key

    def save_key_to_file(self, key: bytes, path: str) -> Path:
        """Saglabā atslēgu lietotāja norādītajā failā.

        Args:
            key: Saglabājamā atslēga baitos.
            path: Ceļš uz failu, kur atslēgu saglabāt.

        Returns:
            Ceļš uz saglabāto atslēgas failu.
        """

        self.validation_service.validate_key(key)
        key_path = self.key_service.save_key(path, key)
        self.log_service.info(f"Atslēga saglabāta failā: {key_path}")
        return key_path

    def load_key_from_file(self, path: str) -> bytes:
        """Ielādē atslēgu no norādītā faila.

        Args:
            path: Ceļš uz atslēgas failu.

        Returns:
            Ielādētā atslēga baitos.
        """

        key = self.key_service.load_key(path)
        self.validation_service.validate_key(key)
        self.log_service.info(f"Atslēga ielādēta no faila: {path}")
        return key

    def build_output_path(self, source_path: str, operation: str) -> str:
        """Izveido gala faila ceļu atkarībā no darbības veida.

        Args:
            source_path: Avota faila ceļš.
            operation: Darbība, piemēram, `encrypt` vai `decrypt`.

        Returns:
            Aprēķinātais gala faila ceļš.
        """

        if operation == "encrypt":
            return self.file_service.build_encrypted_file_path(source_path)
        if operation == "decrypt":
            return self.file_service.build_decrypted_file_path(source_path)

        raise ValidationError("Nepareiza darbība gala faila ceļa veidošanai.")

    def _process_request(
        self,
        request: OperationRequest,
        operation: str,
    ) -> EncryptionResult:
        """Apstrādā vienu šifrēšanas vai atšifrēšanas pieprasījumu."""

        output_path = request.output_file_path

        try:
            if request.operation != operation:
                raise ValidationError("Pieprasījuma darbība nesakrīt ar izvēlēto metodi.")

            self.validation_service.validate_operation_request(request)
            source_data = self.file_service.read_bytes(request.source_file_path)
            key = self._resolve_key(request)
            output_path = request.output_file_path or self.build_output_path(
                request.source_file_path,
                operation,
            )
            self.validation_service.validate_output_path(output_path)

            if not request.overwrite_existing and not self.file_service.safe_overwrite_check(output_path):
                raise ValidationError(
                    "Gala fails jau eksistē. Izvēlies citu ceļu vai atļauj pārrakstīšanu."
                )

            if operation == "encrypt":
                result_data = self.crypto_service.encrypt_bytes(source_data, key)
                success_message = "Fails veiksmīgi sašifrēts."
            else:
                result_data = self.crypto_service.decrypt_bytes(source_data, key)
                success_message = "Fails veiksmīgi atšifrēts."

            saved_path = self.file_service.write_bytes(output_path, result_data)
            self.log_service.info(
                f"{operation} veiksmīga: {request.source_file_path} -> {saved_path}"
            )
            return EncryptionResult(
                success=True,
                message=success_message,
                source_path=request.source_file_path,
                output_path=str(saved_path),
                operation=operation,
                file_size_before=len(source_data),
                file_size_after=len(result_data),
            )
        except AppError as exc:
            self.log_service.warning(
                f"{operation} neizdevās failam {request.source_file_path}: {exc}"
            )
            return EncryptionResult(
                success=False,
                message=self._build_error_message(exc, operation),
                source_path=request.source_file_path,
                output_path=output_path,
                operation=operation,
            )
        except Exception as exc:
            self.log_service.error(f"Negaidīta kļūda darbībā {operation}.", exc)
            return EncryptionResult(
                success=False,
                message=self._build_unexpected_error_message(operation),
                source_path=request.source_file_path,
                output_path=output_path,
                operation=operation,
            )

    def _resolve_key(self, request: OperationRequest) -> bytes:
        """Iegūst atslēgu no pieprasījuma vai no atslēgas faila."""

        if request.key is not None:
            self.validation_service.validate_key(request.key)
            return request.key

        if request.key_file_path is None:
            raise ValidationError("Nav norādīta atslēga vai atslēgas fails.")

        return self.load_key_from_file(request.key_file_path)

    def _build_error_message(self, exc: AppError, operation: str) -> str:
        """Pārvērš sistēmas kļūdu par saprotamu ziņu lietotājam."""

        if isinstance(exc, ValidationError):
            return "Darbību nevar izpildīt. Pārbaudi ievadītos datus."
        if isinstance(exc, FileAccessError):
            return "Neizdevās piekļūt failam. Pārbaudi ceļu un faila tiesības."
        if isinstance(exc, KeyErrorInvalid):
            return "Atslēga nav derīga. Pārbaudi izvēlēto atslēgu."
        if isinstance(exc, EncryptionProcessError) and operation == "decrypt":
            return "Atšifrēšana neizdevās. Pārbaudi, vai atslēga ir pareiza un fails nav bojāts."
        if isinstance(exc, EncryptionProcessError):
            return "Šifrēšana neizdevās. Mēģini vēlreiz ar korektu failu un atslēgu."

        return "Darbība neizdevās."

    def _build_unexpected_error_message(self, operation: str) -> str:
        """Atgriež īsu ziņu negaidītas kļūdas gadījumam."""

        if operation == "encrypt":
            return "Šifrēšana neizdevās negaidītas kļūdas dēļ."

        return "Atšifrēšana neizdevās negaidītas kļūdas dēļ."
