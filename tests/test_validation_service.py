"""ValidationService testu skelets."""

from pathlib import Path

from cryptography.fernet import Fernet
import pytest

from app.services.validation_service import ValidationService


def test_validate_file_path_rejects_empty_path() -> None:
    """Pārbauda, vai tukšs ceļš tiek noraidīts."""

    service = ValidationService()

    with pytest.raises(ValueError):
        service.validate_file_path("   ")


def test_validate_key_rejects_invalid_key() -> None:
    """Pārbauda, vai nederīga atslēga tiek noraidīta."""

    service = ValidationService()

    with pytest.raises(ValueError):
        service.validate_key(b"nederiga-atslega")


def test_validate_output_path_rejects_missing_folder(tmp_path: Path) -> None:
    """Pārbauda, vai neesoša gala mape tiek noraidīta."""

    service = ValidationService()
    output_path = tmp_path / "nav_mapes" / "fails.encrypted"

    with pytest.raises(FileNotFoundError):
        service.validate_output_path(str(output_path))


def test_validate_key_accepts_valid_key() -> None:
    """Pārbauda, vai derīga atslēga tiek pieņemta bez kļūdas."""

    service = ValidationService()
    valid_key = Fernet.generate_key()

    service.validate_key(valid_key)
