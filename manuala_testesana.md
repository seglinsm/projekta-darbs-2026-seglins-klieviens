# Manuala testeesana

## Pirms sāc

Sagatavo dažus mazus failus:

- vienu `.txt` failu
- vienu `.pdf` failu
- vienu `.png` vai `.jpg` failu

Lietotni palaid ar:

`python -m app.main`

Ja gribi pārlaist automātiskos testus:

`python -m pytest -q`

## Pamata gaita

1. Atver lietotni.
2. Izvēlies failu ar pogu `Izvēlēties failu`.
3. Ģenerē jaunu atslēgu vai ielādē jau saglabātu.
4. Ja izveidoji jaunu atslēgu, saglabā to failā.
5. Nospied `Šifrēt`.
6. Pēc tam atver iegūto `.encrypted` failu un nospied `Atšifrēt`.

Parasti vajadzētu notikt šādi:

- pēc šifrēšanas rodas fails ar `.encrypted` beigās
- pēc atšifrēšanas rodas fails ar `.decrypted` pirms sākotnējā paplašinājuma
- ja gala fails jau eksistē, lietotne prasa apstiprinājumu
- ja atslēga ir nepareiza, atšifrēšana neizdodas un parādās kļūdas ziņojums

---

## 1. TXT fails

Soļi:

1. Izvēlies mazu `.txt` failu.
2. Ģenerē vai ielādē atslēgu.
3. Nospied `Šifrēt`.
4. Pēc tam atšifrē ar to pašu atslēgu.

Sagaidāmais rezultāts:

- rodas `fails.txt.encrypted`
- rodas `fails.decrypted.txt`
- saturs sakrīt ar oriģinālu

Faktiskais rezultāts:

-

Secinājums:

- Izdodas / Neizdodas:
- Piezīmes:

---

## 2. PDF fails

Soļi:

1. Izvēlies mazu `.pdf` failu.
2. Ģenerē vai ielādē atslēgu.
3. Nospied `Šifrēt`.
4. Atšifrē ar to pašu atslēgu.

Sagaidāmais rezultāts:

- rodas `.pdf.encrypted` fails
- rodas `.decrypted.pdf` fails
- atjaunotais PDF atveras korekti

Faktiskais rezultāts:

-

Secinājums:

- Izdodas / Neizdodas:
- Piezīmes:

---

## 3. PNG vai JPG fails

Soļi:

1. Izvēlies `.png` vai `.jpg` failu.
2. Ģenerē vai ielādē atslēgu.
3. Nospied `Šifrēt`.
4. Atšifrē ar to pašu atslēgu.

Sagaidāmais rezultāts:

- rodas attēla `.encrypted` fails
- rodas `.decrypted.png` vai `.decrypted.jpg` fails
- atjaunotais attēls atveras bez bojājumiem

Faktiskais rezultāts:

-

Secinājums:

- Izdodas / Neizdodas:
- Piezīmes:

---

## 4. Nepareiza atslēga

Soļi:

1. Sašifrē failu ar vienu atslēgu.
2. Mēģini to atšifrēt ar citu atslēgu.

Sagaidāmais rezultāts:

- atšifrēšana neizdodas
- lietotne parāda skaidru kļūdas ziņojumu
- pareizais saturs netiek atjaunots

Faktiskais rezultāts:

-

Secinājums:

- Izdodas / Neizdodas:
- Piezīmes:

---

## 5. Parrakstisanas gadijums

Soļi:

1. Veic šifrēšanu vai atšifrēšanu vienu reizi.
2. Veic to pašu darbību vēlreiz, lai gala fails jau eksistētu.

Sagaidāmais rezultāts:

- lietotne uzdod jautājumu par pārrakstīšanu
- ja neapstiprina, darbība apstājas
- ja apstiprina, gala fails tiek pārrakstīts

Faktiskais rezultāts:

-

Secinājums:

- Izdodas / Neizdodas:
- Piezīmes:

---

## 6. Atslegas saglabasana un ielade pec aizversanas

Soļi:

1. Ģenerē atslēgu.
2. Saglabā to failā.
3. Aizver lietotni.
4. Atver lietotni vēlreiz.
5. Ielādē iepriekš saglabāto atslēgu.
6. Pamēģini atšifrēt iepriekš šifrētu failu.

Sagaidāmais rezultāts:

- atslēgas fails saglabājas korekti
- pēc lietotnes atvēršanas atslēgu var ielādēt
- atšifrēšana ar to pašu atslēgu izdodas

Faktiskais rezultāts:

-

Secinājums:

- Izdodas / Neizdodas:
- Piezīmes:
