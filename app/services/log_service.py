"""Vienkāršs lokālais žurnāla serviss."""

from __future__ import annotations

import logging
from pathlib import Path


class LogService:
    """Reģistrē lietotnes darbības un kļūdas lokālā žurnālā."""

    def __init__(self, log_file_path: str = "logs/app.log") -> None:
        """Inicializē žurnāla servisu un sagatavo log faila ceļu.

        Args:
            log_file_path: Ceļš uz lokālo log failu.
        """

        self.log_file_path = Path(log_file_path)
        self.logger = logging.getLogger(f"file_security_app.{id(self)}")
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
        self.configure()

    def configure(self) -> None:
        """Inicializē žurnāla konfigurāciju."""

        self.log_file_path.parent.mkdir(parents=True, exist_ok=True)
        if self.logger.handlers:
            return

        file_handler = logging.FileHandler(self.log_file_path, encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def info(self, message: str) -> None:
        """Saglabā informatīvu ierakstu.

        Args:
            message: Ziņojuma teksts.
        """

        self.configure()
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """Saglabā brīdinājuma ierakstu.

        Args:
            message: Ziņojuma teksts.
        """

        self.configure()
        self.logger.warning(message)

    def error(self, message: str, exc: Exception | None = None) -> None:
        """Saglabā kļūdas ierakstu.

        Args:
            message: Ziņojuma teksts.
            exc: Papildu izņēmuma objekts, ja pieejams.
        """

        self.configure()
        if exc is None:
            self.logger.error(message)
            return

        self.logger.error("%s | %s: %s", message, exc.__class__.__name__, exc)
