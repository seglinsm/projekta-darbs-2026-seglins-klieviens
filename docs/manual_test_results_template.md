# Manuālo testu rezultātu veidne

## Pamatinformācija

- Testētājs:
- Datums:
- Operētājsistēma:
- Python versija:
- Lietotnes palaišanas komanda: `python -m app.main`

---

## 1. TXT faila tests

### Testējamie soļi

1. Palaist lietotni.
2. Izvēlēties nelielu `.txt` failu.
3. Ģenerēt vai ielādēt atslēgu.
4. Nospiest `Šifrēt`.
5. Pēc tam izvēlēties iegūto `.encrypted` failu.
6. Nospiezt `Atšifrēt`.

### Sagaidāmais rezultāts

- Rodas `fails.txt.encrypted`.
- Rodas `fails.decrypted.txt`.
- Atšifrētā faila saturs sakrīt ar sākotnējo tekstu.

### Faktiskais rezultāts

-

### Secinājums

- Izdodas / Neizdodas:
- Piezīmes:

---

## 2. PDF faila tests

### Testējamie soļi

1. Izvēlēties nelielu `.pdf` failu.
2. Ģenerēt vai ielādēt atslēgu.
3. Nospiest `Šifrēt`.
4. Pēc tam atšifrēt ar to pašu atslēgu.

### Sagaidāmais rezultāts

- Rodas `.pdf.encrypted` fails.
- Rodas `.decrypted.pdf` fails.
- Atšifrētais PDF atveras korekti.

### Faktiskais rezultāts

-

### Secinājums

- Izdodas / Neizdodas:
- Piezīmes:

---

## 3. PNG vai JPG faila tests

### Testējamie soļi

1. Izvēlēties `.png` vai `.jpg` failu.
2. Ģenerēt vai ielādēt atslēgu.
3. Nospiest `Šifrēt`.
4. Pēc tam atšifrēt ar to pašu atslēgu.

### Sagaidāmais rezultāts

- Rodas attēla `.encrypted` fails.
- Rodas `.decrypted.png` vai `.decrypted.jpg` fails.
- Atšifrētais attēls atveras bez bojājumiem.

### Faktiskais rezultāts

-

### Secinājums

- Izdodas / Neizdodas:
- Piezīmes:

---

## 4. Nepareizas atslēgas tests

### Testējamie soļi

1. Sašifrēt failu ar vienu atslēgu.
2. Mēģināt atšifrēt to pašu failu ar citu atslēgu.

### Sagaidāmais rezultāts

- Atšifrēšana neizdodas.
- Lietotne parāda skaidru kļūdas ziņojumu.
- Pareizais sākotnējais saturs netiek atjaunots.

### Faktiskais rezultāts

-

### Secinājums

- Izdodas / Neizdodas:
- Piezīmes:

---

## 5. Pārrakstīšanas gadījums

### Testējamie soļi

1. Veikt šifrēšanu vai atšifrēšanu vienu reizi.
2. Veikt to pašu darbību vēlreiz, lai gala fails jau eksistētu.

### Sagaidāmais rezultāts

- Lietotne parāda jautājumu par pārrakstīšanu.
- Ja pārrakstīšanu neapstiprina, darbība tiek atcelta.
- Ja pārrakstīšanu apstiprina, gala fails tiek pārrakstīts.

### Faktiskais rezultāts

-

### Secinājums

- Izdodas / Neizdodas:
- Piezīmes:

---

## 6. Atslēgas saglabāšana un ielāde pēc lietotnes aizvēršanas

### Testējamie soļi

1. Ģenerēt atslēgu.
2. Saglabāt to failā.
3. Aizvērt lietotni.
4. Atvērt lietotni vēlreiz.
5. Ielādēt iepriekš saglabāto atslēgu.
6. Pārbaudīt, vai ar to var atšifrēt iepriekš šifrētu failu.

### Sagaidāmais rezultāts

- Atslēgas fails tiek veiksmīgi saglabāts.
- Pēc lietotnes atkārtotas palaišanas atslēgu var ielādēt.
- Atšifrēšana ar šo atslēgu izdodas.

### Faktiskais rezultāts

-

### Secinājums

- Izdodas / Neizdodas:
- Piezīmes:
