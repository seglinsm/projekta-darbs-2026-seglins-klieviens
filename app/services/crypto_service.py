"""Kriptogrāfijas serviss darbam ar Fernet šifrēšanu."""

from cryptography.fernet import Fernet, InvalidToken

from app.utils.exceptions import EncryptionProcessError, KeyErrorInvalid


class CryptoService:
    """Apstrādā failu datu šifrēšanu un atšifrēšanu."""

    def encrypt_bytes(self, data: bytes, key: bytes) -> bytes:
        """Šifrē datus ar norādīto atslēgu.

        Args:
            data: Nešifrētie dati baitos.
            key: Šifrēšanas atslēga baitos.

        Returns:
            Šifrētie dati baitos.

        Raises:
            KeyErrorInvalid: Ja atslēga nav derīga.
        """

        if not self.is_valid_key(key):
            raise KeyErrorInvalid("Nederīga šifrēšanas atslēga.")

        return Fernet(key).encrypt(data)

    def decrypt_bytes(self, data: bytes, key: bytes) -> bytes:
        """Atšifrē datus ar norādīto atslēgu.

        Args:
            data: Šifrētie dati baitos.
            key: Atšifrēšanas atslēga baitos.

        Returns:
            Atšifrētie dati baitos.

        Raises:
            KeyErrorInvalid: Ja atslēga nav derīga.
            EncryptionProcessError: Ja atšifrēšana neizdodas.
        """

        if not self.is_valid_key(key):
            raise KeyErrorInvalid("Nederīga atšifrēšanas atslēga.")

        try:
            return Fernet(key).decrypt(data)
        except InvalidToken as exc:
            raise EncryptionProcessError(
                "Atšifrēšana neizdevās. Iespējams, atslēga nav pareiza vai dati ir bojāti."
            ) from exc

    def is_valid_key(self, key: bytes) -> bool:
        """Pārbauda, vai atslēga atbilst paredzētajam formātam.

        Args:
            key: Pārbaudāmā atslēga baitos.

        Returns:
            `True`, ja atslēga ir derīga, pretējā gadījumā `False`.
        """

        if not key:
            return False

        try:
            Fernet(key)
        except (TypeError, ValueError):
            return False

        return True
