"""Galvenā loga skelets."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.controllers.encryption_controller import EncryptionController
    from app.models.encryption_result import EncryptionResult


class MainWindow:
    """Galvenais lietotnes logs failu izvēlei un darbību palaišanai."""

    def __init__(self, controller: EncryptionController) -> None:
        """Inicializē galveno logu un saglabā kontrolieri.

        Args:
            controller: Kontrolieris, kas apstrādā lietotāja darbības.
        """

        self.controller = controller
        self.selected_file_path: str | None = None
        self.key_file_path: str | None = None

    def build_ui(self) -> None:
        """Izveido galvenos saskarnes elementus."""

        raise NotImplementedError("GUI izkārtojums vēl nav izveidots.")

    def bind_events(self) -> None:
        """Piesaista pogām un citiem elementiem notikumus."""

        raise NotImplementedError("GUI notikumu piesaiste vēl nav izveidota.")

    def select_file(self) -> None:
        """Atver faila izvēles darbību un saglabā atlasīto ceļu."""

        raise NotImplementedError("Faila izvēles darbība vēl nav izveidota.")

    def load_key_file(self) -> None:
        """Atver atslēgas faila izvēles darbību."""

        raise NotImplementedError("Atslēgas faila izvēle vēl nav izveidota.")

    def save_key(self) -> None:
        """Saglabā pašreizējo atslēgu lietotāja izvēlētā failā."""

        raise NotImplementedError("Atslēgas saglabāšanas darbība vēl nav izveidota.")

    def generate_key(self) -> None:
        """Izsauc kontrolieri jaunas atslēgas ģenerēšanai."""

        raise NotImplementedError("Atslēgas ģenerēšanas darbība vēl nav izveidota.")

    def encrypt_selected_file(self) -> None:
        """Sagatavo pieprasījumu izvēlētā faila šifrēšanai."""

        raise NotImplementedError("Šifrēšanas darbība vēl nav izveidota.")

    def decrypt_selected_file(self) -> None:
        """Sagatavo pieprasījumu izvēlētā faila atšifrēšanai."""

        raise NotImplementedError("Atšifrēšanas darbība vēl nav izveidota.")

    def show_status(self, message: str, is_error: bool = False) -> None:
        """Parāda statusa ziņojumu lietotājam.

        Args:
            message: Teksts, ko attēlot statusa laukā.
            is_error: Vai ziņojums apraksta kļūdu.
        """

        raise NotImplementedError("Statusa attēlošana vēl nav izveidota.")

    def show_result(self, result: EncryptionResult) -> None:
        """Parāda lietotājam darbības rezultātu.

        Args:
            result: Šifrēšanas vai atšifrēšanas rezultāta objekts.
        """

        raise NotImplementedError("Rezultāta attēlošana vēl nav izveidota.")

    def run(self) -> None:
        """Palaiž galveno lietotnes logu."""

        raise NotImplementedError("Lietotnes palaišana vēl nav izveidota.")
