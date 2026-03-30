"""EncryptionController testu komplekts."""

from pathlib import Path

from app.controllers.encryption_controller import EncryptionController
from app.models.operation_request import OperationRequest
from app.services.crypto_service import CryptoService
from app.services.file_service import FileService
from app.services.key_service import KeyService
from app.services.log_service import LogService
from app.services.validation_service import ValidationService


def _build_controller(tmp_path: Path) -> EncryptionController:
    """Izveido kontrolieri ar īstu servisu komplektu testiem."""

    return EncryptionController(
        crypto_service=CryptoService(),
        file_service=FileService(),
        key_service=KeyService(),
        validation_service=ValidationService(),
        log_service=LogService(log_file_path=str(tmp_path / "app.log")),
    )


def test_controller_constructor_stores_services(tmp_path: Path) -> None:
    """Pārbauda, vai kontrolieris saglabā padotos servisus."""

    crypto_service = CryptoService()
    file_service = FileService()
    key_service = KeyService()
    validation_service = ValidationService()
    log_service = LogService(log_file_path=str(tmp_path / "controller.log"))
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


def test_encrypt_file_success(tmp_path: Path) -> None:
    """Pārbauda veiksmīgu šifrēšanas plūsmu."""

    controller = _build_controller(tmp_path)
    source_file = tmp_path / "dokuments.txt"
    original_data = b"Slepeni dati"
    source_file.write_bytes(original_data)
    key = controller.generate_new_key()

    result = controller.encrypt_file(
        OperationRequest(
            source_file_path=str(source_file),
            operation="encrypt",
            key=key,
        )
    )

    assert result.success is True
    assert result.output_path is not None
    assert Path(result.output_path).exists() is True
    assert Path(result.output_path).read_bytes() != original_data
    assert result.file_size_before == len(original_data)


def test_decrypt_file_success(tmp_path: Path) -> None:
    """Pārbauda veiksmīgu atšifrēšanas plūsmu."""

    controller = _build_controller(tmp_path)
    source_file = tmp_path / "slepens.txt"
    original_data = b"Atjaunojami dati"
    source_file.write_bytes(original_data)
    key = controller.generate_new_key()

    encrypt_result = controller.encrypt_file(
        OperationRequest(
            source_file_path=str(source_file),
            operation="encrypt",
            key=key,
        )
    )
    decrypt_result = controller.decrypt_file(
        OperationRequest(
            source_file_path=encrypt_result.output_path or "",
            operation="decrypt",
            key=key,
        )
    )

    assert encrypt_result.success is True
    assert decrypt_result.success is True
    assert decrypt_result.output_path is not None
    assert Path(decrypt_result.output_path).read_bytes() == original_data


def test_wrong_key_returns_failed_result(tmp_path: Path) -> None:
    """Pārbauda, vai nepareiza atslēga atgriež saprotamu neveiksmes rezultātu."""

    controller = _build_controller(tmp_path)
    source_file = tmp_path / "nepareiza_atslega.txt"
    source_file.write_bytes(b"Svarigi dati")
    correct_key = controller.generate_new_key()
    wrong_key = controller.generate_new_key()

    encrypt_result = controller.encrypt_file(
        OperationRequest(
            source_file_path=str(source_file),
            operation="encrypt",
            key=correct_key,
        )
    )
    decrypt_result = controller.decrypt_file(
        OperationRequest(
            source_file_path=encrypt_result.output_path or "",
            operation="decrypt",
            key=wrong_key,
        )
    )

    assert decrypt_result.success is False
    assert "Atšifrēšana neizdevās" in decrypt_result.message


def test_key_loaded_from_file(tmp_path: Path) -> None:
    """Pārbauda, vai kontrolieris var izmantot atslēgu no faila."""

    controller = _build_controller(tmp_path)
    source_file = tmp_path / "fails.txt"
    key_file = tmp_path / "fails.key"
    source_file.write_bytes(b"Testa saturs")
    key = controller.generate_new_key()
    controller.save_key_to_file(key, str(key_file))

    result = controller.encrypt_file(
        OperationRequest(
            source_file_path=str(source_file),
            operation="encrypt",
            key_file_path=str(key_file),
        )
    )

    assert result.success is True
    assert result.output_path is not None
    assert Path(result.output_path).exists() is True


def test_encrypt_file_rejects_overwrite_by_default(tmp_path: Path) -> None:
    """Pārbauda, vai gala fails pēc noklusējuma netiek pārrakstīts."""

    controller = _build_controller(tmp_path)
    source_file = tmp_path / "jautajums.txt"
    source_file.write_bytes(b"Dati bez parslegsanas")
    key = controller.generate_new_key()

    first_result = controller.encrypt_file(
        OperationRequest(
            source_file_path=str(source_file),
            operation="encrypt",
            key=key,
        )
    )
    second_result = controller.encrypt_file(
        OperationRequest(
            source_file_path=str(source_file),
            operation="encrypt",
            key=key,
        )
    )

    assert first_result.success is True
    assert second_result.success is False
    assert "Gala fails jau eksistē" in second_result.message
