"""Vienkāršs Tkinter galvenais logs failu šifrēšanas lietotnei."""

from __future__ import annotations

from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.controllers.encryption_controller import EncryptionController
    from app.models.encryption_result import EncryptionResult

from app.models.operation_request import OperationRequest


class MainWindow:
    """Galvenais lietotnes logs failu izvēlei un darbību palaišanai."""

    def __init__(
        self,
        controller: EncryptionController,
        root: tk.Tk | None = None,
    ) -> None:
        """Inicializē galveno logu un saglabā kontrolieri.

        Args:
            controller: Kontrolieris, kas apstrādā lietotāja darbības.
            root: Esošs Tk logs testiem vai pielāgotai palaišanai.
        """

        self.controller = controller
        self.root = root
        self.selected_file_path: str | None = None
        self.key_file_path: str | None = None
        self.current_key: bytes | None = None

        self.file_path_var: tk.StringVar | None = None
        self.key_path_var: tk.StringVar | None = None
        self.status_var: tk.StringVar | None = None

        self.file_path_entry: ttk.Entry | None = None
        self.key_path_entry: ttk.Entry | None = None
        self.status_label: tk.Label | None = None
        self.select_file_button: ttk.Button | None = None
        self.load_key_button: ttk.Button | None = None
        self.generate_key_button: ttk.Button | None = None
        self.save_key_button: ttk.Button | None = None
        self.encrypt_button: ttk.Button | None = None
        self.decrypt_button: ttk.Button | None = None
        self._ui_built = False

    def build_ui(self) -> None:
        """Izveido galvenos saskarnes elementus."""

        if self._ui_built:
            return

        if self.root is None:
            self.root = tk.Tk()

        self.root.title("Failu drošības lietotne")
        self.root.minsize(620, 300)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        main_frame = ttk.Frame(self.root, padding=16)
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.columnconfigure(1, weight=1)

        self.file_path_var = tk.StringVar(master=self.root, value="")
        self.key_path_var = tk.StringVar(master=self.root, value="")
        self.status_var = tk.StringVar(master=self.root, value="Lietotne gatava darbam.")

        title_label = ttk.Label(
            main_frame,
            text="Lokāla failu šifrēšana",
        )
        title_label.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 12))

        ttk.Label(main_frame, text="Fails:").grid(row=1, column=0, sticky="w", pady=4)
        self.file_path_entry = ttk.Entry(
            main_frame,
            textvariable=self.file_path_var,
            width=60,
        )
        self.file_path_entry.grid(row=1, column=1, sticky="ew", padx=(8, 8), pady=4)
        self.select_file_button = ttk.Button(main_frame, text="Izvēlēties failu")
        self.select_file_button.grid(row=1, column=2, sticky="ew", pady=4)

        ttk.Label(main_frame, text="Atslēgas fails:").grid(
            row=2,
            column=0,
            sticky="w",
            pady=4,
        )
        self.key_path_entry = ttk.Entry(
            main_frame,
            textvariable=self.key_path_var,
            width=60,
        )
        self.key_path_entry.grid(row=2, column=1, sticky="ew", padx=(8, 8), pady=4)
        self.load_key_button = ttk.Button(main_frame, text="Ielādēt atslēgu")
        self.load_key_button.grid(row=2, column=2, sticky="ew", pady=4)

        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=3, column=0, columnspan=3, sticky="ew", pady=(16, 12))
        for index in range(4):
            buttons_frame.columnconfigure(index, weight=1)

        self.generate_key_button = ttk.Button(buttons_frame, text="Ģenerēt atslēgu")
        self.generate_key_button.grid(row=0, column=0, sticky="ew", padx=(0, 8))

        self.save_key_button = ttk.Button(buttons_frame, text="Saglabāt atslēgu")
        self.save_key_button.grid(row=0, column=1, sticky="ew", padx=(0, 8))

        self.encrypt_button = ttk.Button(buttons_frame, text="Šifrēt")
        self.encrypt_button.grid(row=0, column=2, sticky="ew", padx=(0, 8))

        self.decrypt_button = ttk.Button(buttons_frame, text="Atšifrēt")
        self.decrypt_button.grid(row=0, column=3, sticky="ew")

        ttk.Label(main_frame, text="Statuss:").grid(row=4, column=0, sticky="nw", pady=4)
        self.status_label = tk.Label(
            main_frame,
            textvariable=self.status_var,
            anchor="w",
            justify="left",
            wraplength=560,
            fg="darkgreen",
        )
        self.status_label.grid(row=4, column=1, columnspan=2, sticky="ew", pady=4)

        self.bind_events()
        self._ui_built = True

    def bind_events(self) -> None:
        """Piesaista pogām un citiem elementiem notikumus."""

        if (
            self.select_file_button is None
            or self.load_key_button is None
            or self.generate_key_button is None
            or self.save_key_button is None
            or self.encrypt_button is None
            or self.decrypt_button is None
        ):
            return

        self.select_file_button.configure(command=self.select_file)
        self.load_key_button.configure(command=self.load_key_file)
        self.generate_key_button.configure(command=self.generate_key)
        self.save_key_button.configure(command=self.save_key)
        self.encrypt_button.configure(command=self.encrypt_selected_file)
        self.decrypt_button.configure(command=self.decrypt_selected_file)

    def select_file(self) -> None:
        """Atver faila izvēles darbību un saglabā atlasīto ceļu."""

        selected_path = filedialog.askopenfilename(title="Izvēlies failu")
        if not selected_path:
            self.show_status("Faila izvēle atcelta.")
            return

        self.selected_file_path = selected_path
        if self.file_path_var is not None:
            self.file_path_var.set(selected_path)
        self.show_status(f"Izvēlēts fails: {Path(selected_path).name}")

    def load_key_file(self) -> None:
        """Atver atslēgas faila izvēles darbību."""

        selected_path = filedialog.askopenfilename(
            title="Izvēlies atslēgas failu",
            filetypes=[
                ("Atslēgas faili", "*.key *.txt"),
                ("Visi faili", "*.*"),
            ],
        )
        if not selected_path:
            self.show_status("Atslēgas faila izvēle atcelta.")
            return

        try:
            loaded_key = self.controller.load_key_from_file(selected_path)
        except Exception as exc:
            self.show_status(str(exc), is_error=True)
            messagebox.showerror("Atslēgas kļūda", str(exc))
            return

        self.key_file_path = selected_path
        self.current_key = loaded_key
        if self.key_path_var is not None:
            self.key_path_var.set(selected_path)
        self.show_status("Atslēga ielādēta no faila.")

    def save_key(self) -> None:
        """Saglabā pašreizējo atslēgu lietotāja izvēlētā failā."""

        if self.current_key is None:
            self.show_status("Nav atslēgas, ko saglabāt.", is_error=True)
            messagebox.showwarning("Nav atslēgas", "Vispirms ģenerē vai ielādē atslēgu.")
            return

        save_path = filedialog.asksaveasfilename(
            title="Saglabāt atslēgu",
            defaultextension=".key",
            filetypes=[
                ("Atslēgas faili", "*.key"),
                ("Teksta faili", "*.txt"),
                ("Visi faili", "*.*"),
            ],
        )
        if not save_path:
            self.show_status("Atslēgas saglabāšana atcelta.")
            return

        try:
            saved_path = self.controller.save_key_to_file(self.current_key, save_path)
        except Exception as exc:
            self.show_status(str(exc), is_error=True)
            messagebox.showerror("Saglabāšanas kļūda", str(exc))
            return

        self.key_file_path = str(saved_path)
        if self.key_path_var is not None:
            self.key_path_var.set(str(saved_path))
        self.show_status("Atslēga saglabāta veiksmīgi.")
        messagebox.showinfo("Atslēga saglabāta", f"Atslēga saglabāta failā:\n{saved_path}")

    def generate_key(self) -> None:
        """Izsauc kontrolieri jaunas atslēgas ģenerēšanai."""

        try:
            self.current_key = self.controller.generate_new_key()
        except Exception as exc:
            self.show_status(str(exc), is_error=True)
            messagebox.showerror("Atslēgas kļūda", str(exc))
            return

        self.key_file_path = None
        if self.key_path_var is not None:
            self.key_path_var.set("")
        self.show_status("Jauna atslēga ģenerēta. Ieteicams to saglabāt failā.")

    def encrypt_selected_file(self) -> None:
        """Sagatavo pieprasījumu izvēlētā faila šifrēšanai."""

        request = self._build_request(operation="encrypt")
        if request is None:
            return
        result = self.controller.encrypt_file(request)
        self.show_result(result)

    def decrypt_selected_file(self) -> None:
        """Sagatavo pieprasījumu izvēlētā faila atšifrēšanai."""

        request = self._build_request(operation="decrypt")
        if request is None:
            return
        result = self.controller.decrypt_file(request)
        self.show_result(result)

    def show_status(self, message: str, is_error: bool = False) -> None:
        """Parāda statusa ziņojumu lietotājam.

        Args:
            message: Teksts, ko attēlot statusa laukā.
            is_error: Vai ziņojums apraksta kļūdu.
        """

        if self.status_var is not None:
            self.status_var.set(message)
        if self.status_label is not None:
            self.status_label.configure(fg="firebrick" if is_error else "darkgreen")

    def show_result(self, result: EncryptionResult) -> None:
        """Parāda lietotājam darbības rezultātu.

        Args:
            result: Šifrēšanas vai atšifrēšanas rezultāta objekts.
        """

        self.show_status(result.message, is_error=not result.success)

        message_lines = [result.message]
        if result.output_path:
            message_lines.append(f"Gala fails:\n{result.output_path}")

        message_text = "\n\n".join(message_lines)
        if result.success:
            messagebox.showinfo("Darbība pabeigta", message_text)
        else:
            messagebox.showerror("Darbība neizdevās", message_text)

    def run(self) -> None:
        """Palaiž galveno lietotnes logu."""

        self.build_ui()
        if self.root is not None:
            self.root.mainloop()

    def _build_request(self, operation: str) -> OperationRequest | None:
        """Izveido pieprasījuma objektu no pašreizējās GUI ievades."""

        self.selected_file_path = self._get_file_path_from_entry()
        key, key_file_path = self._get_key_data_for_request()

        if not self.selected_file_path:
            self.show_status("Vispirms izvēlies failu.", is_error=True)
            messagebox.showwarning("Nav izvēlēts fails", "Vispirms izvēlies failu.")
            return None

        if key is None and not key_file_path:
            self.show_status("Vispirms ģenerē vai ielādē atslēgu.", is_error=True)
            messagebox.showwarning(
                "Nav atslēgas",
                "Vispirms ģenerē vai ielādē atslēgu.",
            )
            return None

        output_path = None
        overwrite_existing = False

        output_path = self.controller.build_output_path(self.selected_file_path, operation)
        if Path(output_path).exists():
            should_overwrite = messagebox.askyesno(
                "Fails jau eksistē",
                (
                    "Gala fails jau eksistē:\n"
                    f"{output_path}\n\n"
                    "Vai vēlies to pārrakstīt?"
                ),
            )
            if not should_overwrite:
                self.show_status(
                    "Darbība atcelta, jo gala fails jau eksistē.",
                    is_error=True,
                )
                return None

            overwrite_existing = True
            self.show_status("Esošais gala fails tiks pārrakstīts.")

        return OperationRequest(
            source_file_path=self.selected_file_path or "",
            operation=operation,
            key=key,
            key_file_path=key_file_path,
            output_file_path=output_path,
            overwrite_existing=overwrite_existing,
        )

    def _get_file_path_from_entry(self) -> str | None:
        """Atgriež pašreizējo faila ceļu no ievades lauka."""

        if self.file_path_var is None:
            return self.selected_file_path

        file_path = self.file_path_var.get().strip()
        return file_path or None

    def _get_key_data_for_request(self) -> tuple[bytes | None, str | None]:
        """Atgriež atslēgu vai atslēgas faila ceļu pieprasījuma izveidei."""

        entered_key_path = None
        if self.key_path_var is not None:
            entered_key_path = self.key_path_var.get().strip() or None

        if entered_key_path != self.key_file_path:
            self.key_file_path = entered_key_path
            self.current_key = None

        if self.current_key is not None:
            return self.current_key, None

        return None, self.key_file_path
