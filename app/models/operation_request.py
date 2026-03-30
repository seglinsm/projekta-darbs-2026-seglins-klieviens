"""Lietotāja pieprasījuma datu modeļa definīcija."""

from dataclasses import dataclass


@dataclass
class OperationRequest:
    """Glabā datus, kas vajadzīgi šifrēšanas vai atšifrēšanas darbībai."""

    source_file_path: str
    operation: str
    key: bytes | None = None
    key_file_path: str | None = None
    output_file_path: str | None = None
    overwrite_existing: bool = False
