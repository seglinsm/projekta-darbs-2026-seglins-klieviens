"""FileService testu skelets."""

import pytest

from app.services.file_service import FileService


@pytest.mark.skip(reason="Sākotnējais testa skelets bez implementācijas.")
def test_read_bytes_reads_file_content() -> None:
    """Pārbauda, vai serviss var nolasīt faila saturu."""

    service = FileService()
    assert service is not None


@pytest.mark.skip(reason="Sākotnējais testa skelets bez implementācijas.")
def test_build_encrypted_file_path_creates_new_path() -> None:
    """Pārbauda, vai serviss veido jaunu ceļu šifrētam failam."""

    service = FileService()
    assert service is not None
