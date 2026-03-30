# Testēšanas pārskats

## Testēšanas mērķis

Pārbaudīt, vai lokālā failu šifrēšanas lietotne darbojas atbilstoši projekta mērķim: spēj lokāli šifrēt un atšifrēt failus, korekti apstrādā atslēgas un skaidri paziņo par kļūdām.

## Veiktā automatizētā testēšana

Projektā ir `pytest` testi šādām daļām:

- `CryptoService`
- `KeyService`
- `FileService`
- `ValidationService`
- `EncryptionController`
- `LogService`
- `MainWindow` viegls smoke tests

Pārbaudītie scenāriji:

- šifrēšanas un atšifrēšanas roundtrip
- nederīgas atslēgas noraidīšana
- atslēgas saglabāšana un ielāde
- faila nolasīšana un saglabāšana
- gala failu nosaukumu veidošana
- pieprasījuma validācija
- kontroliera veiksmīgā šifrēšanas un atšifrēšanas plūsma
- kļūda, ja mēģina pārrakstīt gala failu bez atļaujas
- log faila ierakstu izveide
- GUI pamatloga izveide

## Kā palaist testus

1. Atver termināli projekta mapē.
2. Uzinstalē atkarības:
   `python -m pip install -r requirements.txt`
3. Palaid testus:
   `python -m pytest -q`

## Manuālā testēšana ar reāliem failiem

Ieteicams pārbaudīt vismaz šādus failus:

- `.txt`
- `.pdf`
- `.png` vai `.jpg`
- kādu citu nelielu bināru failu

Katram failam pārbaudi:

1. Vai šifrēšana izveido jaunu `.encrypted` failu.
2. Vai atšifrēšana ar pareizu atslēgu izveido `.decrypted` failu ar pareizu saturu.
3. Vai atšifrēšana ar nepareizu atslēgu rāda kļūdu.
4. Vai lietotne neprasa pārrakstīt esošu gala failu bez lietotāja apstiprinājuma.

## Sagaidāmais rezultāts

- Pareiza atslēga ļauj atjaunot sākotnējo saturu.
- Nepareiza atslēga neļauj atšifrēt failu.
- Lietotājs saņem skaidrus paziņojumus GUI pusē.
- Lietotne saglabā OOP dalījumu starp GUI, kontrolieri, servisiem un modeļiem.

## Ierobežojumi

- Pilna GUI automatizētā testēšana nav veikta, jo failu dialogi un lietotāja klikšķi tiek pārbaudīti galvenokārt manuāli.
- Testi neaptver ļoti lielus failus vai ilgstošas veiktspējas pārbaudes.
- Projekts ir veidots kā vienkārša lokāla lietotne, nevis pilnvērtīga failu pārvaldības sistēma.
