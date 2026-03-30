"""Ievades validācijas servisa skelets."""

from app.models.operation_request import OperationRequest


class ValidationService:
    """Pārbauda lietotāja ievadi pirms apstrādes uzsākšanas."""

    def validate_operation_request(self, request: OperationRequest) -> None:
        """Pārbauda pilnu lietotāja pieprasījumu.

        Args:
            request: Lietotāja pieprasījums šifrēšanai vai atšifrēšanai.
        """

        raise NotImplementedError("Pieprasījuma validācija vēl nav izveidota.")

    def validate_file_path(self, path: str) -> None:
        """Pārbauda, vai faila ceļš ir derīgs.

        Args:
            path: Pārbaudāmais faila ceļš.
        """

        raise NotImplementedError("Faila ceļa validācija vēl nav izveidota.")

    def validate_key(self, key: bytes) -> None:
        """Pārbauda, vai atslēga ir derīgā formātā.

        Args:
            key: Pārbaudāmā atslēga baitos.
        """

        raise NotImplementedError("Atslēgas validācija vēl nav izveidota.")

    def validate_output_path(self, path: str) -> None:
        """Pārbauda, vai gala ceļš ir drošs saglabāšanai.

        Args:
            path: Pārbaudāmais gala faila ceļš.
        """

        raise NotImplementedError("Gala ceļa validācija vēl nav izveidota.")
