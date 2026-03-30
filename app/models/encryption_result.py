"""Darbības rezultāta datu modeļa definīcija."""

from dataclasses import dataclass


@dataclass
class EncryptionResult:
    """Apraksta šifrēšanas vai atšifrēšanas procesa rezultātu."""

    success: bool
    message: str
    source_path: str
    output_path: str | None
    operation: str
    file_size_before: int | None = None
    file_size_after: int | None = None
