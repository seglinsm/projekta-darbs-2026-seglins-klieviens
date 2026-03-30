"""Faila datu modeļa definīcija."""

from dataclasses import dataclass


@dataclass
class FileRecord:
    """Glabā pamatinformāciju par izvēlēto failu."""

    path: str
    name: str
    extension: str
    size_bytes: int
