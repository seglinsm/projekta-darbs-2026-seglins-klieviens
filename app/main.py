"""Lietotnes palaišanas punkts."""

from __future__ import annotations

from app.controllers.encryption_controller import EncryptionController
from app.gui.main_window import MainWindow
from app.services.crypto_service import CryptoService
from app.services.file_service import FileService
from app.services.key_service import KeyService
from app.services.log_service import LogService
from app.services.validation_service import ValidationService


def build_application() -> MainWindow:
    """Izveido lietotnes objektus un sasaista tos savā starpā."""

    controller = EncryptionController(
        crypto_service=CryptoService(),
        file_service=FileService(),
        key_service=KeyService(),
        validation_service=ValidationService(),
        log_service=LogService(),
    )
    return MainWindow(controller=controller)


def main() -> None:
    """Sagatavo lietotni palaišanai."""

    window = build_application()
    window.run()


if __name__ == "__main__":
    main()
