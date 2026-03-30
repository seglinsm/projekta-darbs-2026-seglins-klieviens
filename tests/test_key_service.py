"""KeyService testu skelets."""

import pytest

from app.services.key_service import KeyService


@pytest.mark.skip(reason="Sākotnējais testa skelets bez implementācijas.")
def test_generate_key_returns_bytes() -> None:
    """Pārbauda, vai atslēgas ģenerēšana atgriež baitus."""

    service = KeyService()
    assert service is not None


@pytest.mark.skip(reason="Sākotnējais testa skelets bez implementācijas.")
def test_save_and_load_key_roundtrip() -> None:
    """Pārbauda, vai atslēgu var saglabāt un vēlāk ielādēt."""

    service = KeyService()
    assert service is not None
