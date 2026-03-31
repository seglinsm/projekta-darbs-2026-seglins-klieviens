# Failu drosibas lietotne

centāmies panākt vienkāršu Python lietotni failu šifrēšanai un atšifrēšanai. Tā darbojas uz datora bez servera un izmanto Tkinter logu kopā ar `cryptography.Fernet`.

## Ko lietotne dara

- ļauj izvēlēties vienu failu
- ļauj ģenerēt jaunu atslēgu vai ielādēt jau saglabātu atslēgas failu
- ļauj saglabāt atslēgu `.key` vai `.txt` failā
- šifrē failu un izveido, piemēram, `dokuments.txt.encrypted`
- atšifrē failu un izveido, piemēram, `dokuments.decrypted.txt`
- pirms pārraksta esošu gala failu, paprasa apstiprinājumu

## Ko lietotne nedara

- nestrādā ar vairākiem failiem reizē
- nešifrē mapes
- neizmanto serveri, datubāzi vai mākoņpakalpojumu
- nav paroles režīma vai lietotāju sistēmas

## Kā palaist lietotni

1. Atver termināli projekta mapē.
2. Uzinstalē vajadzīgās paketes:
   `python -m pip install -r requirements.txt`
3. Palaid lietotni:
   `python -m app.main`

Ja gribi visu pārbaudīt mierīgi, pirms tam sagatavo mazu `.txt`, `.pdf` un `.png` vai `.jpg` failu.

## Kā lietot

1. Nospied `Izvēlēties failu` un izvēlies failu.
2. Nospied `Ģenerēt atslēgu` vai `Ielādēt atslēgu`.
3. Ja izveidoji jaunu atslēgu, nospied `Saglabāt atslēgu`.
4. Nospied `Šifrēt` vai `Atšifrēt`.
5. Paskaties statusa tekstu un ziņojuma logu.

## Kā palaist testus

Automātiskos testus var palaist ar komandu:

`python -m pytest -q`

Pēc pēdējās pārbaudes iziet `20` testi.

## Manuālā pārbaude

Manuālajai pārbaudei skaties failu `manuala_testesana.md`.

## Struktūra īsi

- `app/` - programmas kods
- `tests/` - automātiskie testi
- `info_detalas/` - darba materiāli
