"""EncryptionController vienkāršs tests."""

from app.controllers.encryption_controller import EncryptionController
from app.services.crypto_service import CryptoService
from app.services.file_service import FileService
from app.services.key_service import KeyService
from app.services.log_service import LogService
from app.services.validation_service import ValidationService


def test_controller_constructor_stores_services() -> None:
    """Pārbauda, vai kontrolieris saglabā padotos servisus."""

    crypto_service = CryptoService()
    file_service = FileService()
    key_service = KeyService()
    validation_service = ValidationService()
    log_service = LogService()
    controller = EncryptionController(
        crypto_service=crypto_service,
        file_service=file_service,
        key_service=key_service,
        validation_service=validation_service,
        log_service=log_service,
    )

    assert controller.crypto_service is crypto_service
    assert controller.file_service is file_service
    assert controller.key_service is key_service
    assert controller.validation_service is validation_service
    assert controller.log_service is log_service
