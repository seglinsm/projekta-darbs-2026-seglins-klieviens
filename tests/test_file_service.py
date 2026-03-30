"""FileService testu skelets."""

from pathlib import Path

import pytest

from app.services.file_service import FileService


def test_read_write_bytes(tmp_path: Path) -> None:
    """Pārbauda, vai serviss var saglabāt un nolasīt faila saturu."""

    service = FileService()
    file_path = tmp_path / "data.bin"
    data = b"Testa dati"

    written_path = service.write_bytes(str(file_path), data)

    assert written_path == file_path
    assert service.file_exists(str(file_path)) is True
    assert service.is_file_readable(str(file_path)) is True
    assert service.is_file_writable(str(file_path)) is True
    assert service.read_bytes(str(file_path)) == data
    assert service.get_file_size(str(file_path)) == len(data)


def test_build_encrypted_file_path(tmp_path: Path) -> None:
    """Pārbauda, vai serviss veido jaunu ceļu šifrētam failam."""

    service = FileService()
    original_path = tmp_path / "dokuments.txt"

    encrypted_path = service.build_encrypted_file_path(str(original_path))

    assert Path(encrypted_path).name == "dokuments.txt.encrypted"


def test_build_decrypted_file_path_preserves_extension(tmp_path: Path) -> None:
    """Pārbauda, vai atšifrētam failam tiek saglabāts saprotams paplašinājums."""

    service = FileService()
    encrypted_path = tmp_path / "attels.jpg.encrypted"

    decrypted_path = service.build_decrypted_file_path(str(encrypted_path))

    assert Path(decrypted_path).name == "attels.decrypted.jpg"


def test_safe_overwrite_check_rejects_existing_file(tmp_path: Path) -> None:
    """Pārbauda, vai esošs gala fails netiek uzskatīts par drošu pārrakstīšanai."""

    service = FileService()
    existing_file = tmp_path / "jau_ir.encrypted"
    existing_file.write_bytes(b"dati")

    assert service.safe_overwrite_check(str(existing_file)) is False
