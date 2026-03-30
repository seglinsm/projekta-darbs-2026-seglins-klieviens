"""Atslēgu pārvaldības servisa skelets."""

from __future__ import annotations

from pathlib import Path

from cryptography.fernet import Fernet

from app.utils.exceptions import FileAccessError, KeyErrorInvalid, ValidationError


class KeyService:
    """Atbild par šifrēšanas atslēgu ģenerēšanu un glabāšanu."""

    def generate_key(self) -> bytes:
        """Izveido jaunu šifrēšanas atslēgu.

        Returns:
            Jaunā atslēga baitos.
        """

        return Fernet.generate_key()

    def save_key(self, path: str, key: bytes) -> Path:
        """Saglabā atslēgu failā.

        Args:
            path: Ceļš uz atslēgas failu.
            key: Saglabājamā atslēga baitos.

        Returns:
            Ceļš uz saglabāto atslēgas failu.
        """

        if not path.strip():
            raise ValidationError("Atslēgas faila ceļš nedrīkst būt tukšs.")

        key_text = self.export_key_as_text(key)
        key_path = Path(path)
        try:
            key_path.parent.mkdir(parents=True, exist_ok=True)
            key_path.write_text(key_text, encoding="utf-8")
        except OSError as exc:
            raise FileAccessError("Atslēgu neizdevās saglabāt failā.") from exc
        return key_path

    def load_key(self, path: str) -> bytes:
        """Ielādē atslēgu no faila.

        Args:
            path: Ceļš uz atslēgas failu.

        Returns:
            Ielādētā atslēga baitos.
        """

        if not path.strip():
            raise ValidationError("Atslēgas faila ceļš nedrīkst būt tukšs.")

        key_path = Path(path)
        if not key_path.is_file():
            raise FileAccessError("Atslēgas fails nav atrasts.")

        try:
            key_text = key_path.read_text(encoding="utf-8").strip()
        except OSError as exc:
            raise FileAccessError("Atslēgas failu neizdevās nolasīt.") from exc
        return self.import_key_from_text(key_text)

    def validate_key_file(self, path: str) -> bool:
        """Pārbauda, vai atslēgas fails satur lietojamu atslēgu.

        Args:
            path: Ceļš uz atslēgas failu.

        Returns:
            `True`, ja fails ir derīgs, pretējā gadījumā `False`.
        """

        try:
            self.load_key(path)
        except (FileAccessError, KeyErrorInvalid, ValidationError):
            return False

        return True

    def export_key_as_text(self, key: bytes) -> str:
        """Pārvērš atslēgu tekstā ērtākai attēlošanai.

        Args:
            key: Atveidojamā atslēga baitos.

        Returns:
            Atslēga teksta formā.
        """

        self._ensure_valid_key(key)

        try:
            return key.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise KeyErrorInvalid("Atslēgu nevar pārvērst tekstā.") from exc

    def import_key_from_text(self, key_text: str) -> bytes:
        """Pārvērš tekstu atslēgas baitu formā.

        Args:
            key_text: Atslēga teksta formā.

        Returns:
            Atslēga baitos.
        """

        cleaned_key_text = key_text.strip()
        if not cleaned_key_text:
            raise ValidationError("Atslēgas teksts nedrīkst būt tukšs.")

        key_bytes = cleaned_key_text.encode("utf-8")
        self._ensure_valid_key(key_bytes)
        return key_bytes

    def _ensure_valid_key(self, key: bytes) -> None:
        """Pārbauda, vai norādītā atslēga ir derīga Fernet atslēga."""

        try:
            Fernet(key)
        except (TypeError, ValueError) as exc:
            raise KeyErrorInvalid("Atslēga nav derīga Fernet formātā.") from exc
