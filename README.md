# Failu drošības nodrošināšana ar lokālu Python lietotni

## Projekta mērķis

Šī projekta mērķis ir izveidot vienkāršu lokālu Python lietotni, kas ļauj izvēlēties failu, to šifrēt vai atšifrēt un droši strādāt ar atslēgu. Lietotne ir paredzēta skolas projekta līmenim un darbojas bez servera, bez datubāzes un bez tīmekļa daļas.

## Izmantotās tehnoloģijas

- Python 3.11+
- Tkinter grafiskais interfeiss
- `cryptography.Fernet` failu šifrēšanai
- `pytest` testiem

## Projekta struktūra

- `app/gui/` satur Tkinter logu un lietotāja darbības.
- `app/controllers/` satur kontrolieri, kas savieno GUI ar servisiem.
- `app/services/` satur failu, atslēgu, validācijas, logēšanas un šifrēšanas loģiku.
- `app/models/` satur vienkāršus datu modeļus.
- `app/utils/` satur pielāgotos izņēmumus.
- `tests/` satur automatizētos testus.
- `docs/` satur lietotāja instrukciju, testēšanas pārskatu un arhitektūras piezīmes.

## Kā palaist lietotni

1. Atver termināli projekta mapē.
2. Uzinstalē atkarības:
   `python -m pip install -r requirements.txt`
3. Palaid lietotni:
   `python -m app.main`

## Kā palaist testus

Palaid testus ar komandu:

`python -m pytest -q`

## Ko vēl jāpārbauda manuāli

Pirms gala iesniegšanas vēl vajag pārbaudīt lietotni ar reāliem failiem:

- `.txt`
- `.pdf`
- `.png` vai `.jpg`
- nepareiza atslēga
- pārrakstīšanas gadījums
- atslēgas saglabāšana un ielāde pēc lietotnes aizvēršanas

Rezultātus var aizpildīt failā `docs/manual_test_results_template.md`.

## Ko lietotne dara

- ļauj izvēlēties vienu failu no datora;
- ģenerē vai ielādē šifrēšanas atslēgu;
- šifrē failu jaunā failā;
- atšifrē failu jaunā failā;
- rāda statusa ziņojumus un kļūdas GUI logā;
- nepārraksta gala failu bez lietotāja apstiprinājuma.

## Ko lietotne nedara

- neizmanto datubāzi;
- nesūta failus uz serveri;
- neveido lietotāju kontus;
- nešifrē vairākus failus vienlaikus;
- nepiedāvā sarežģītu failu pārvaldības sistēmu vai “cloud” funkcijas.
