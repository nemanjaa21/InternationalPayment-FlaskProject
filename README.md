# DRS-Projekat

Implementirati projekat koji simulira medjunarodni platni promet i on-line racun za licne uplate.

Implementacija treba da sadrzi 3 komponente:

1. Korisnicki interfejs (UI)
2. Servis za obradu zahteva i podataka (Engine)
3. Bazu podataka (DB)

# Korisnicki interfejs (UI)

Korisnicki interfejs je Flask web aplikacija koja treba da opsluzi korisnika u interakciji sa 
platnim prometom.

1. Registracija novog korisnika
2. Logovanje postojeceg korisnika
3. Izmena korisnickog profila
4. Pregled stanja
5. Ubacivanje sredstava putem platne kartice na on-line racun
6. Pregled istorije transakcija sa mogucnoscu sortiranja i filtriranja
7. Iniciranje nove transakcije drugom korisniku
   a. Koji ima otvoren on-line racun
   b. Na racun u banci
8. Izbor valute – sa osvezavanjem kursne liste sa interneta
9. Zamena valute

Korisnik se registruje unoseci:
1. Ime
2. Prezime
3. Adresa
4. Grad
5. Drzava
6. Broj telefona
7. Email
8. Lozinka

Korisnike se loguje putem:
  -Email
  -Lozinka

Novi korisnik ima stanje 0. On tada treba da zatrazi verifikaciju naloga. Za verifikaciju je
potrebno da unese svoju platnu karticu i bice mu skinuto 1$. Nakon toga korisnik moze da
uplati sredstva sa kartice na svoj on-line racun.

Test platna kartica:

  Broj: 4242 4242 4242 4242 
  Ime: <Ime Korisnika>
  Datum isteka kartice: 02/23
  Sigurnosni kod: 123

Korisnik inicira transakciju drugom korisniku unoseci podatke o racunu korisnika u banci ili
njegovoj email adresi ukoliko drugi korisnik ima registrovan nalog.

Kad se inicira transakcija, ona treba da se obradi na strain Engine-a. Transakcija ima stanja:
1. U obradi
2. Obradjeno
3. Odbijeno

Potrebno vreme da se transakcija odobri je 2min. Za to vreme sistem mora da bude sposoban da
odgovori na ostale zahteve. Konverzija valute se vrsi po principu da korisnik uplacuje sa 
kartice sa on-line racun u Dinarima. Kursna lista se dovlaci sa eksternog API-a kursne liste.
Nakon dobijanja liste, korisnik bira valutu i iznos. Nakon uspesne konverzije korisnik ima 
novo stanje u novoj valuti. Korisnik moze da ima neogranicen broj valuta i stanja racuna u valutama.

# Servis za obradu zahteva i podataka (Engine)

Engine je servis implementiran kao flask API aplikacija. Engine ima svoje endpointe koje
prikazuje eksternom svetu (UI aplikaciji) za koriscenje. UI deo poziva endpointe Engine-a radi
obrade raznih zahteva i podataka. Pri tome samo Engine komunicira sa bazom, a UI sa Engine-om.

# Baza podataka (DB)

Baza podataka je u komunikaciji sa Engine-om za svrhu skladistenja podataka o aplikaciji. 
U bazi se skladiste svi esencijalno bitni podaci za rad aplikacije. Model baze kao i tip
baze (NoSQL, SQL) je proizvoljan.