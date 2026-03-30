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

        raise NotImplementedError("Šifrēšanas plūsma vēl nav izveidota.")

    def decrypt_file(self, request: OperationRequest) -> EncryptionResult:
        """Veic pilna faila atšifrēšanas procesa koordinēšanu.

        Args:
            request: Lietotāja pieprasījums atšifrēšanas darbībai.

        Returns:
            Standartizēts darbības rezultāts.
        """

        raise NotImplementedError("Atšifrēšanas plūsma vēl nav izveidota.")

    def generate_new_key(self) -> bytes:
        """Izsauc atslēgu servisu jaunas atslēgas iegūšanai.

        Returns:
            Jauna šifrēšanas atslēga baitos.
        """

        raise NotImplementedError("Atslēgas ģenerēšana vēl nav izveidota.")

    def save_key_to_file(self, key: bytes, path: str) -> Path:
        """Saglabā atslēgu lietotāja norādītajā failā.

        Args:
            key: Saglabājamā atslēga baitos.
            path: Ceļš uz failu, kur atslēgu saglabāt.

        Returns:
            Ceļš uz saglabāto atslēgas failu.
        """

        raise NotImplementedError("Atslēgas saglabāšana vēl nav izveidota.")

    def load_key_from_file(self, path: str) -> bytes:
        """Ielādē atslēgu no norādītā faila.

        Args:
            path: Ceļš uz atslēgas failu.

        Returns:
            Ielādētā atslēga baitos.
        """

        raise NotImplementedError("Atslēgas ielāde vēl nav izveidota.")

    def build_output_path(self, source_path: str, operation: str) -> str:
        """Izveido gala faila ceļu atkarībā no darbības veida.

        Args:
            source_path: Avota faila ceļš.
            operation: Darbība, piemēram, `encrypt` vai `decrypt`.

        Returns:
            Aprēķinātais gala faila ceļš.
        """

        raise NotImplementedError("Gala faila ceļa veidošana vēl nav izveidota.")
