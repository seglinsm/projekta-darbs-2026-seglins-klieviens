# Testēšanas pārskats

## Testēšanas mērķis

Pārbaudīt, vai lokālā failu šifrēšanas lietotne darbojas atbilstoši projekta mērķim: spēj lokāli šifrēt un atšifrēt failus, pareizi apstrādā atslēgas, neiznīcina sākotnējos failus bez apstiprinājuma un rāda saprotamus ziņojumus lietotājam.

## Automatizētā testēšana

Pēdējā lokālā automatizētā pārbaude:

- komanda: `python -m pytest -q`
- rezultāts: `20 passed`

Ar testiem tiek pārbaudīts:

- `CryptoService`
- `KeyService`
- `FileService`
- `ValidationService`
- `EncryptionController`
- `LogService`
- `MainWindow` viegls smoke tests

Automatizētie scenāriji:

- šifrēšanas un atšifrēšanas roundtrip
- nederīgas atslēgas noraidīšana
- atslēgas saglabāšana un ielāde
- faila nolasīšana un saglabāšana
- gala failu nosaukumu veidošana
- pieprasījuma validācija
- kontroliera veiksmīga šifrēšana un atšifrēšana
- kļūda, ja mēģina pārrakstīt gala failu bez atļaujas
- log faila ieraksta izveide
- GUI pamatloga izveide

## Kā palaist testus

1. Atver termināli projekta mapē.
2. Ja vajag, uzinstalē atkarības:
   `python -m pip install -r requirements.txt`
3. Palaid testus:
   `python -m pytest -q`

## Secinājums

Automatizētie testi rāda, ka kodola loģika un pamatplūsmas strādā. Lai projektu varētu godīgi iesniegt kā pabeigtu gala darbu, vēl ir jāiziet manuālā pārbaude ar īstiem `.txt`, `.pdf` un attēlu failiem.

## Ierobežojumi

- Pilna GUI automatizētā testēšana nav veikta, jo failu dialogi un lietotāja klikšķi galvenokārt tiek pārbaudīti manuāli.
- Testi neaptver ļoti lielus failus un veiktspējas robežgadījumus.
- Projekts ir apzināti vienkārša lokāla lietotne, nevis pilnvērtīga failu pārvaldības sistēma.
