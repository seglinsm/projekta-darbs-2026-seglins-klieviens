"""Kriptogrāfijas servisa skelets."""


class CryptoService:
    """Apstrādā failu datu šifrēšanu un atšifrēšanu."""

    def encrypt_bytes(self, data: bytes, key: bytes) -> bytes:
        """Šifrē datus ar norādīto atslēgu.

        Args:
            data: Nešifrētie dati baitos.
            key: Šifrēšanas atslēga baitos.

        Returns:
            Šifrētie dati baitos.
        """

        raise NotImplementedError("Šifrēšanas loģika vēl nav izveidota.")

    def decrypt_bytes(self, data: bytes, key: bytes) -> bytes:
        """Atšifrē datus ar norādīto atslēgu.

        Args:
            data: Šifrētie dati baitos.
            key: Atšifrēšanas atslēga baitos.

        Returns:
            Atšifrētie dati baitos.
        """

        raise NotImplementedError("Atšifrēšanas loģika vēl nav izveidota.")

    def is_valid_key(self, key: bytes) -> bool:
        """Pārbauda, vai atslēga atbilst paredzētajam formātam.

        Args:
            key: Pārbaudāmā atslēga baitos.

        Returns:
            `True`, ja atslēga ir derīga, pretējā gadījumā `False`.
        """

        raise NotImplementedError("Atslēgas validācija vēl nav izveidota.")
