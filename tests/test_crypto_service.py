"""CryptoService testu skelets."""

import pytest

from app.services.crypto_service import CryptoService


@pytest.mark.skip(reason="Sākotnējais testa skelets bez implementācijas.")
def test_encrypt_bytes_returns_encrypted_data() -> None:
    """Pārbauda, vai serviss spēj sagatavot šifrētu rezultātu."""

    service = CryptoService()
    assert service is not None


@pytest.mark.skip(reason="Sākotnējais testa skelets bez implementācijas.")
def test_decrypt_bytes_restores_original_data() -> None:
    """Pārbauda, vai serviss spēj atjaunot sākotnējos datus."""

    service = CryptoService()
    assert service is not None
