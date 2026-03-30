# Arhitektūras piezīmes

## Kā projekts atbilst OOP pieejai

Repo ir sadalīts vairākos slāņos, lai katrai daļai būtu sava atbildība. Tas palīdz saglabāt kodu saprotamu un vieglāk testējamu.

## Kur atrodas GUI slānis

GUI slānis ir mapē `app/gui/`.

- `main_window.py` izveido Tkinter logu, pogas, ievades laukus un statusa paziņojumus.
- GUI pats neveic šifrēšanu.

## Kur atrodas controller

Controller atrodas mapē `app/controllers/`.

- `encryption_controller.py` saņem pieprasījumu no GUI.
- Controller pārbauda datus, izsauc servisus un atgriež rezultātu GUI slānim.

## Kur atrodas services

Services atrodas mapē `app/services/`.

- `crypto_service.py` strādā ar šifrēšanu un atšifrēšanu.
- `file_service.py` strādā ar failu nolasīšanu, saglabāšanu un gala failu nosaukumiem.
- `key_service.py` strādā ar atslēgu ģenerēšanu, saglabāšanu un ielādi.
- `validation_service.py` pārbauda ievadi.
- `log_service.py` raksta vienkāršu lokālu log failu.

## Kur atrodas models

Modeļi atrodas mapē `app/models/`.

- `operation_request.py` apraksta lietotāja pieprasījumu.
- `encryption_result.py` apraksta rezultātu.
- pārējie modeļi glabā papildu datus par failiem un konfigurāciju.

## Kā GUI izmanto controller

GUI izveido `OperationRequest` objektu un nodod to controllerim.

- `MainWindow` izsauc `controller.encrypt_file(...)`
- `MainWindow` izsauc `controller.decrypt_file(...)`
- `MainWindow` izsauc `controller.generate_new_key()`
- `MainWindow` izsauc `controller.save_key_to_file(...)`

Tas nozīmē, ka šifrēšanas loģika neatrodas GUI logā. GUI tikai savāc lietotāja ievadi un parāda rezultātu.
