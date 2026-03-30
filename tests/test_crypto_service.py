"""CryptoService testu skelets."""

from cryptography.fernet import Fernet
import pytest

from app.services.crypto_service import CryptoService


def test_encrypt_decrypt_roundtrip() -> None:
    """Pārbauda, vai datus var veiksmīgi sašifrēt un atšifrēt."""

    service = CryptoService()
    key = Fernet.generate_key()
    data = b"Slepeni dati"

    encrypted_data = service.encrypt_bytes(data, key)
    decrypted_data = service.decrypt_bytes(encrypted_data, key)

    assert encrypted_data != data
    assert decrypted_data == data


def test_invalid_key_rejection() -> None:
    """Pārbauda, vai nederīga atslēga tiek noraidīta."""

    service = CryptoService()
    invalid_key = b"nederiga-atslega"

    assert service.is_valid_key(invalid_key) is False

    with pytest.raises(ValueError):
        service.encrypt_bytes(b"dati", invalid_key)
