"""KeyService testu skelets."""

from pathlib import Path

import pytest

from app.services.key_service import KeyService


def test_save_and_load_key_roundtrip(tmp_path: Path) -> None:
    """Pārbauda, vai atslēgu var saglabāt un vēlāk ielādēt."""

    service = KeyService()
    key = service.generate_key()
    key_path = tmp_path / "secret.key"

    saved_path = service.save_key(str(key_path), key)
    loaded_key = service.load_key(str(key_path))

    assert saved_path == key_path
    assert loaded_key == key
    assert service.validate_key_file(str(key_path)) is True


def test_import_key_from_text_rejects_invalid_value() -> None:
    """Pārbauda, vai nederīgs atslēgas teksts tiek noraidīts."""

    service = KeyService()

    with pytest.raises(ValueError):
        service.import_key_from_text("nederiga-atslega")
