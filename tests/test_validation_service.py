"""ValidationService testu skelets."""

import pytest

from app.services.validation_service import ValidationService


@pytest.mark.skip(reason="Sākotnējais testa skelets bez implementācijas.")
def test_validate_file_path_rejects_empty_path() -> None:
    """Pārbauda, vai tukšs ceļš tiek noraidīts."""

    service = ValidationService()
    assert service is not None


@pytest.mark.skip(reason="Sākotnējais testa skelets bez implementācijas.")
def test_validate_key_rejects_invalid_key() -> None:
    """Pārbauda, vai nederīga atslēga tiek noraidīta."""

    service = ValidationService()
    assert service is not None
