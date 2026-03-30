"""Lietotnes konfigurācijas datu modeļa definīcija."""

from dataclasses import dataclass


@dataclass
class AppConfig:
    """Glabā vienkāršus lietotnes konfigurācijas iestatījumus."""

    app_name: str
    default_output_dir: str | None
    log_file_path: str
    allow_overwrite: bool
    theme_name: str
