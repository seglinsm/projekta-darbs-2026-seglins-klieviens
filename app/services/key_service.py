"""Atslēgu pārvaldības servisa skelets."""

from __future__ import annotations

from pathlib import Path


class KeyService:
    """Atbild par šifrēšanas atslēgu ģenerēšanu un glabāšanu."""

    def generate_key(self) -> bytes:
        """Izveido jaunu šifrēšanas atslēgu.

        Returns:
            Jaunā atslēga baitos.
        """

        raise NotImplementedError("Atslēgas ģenerēšana vēl nav izveidota.")

    def save_key(self, path: str, key: bytes) -> Path:
        """Saglabā atslēgu failā.

        Args:
            path: Ceļš uz atslēgas failu.
            key: Saglabājamā atslēga baitos.

        Returns:
            Ceļš uz saglabāto atslēgas failu.
        """

        raise NotImplementedError("Atslēgas saglabāšana vēl nav izveidota.")

    def load_key(self, path: str) -> bytes:
        """Ielādē atslēgu no faila.

        Args:
            path: Ceļš uz atslēgas failu.

        Returns:
            Ielādētā atslēga baitos.
        """

        raise NotImplementedError("Atslēgas ielāde vēl nav izveidota.")

    def validate_key_file(self, path: str) -> bool:
        """Pārbauda, vai atslēgas fails satur lietojamu atslēgu.

        Args:
            path: Ceļš uz atslēgas failu.

        Returns:
            `True`, ja fails ir derīgs, pretējā gadījumā `False`.
        """

        raise NotImplementedError("Atslēgas faila validācija vēl nav izveidota.")

    def export_key_as_text(self, key: bytes) -> str:
        """Pārvērš atslēgu tekstā ērtākai attēlošanai.

        Args:
            key: Atveidojamā atslēga baitos.

        Returns:
            Atslēga teksta formā.
        """

        raise NotImplementedError("Atslēgas eksportēšana tekstā vēl nav izveidota.")

    def import_key_from_text(self, key_text: str) -> bytes:
        """Pārvērš tekstu atslēgas baitu formā.

        Args:
            key_text: Atslēga teksta formā.

        Returns:
            Atslēga baitos.
        """

        raise NotImplementedError("Atslēgas importēšana no teksta vēl nav izveidota.")
