"""Ievades validācijas servisa skelets."""

from pathlib import Path

from app.models.operation_request import OperationRequest
from app.services.crypto_service import CryptoService
from app.utils.exceptions import FileAccessError, KeyErrorInvalid, ValidationError


class ValidationService:
    """Pārbauda lietotāja ievadi pirms apstrādes uzsākšanas."""

    def validate_operation_request(self, request: OperationRequest) -> None:
        """Pārbauda pilnu lietotāja pieprasījumu.

        Args:
            request: Lietotāja pieprasījums šifrēšanai vai atšifrēšanai.
        """

        if request.operation not in {"encrypt", "decrypt"}:
            raise ValidationError("Darbībai jābūt 'encrypt' vai 'decrypt'.")

        self.validate_file_path(request.source_file_path)

        if request.key is not None:
            self.validate_key(request.key)
        elif request.key_file_path:
            self.validate_file_path(request.key_file_path)
        else:
            raise ValidationError("Jānorāda atslēga vai atslēgas fails.")

        if request.output_file_path is not None:
            self.validate_output_path(request.output_file_path)

    def validate_file_path(self, path: str) -> None:
        """Pārbauda, vai faila ceļš ir derīgs.

        Args:
            path: Pārbaudāmais faila ceļš.
        """

        if not path.strip():
            raise ValidationError("Faila ceļš nedrīkst būt tukšs.")

        file_path = Path(path)
        if not file_path.exists():
            raise FileAccessError("Fails nav atrasts.")
        if not file_path.is_file():
            raise FileAccessError("Norādītais ceļš nav fails.")

    def validate_key(self, key: bytes) -> None:
        """Pārbauda, vai atslēga ir derīgā formātā.

        Args:
            key: Pārbaudāmā atslēga baitos.
        """

        if not key:
            raise ValidationError("Atslēga nedrīkst būt tukša.")

        if not CryptoService().is_valid_key(key):
            raise KeyErrorInvalid("Atslēga nav derīga.")

    def validate_output_path(self, path: str) -> None:
        """Pārbauda, vai gala ceļš ir drošs saglabāšanai.

        Args:
            path: Pārbaudāmais gala faila ceļš.
        """

        if not path.strip():
            raise ValidationError("Gala faila ceļš nedrīkst būt tukšs.")

        output_path = Path(path)
        if not output_path.name:
            raise ValidationError("Gala faila ceļš nav derīgs.")
        if not output_path.parent.exists():
            raise FileAccessError("Gala faila mape nav atrasta.")
