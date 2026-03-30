"""EncryptionController testu skelets."""

import pytest

from app.controllers.encryption_controller import EncryptionController
from app.services.crypto_service import CryptoService
from app.services.file_service import FileService
from app.services.key_service import KeyService
from app.services.log_service import LogService
from app.services.validation_service import ValidationService


@pytest.mark.skip(reason="Sākotnējais testa skelets bez implementācijas.")
def test_encrypt_file_returns_result_object() -> None:
    """Pārbauda, vai kontrolieris atgriež rezultāta objektu šifrēšanai."""

    controller = EncryptionController(
        crypto_service=CryptoService(),
        file_service=FileService(),
        key_service=KeyService(),
        validation_service=ValidationService(),
        log_service=LogService(),
    )
    assert controller is not None


@pytest.mark.skip(reason="Sākotnējais testa skelets bez implementācijas.")
def test_decrypt_file_returns_result_object() -> None:
    """Pārbauda, vai kontrolieris atgriež rezultāta objektu atšifrēšanai."""

    controller = EncryptionController(
        crypto_service=CryptoService(),
        file_service=FileService(),
        key_service=KeyService(),
        validation_service=ValidationService(),
        log_service=LogService(),
    )
    assert controller is not None
