"""LogService pamata testi."""

from pathlib import Path

from app.services.log_service import LogService


def test_log_service_writes_messages_to_file(tmp_path: Path) -> None:
    """Pārbauda, vai log serviss izveido failu un ieraksta ziņojumus."""

    log_file = tmp_path / "logs" / "app.log"
    service = LogService(log_file_path=str(log_file))

    service.info("Informācijas ieraksts")
    service.warning("Brīdinājuma ieraksts")
    service.error("Kļūdas ieraksts", ValueError("Piemēra kļūda"))

    log_text = log_file.read_text(encoding="utf-8")

    assert "Informācijas ieraksts" in log_text
    assert "Brīdinājuma ieraksts" in log_text
    assert "Kļūdas ieraksts" in log_text
    assert "ValueError" in log_text
