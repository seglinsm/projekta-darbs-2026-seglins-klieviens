# Manuālās pārbaudes saraksts

## Kā palaist lietotni

1. Atver termināli projekta mapē.
2. Ja vajag, uzinstalē atkarības:
   `python -m pip install -r requirements.txt`
3. Palaid lietotni:
   `python -m app.main`

## Ko pārbaudīt manuāli

1. Atver lietotni un pārliecinies, ka logs parādās bez kļūdas.
2. Nospied `Izvēlēties failu` un izvēlies pārbaudes failu.
3. Nospied `Ģenerēt atslēgu`.
4. Nospied `Saglabāt atslēgu` un saglabā to `.key` vai `.txt` failā.
5. Nospied `Šifrēt`.
6. Pārbaudi, ka tiek izveidots jauns fails, kuram sākotnējais nosaukums tiek saglabāts un beigās tiek pievienots `.encrypted`.
7. Nospied `Ielādēt atslēgu` un izvēlies iepriekš saglabāto atslēgas failu.
8. Nospied `Atšifrēt`.
9. Pārbaudi, ka tiek izveidots jauns fails ar `.decrypted` marķieri pirms sākotnējā faila paplašinājuma, piemēram, `attels.decrypted.jpg`.

## Kādus failus pārbaudīt

- Mazs `.txt` fails ar vienkāršu tekstu.
- Neliels `.pdf` fails.
- Neliels attēls, piemēram, `.png` vai `.jpg`.
- Neliels binārs fails, lai pārbaudītu, ka lietotne strādā arī ne tikai ar tekstu.

## Ko sagaidīt pie nepareizas atslēgas

- Atšifrēšana nedrīkst izdoties.
- Lietotnei jāparāda saprotams kļūdas paziņojums.
- Nevajadzētu iegūt korektu sākotnējo saturu.
- Esošais šifrētais fails nedrīkst tikt bojāts tikai tāpēc, ka tika izmantota nepareiza atslēga.
- Ja gala fails jau eksistē, lietotnei jāprasa apstiprinājums par pārrakstīšanu.
