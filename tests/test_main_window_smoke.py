"""Ļoti viegls MainWindow smoke tests."""

import tkinter as tk
from pathlib import Path

import pytest

from app.controllers.encryption_controller import EncryptionController
from app.gui.main_window import MainWindow
from app.services.crypto_service import CryptoService
from app.services.file_service import FileService
from app.services.key_service import KeyService
from app.services.log_service import LogService
from app.services.validation_service import ValidationService


def _build_controller(tmp_path: Path) -> EncryptionController:
    """Izveido kontrolieri GUI smoke testam."""

    return EncryptionController(
        crypto_service=CryptoService(),
        file_service=FileService(),
        key_service=KeyService(),
        validation_service=ValidationService(),
        log_service=LogService(log_file_path=str(tmp_path / "gui.log")),
    )


def test_main_window_builds_ui(tmp_path: Path) -> None:
    """Pārbauda, vai galveno logu var izveidot bez kļūdas."""

    try:
        root = tk.Tk()
    except tk.TclError:
        pytest.skip("Tkinter GUI nav pieejams šajā vidē.")

    root.withdraw()
    window = MainWindow(controller=_build_controller(tmp_path), root=root)

    try:
        window.build_ui()
        window.generate_key()

        assert window.file_path_entry is not None
        assert window.key_path_entry is not None
        assert window.encrypt_button is not None
        assert window.decrypt_button is not None
        assert window.current_key is not None
    finally:
        root.destroy()
