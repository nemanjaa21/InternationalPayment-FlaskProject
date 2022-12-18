CREATE DATABASE DRS_PROJEKAT;

use DRS_PROJEKAT;

CREATE TABLE Kartica(
   BrojKartice BIGINT NOT NULL,
   ImeKorisnika VARCHAR(50) NOT NULL,
   DatumIsteka date,
   SigurnosniKod INTEGER NOT NULL,
   CONSTRAINT kartica_PK PRIMARY KEY (BrojKartice)

);

INSERT INTO Kartica(BrojKartice,ImeKorisnika,DatumIsteka,SigurnosniKod) 
VALUES(4242424242424242,"Pera",'2023-02-01',123);
INSERT INTO Kartica(BrojKartice,ImeKorisnika,DatumIsteka,SigurnosniKod) 
VALUES(4552455245524552,"Nikola",'2023-05-01',456);
INSERT INTO Kartica(BrojKartice,ImeKorisnika,DatumIsteka,SigurnosniKod) 
VALUES(5555666677778888,"Mark",'2024-07-01',987);

CREATE TABLE Korisnik(
    Ime VARCHAR(50) NOT NULL,
    Prezime VARCHAR(50) NOT NULL,
    Adresa VARCHAR(50) NOT NULL,
    Grad VARCHAR(50) NOT NULL,
    Drzava VARCHAR(50) NOT NULL,
    BrojTelefona BIGINT NOT NULL,
    Email VARCHAR(50) NOT NULL, 
    Lozinka VARCHAR(50) NOT NULL,
    BrojKartice BIGINT NOT NULL,
    CONSTRAINT korisnik_PK PRIMARY KEY (Ime),
    CONSTRAINT korisnik_FK FOREIGN KEY (BrojKartice) REFERENCES DRS_PROJEKAT.Kartica(BrojKartice)

);

INSERT INTO Korisnik(Ime,Prezime,Adresa,Grad,Drzava,BrojTelefona,Email,Lozinka,BrojKartice)
VALUES("Pera","Peric","Bulevar Evrope 98","Novi Sad","Srbija",0601112223,"pera@gmail.com","lozinka1",4242424242424242);
INSERT INTO Korisnik(Ime,Prezime,Adresa,Grad,Drzava,BrojTelefona,Email,Lozinka,BrojKartice)
VALUES("Nikola","Nikolic","Jovana Ducica 20","Beograd","Srbija",0604442223,"nikola@yahoo.com","lozinka2",4552455245524552);
INSERT INTO Korisnik(Ime,Prezime,Adresa,Grad,Drzava,BrojTelefona,Email,Lozinka,BrojKartice)
VALUES("Mark","Peterson","Times Square","New York","SAD",4456767563,"mark@gmail.com","password1",5555666677778888);


CREATE TABLE Transakcija(
       IdTransakcije INTEGER NOT NULL AUTO_INCREMENT,
       BrojKarticeKorisnika BIGINT NOT NULL,
       Stanje VARCHAR(50) NOT NULL,
       CONSTRAINT transakcija_PK PRIMARY KEY (IdTransakcije),
       CONSTRAINT transakcija_FK FOREIGN KEY (BrojKarticeKorisnika) REFERENCES DRS_PROJEKAT.Korisnik (BrojKartice)
       
);
