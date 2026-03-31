# Failu drosibas lietotne

centāmies panākt vienkāršu Python lietotni failu šifrēšanai un atšifrēšanai. Tā darbojas uz datora bez servera (lokāli) un izmanto Tkinter logu kopā ar `cryptography.Fernet`.

## Ko lietotne dara

- ļauj izvēlēties vienu failu
- ļauj ģenerēt jaunu atslēgu vai ielādēt jau saglabātu atslēgas failu
- šifrē failu un izveido, piemēram, `dokuments.txt.encrypted`
- atšifrē failu un izveido, piemēram, `dokuments.decrypted.txt`
## Ko lietotne nedara

- nestrādā ar vairākiem failiem reizē (!)
- nešifrē mapes (es domāju ka līdz ceturtdienai jeb prezentēšanai nepagūšu uztaisīt)
- neizmanto serveri, datubāzi vai mākoņpakalpojumu
- nav paroles režīma vai lietotāju sistēmas

## Kā palaist lietotni

1. Atvērt šīs repozitorijas mapi terminālī.
2. Uzinstalē vajadzigo:
   `python -m pip install -r requirements.txt`
3. Palaid lietotni:
   `python -m app.main`



## Kā lietot

1. Nospied `Izvēlēties failu` un izvēlies failu.
2. Nospied `Ģenerēt atslēgu` vai `Ielādēt atslēgu`.
3. Ja izveidoji jaunu atslēgu, nospied `Saglabāt atslēgu`.
4. Nospied `Šifrēt` vai `Atšifrēt`.
5. Paskaties statusa tekstu un ziņojuma logu.

## Kā palaist testus -
Automātiskos testus var palaist ar komandu: (ja nemaldos, smeļos no https://docs.pytest.org/en/stable/ un https://www.geeksforgeeks.org/python/pytest-tutorial-testing-python-application-using-pytest/)

`python -m pytest -q`
