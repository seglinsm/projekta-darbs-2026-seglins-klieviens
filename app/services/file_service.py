"""Failu apstrādes servisa skelets."""

from __future__ import annotations

import os
from pathlib import Path

from app.utils.exceptions import FileAccessError, ValidationError


class FileService:
    """Nodrošina failu nolasīšanu, saglabāšanu un ceļu apstrādi."""

    def read_bytes(self, path: str) -> bytes:
        """Nolasa faila saturu binārā veidā.

        Args:
            path: Ceļš uz nolasāmo failu.

        Returns:
            Faila saturs baitos.
        """

        if not path.strip():
            raise ValidationError("Faila ceļš nedrīkst būt tukšs.")

        file_path = Path(path)
        if not file_path.is_file():
            raise FileAccessError("Fails nav atrasts.")

        try:
            return file_path.read_bytes()
        except OSError as exc:
            raise FileAccessError("Failu neizdevās nolasīt.") from exc

    def write_bytes(self, path: str, data: bytes) -> Path:
        """Saglabā datus failā binārā veidā.

        Args:
            path: Ceļš uz failu, kur saglabāt datus.
            data: Saglabājamie dati baitos.

        Returns:
            Ceļš uz saglabāto failu.
        """

        if not path.strip():
            raise ValidationError("Faila ceļš nedrīkst būt tukšs.")

        file_path = Path(path)
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_bytes(data)
        except OSError as exc:
            raise FileAccessError("Failu neizdevās saglabāt.") from exc
        return file_path

    def file_exists(self, path: str) -> bool:
        """Pārbauda, vai fails eksistē.

        Args:
            path: Ceļš uz pārbaudāmo failu.

        Returns:
            `True`, ja fails eksistē, pretējā gadījumā `False`.
        """

        if not path.strip():
            return False

        return Path(path).is_file()

    def is_file_readable(self, path: str) -> bool:
        """Pārbauda, vai fails ir nolasāms.

        Args:
            path: Ceļš uz pārbaudāmo failu.

        Returns:
            `True`, ja failu var nolasīt, pretējā gadījumā `False`.
        """

        if not self.file_exists(path):
            return False

        return os.access(path, os.R_OK)

    def is_file_writable(self, path: str) -> bool:
        """Pārbauda, vai failu var pārrakstīt vai izveidot.

        Args:
            path: Ceļš uz pārbaudāmo failu.

        Returns:
            `True`, ja failu var ierakstīt, pretējā gadījumā `False`.
        """

        if not path.strip():
            return False

        file_path = Path(path)
        if file_path.exists():
            return os.access(file_path, os.W_OK)

        return file_path.parent.exists() and os.access(file_path.parent, os.W_OK)

    def build_encrypted_file_path(self, original_path: str) -> str:
        """Izveido gala ceļu šifrētam failam.

        Args:
            original_path: Sākotnējā faila ceļš.

        Returns:
            Jaunais ceļš šifrētajam failam.
        """

        if not original_path.strip():
            raise ValidationError("Sākotnējais ceļš nedrīkst būt tukšs.")

        return str(Path(original_path).with_suffix(".encrypted"))

    def build_decrypted_file_path(self, original_path: str) -> str:
        """Izveido gala ceļu atšifrētam failam.

        Args:
            original_path: Sākotnējā faila ceļš.

        Returns:
            Jaunais ceļš atšifrētajam failam.
        """

        if not original_path.strip():
            raise ValidationError("Sākotnējais ceļš nedrīkst būt tukšs.")

        return str(Path(original_path).with_suffix(".decrypted"))

    def get_file_size(self, path: str) -> int:
        """Atgriež faila izmēru baitos.

        Args:
            path: Ceļš uz pārbaudāmo failu.

        Returns:
            Faila izmērs baitos.
        """

        if not path.strip():
            raise ValidationError("Faila ceļš nedrīkst būt tukšs.")

        file_path = Path(path)
        if not file_path.is_file():
            raise FileAccessError("Fails nav atrasts.")

        try:
            return file_path.stat().st_size
        except OSError as exc:
            raise FileAccessError("Faila izmēru neizdevās noteikt.") from exc

    def safe_overwrite_check(self, path: str) -> bool:
        """Pārbauda, vai gala failu drīkst droši pārrakstīt.

        Args:
            path: Ceļš uz gala failu.

        Returns:
            `True`, ja pārrakstīšana ir atļauta, pretējā gadījumā `False`.
        """

        if not path.strip():
            return False

        return not Path(path).exists()
