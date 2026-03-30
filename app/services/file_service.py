"""Failu apstrādes servisa skelets."""

from __future__ import annotations

from pathlib import Path


class FileService:
    """Nodrošina failu nolasīšanu, saglabāšanu un ceļu apstrādi."""

    def read_bytes(self, path: str) -> bytes:
        """Nolasa faila saturu binārā veidā.

        Args:
            path: Ceļš uz nolasāmo failu.

        Returns:
            Faila saturs baitos.
        """

        raise NotImplementedError("Faila nolasīšana vēl nav izveidota.")

    def write_bytes(self, path: str, data: bytes) -> Path:
        """Saglabā datus failā binārā veidā.

        Args:
            path: Ceļš uz failu, kur saglabāt datus.
            data: Saglabājamie dati baitos.

        Returns:
            Ceļš uz saglabāto failu.
        """

        raise NotImplementedError("Faila saglabāšana vēl nav izveidota.")

    def file_exists(self, path: str) -> bool:
        """Pārbauda, vai fails eksistē.

        Args:
            path: Ceļš uz pārbaudāmo failu.

        Returns:
            `True`, ja fails eksistē, pretējā gadījumā `False`.
        """

        raise NotImplementedError("Faila esamības pārbaude vēl nav izveidota.")

    def is_file_readable(self, path: str) -> bool:
        """Pārbauda, vai fails ir nolasāms.

        Args:
            path: Ceļš uz pārbaudāmo failu.

        Returns:
            `True`, ja failu var nolasīt, pretējā gadījumā `False`.
        """

        raise NotImplementedError("Lasīšanas tiesību pārbaude vēl nav izveidota.")

    def is_file_writable(self, path: str) -> bool:
        """Pārbauda, vai failu var pārrakstīt vai izveidot.

        Args:
            path: Ceļš uz pārbaudāmo failu.

        Returns:
            `True`, ja failu var ierakstīt, pretējā gadījumā `False`.
        """

        raise NotImplementedError("Rakstīšanas tiesību pārbaude vēl nav izveidota.")

    def build_encrypted_file_path(self, original_path: str) -> str:
        """Izveido gala ceļu šifrētam failam.

        Args:
            original_path: Sākotnējā faila ceļš.

        Returns:
            Jaunais ceļš šifrētajam failam.
        """

        raise NotImplementedError("Šifrētā faila ceļa veidošana vēl nav izveidota.")

    def build_decrypted_file_path(self, original_path: str) -> str:
        """Izveido gala ceļu atšifrētam failam.

        Args:
            original_path: Sākotnējā faila ceļš.

        Returns:
            Jaunais ceļš atšifrētajam failam.
        """

        raise NotImplementedError("Atšifrētā faila ceļa veidošana vēl nav izveidota.")

    def get_file_size(self, path: str) -> int:
        """Atgriež faila izmēru baitos.

        Args:
            path: Ceļš uz pārbaudāmo failu.

        Returns:
            Faila izmērs baitos.
        """

        raise NotImplementedError("Faila izmēra noteikšana vēl nav izveidota.")

    def safe_overwrite_check(self, path: str) -> bool:
        """Pārbauda, vai gala failu drīkst droši pārrakstīt.

        Args:
            path: Ceļš uz gala failu.

        Returns:
            `True`, ja pārrakstīšana ir atļauta, pretējā gadījumā `False`.
        """

        raise NotImplementedError("Pārrakstīšanas pārbaude vēl nav izveidota.")
