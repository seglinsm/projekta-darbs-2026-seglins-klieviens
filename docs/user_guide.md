# Lietotāja instrukcija

## Projekta mērķis

Šī ir lokāla Python lietotne failu šifrēšanai un atšifrēšanai. Tā darbojas datorā bez servera un bez datubāzes. Lietotne izmanto `cryptography.Fernet` un vienkāršu Tkinter grafisko interfeisu.

## Kā palaist lietotni

1. Atver termināli projekta mapē.
2. Ja nepieciešams, uzinstalē atkarības:
   `python -m pip install -r requirements.txt`
3. Palaid lietotni:
   `python -m app.main`

## Kā lietot GUI

1. Nospied `Izvēlēties failu` un izvēlies failu, kuru gribi šifrēt vai atšifrēt.
2. Ja vēlies jaunu atslēgu, nospied `Ģenerēt atslēgu`.
3. Ja gribi šo atslēgu saglabāt, nospied `Saglabāt atslēgu`.
4. Ja tev jau ir atslēga failā, nospied `Ielādēt atslēgu`.
5. Nospied `Šifrēt` vai `Atšifrēt`.
6. Izlasi statusa tekstu un ziņojumu logu.

## Kādi faili ir piemēroti testēšanai

- `.txt` faili ar īsu tekstu
- `.pdf` dokumenti
- attēli, piemēram, `.png` un `.jpg`
- citi nelieli faili, kurus gribas pārbaudīt lokāli

Lietotne strādā ar faila baitiem, tāpēc tā nav ierobežota tikai ar teksta failiem.

## Sagaidāmais rezultāts

- Pēc šifrēšanas tiek izveidots jauns fails ar `.encrypted` beigās, piemēram, `dokuments.txt.encrypted`.
- Pēc atšifrēšanas tiek izveidots jauns fails ar `.decrypted` pirms sākotnējā paplašinājuma, piemēram, `dokuments.decrypted.txt`.
- Sākotnējais fails pēc noklusējuma netiek pārrakstīts.
- Ja gala fails jau eksistē, GUI prasa apstiprinājumu par pārrakstīšanu.

## Kas notiek pie nepareizas atslēgas

- Atšifrēšana neizdodas.
- Lietotājs saņem saprotamu kļūdas ziņojumu.
- Pareizais sākotnējais saturs netiek atjaunots.
- Esošais šifrētais fails netiek sabojāts tikai nepareizas atslēgas dēļ.

## Projekta ierobežojumi

- Lietotne apstrādā pa vienam failam.
- Nav paroles režīma vai vairāku lietotāju sistēmas.
- Nav automātiskas mapju šifrēšanas.
- Interfeiss ir apzināti vienkāršs un paredzēts skolas projekta līmenim.
