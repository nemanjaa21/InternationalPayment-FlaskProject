DROP DATABASE IF EXISTS DRS_PROJEKAT;

CREATE DATABASE DRS_PROJEKAT;

use DRS_PROJEKAT;

CREATE TABLE Kartica(
   BrojKartice BIGINT NOT NULL,
   ImeKorisnika VARCHAR(50) NOT NULL,
   DatumIsteka date,
   NovcanoStanje FLOAT NOT NULL,
   SigurnosniKod INTEGER NOT NULL,
   CONSTRAINT kartica_PK PRIMARY KEY (BrojKartice)

);

INSERT INTO Kartica(BrojKartice,ImeKorisnika,DatumIsteka,NovcanoStanje,SigurnosniKod) 
VALUES(4242424242424242,"Pera",'2023-02-01',5,123);

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
    NovcanoStanje FLOAT NOT NULL,
    Verifikovan TINYINT NOT NULL,
    Valuta VARCHAR(3) NOT NULL,
    CONSTRAINT korisnik_PK PRIMARY KEY (Email),
    CONSTRAINT korisnik_FK FOREIGN KEY (BrojKartice) REFERENCES DRS_PROJEKAT.Kartica(BrojKartice)

);

INSERT INTO Korisnik(Ime,Prezime,Adresa,Grad,Drzava,BrojTelefona,Email,Lozinka,BrojKartice,NovcanoStanje,Verifikovan,Valuta)
VALUES("Pera","Peric","Bulevar Evrope 98","Novi Sad","Srbija",0601112223,"pera@gmail.com","lozinka1",4242424242424242,0,0,"RSD");


CREATE TABLE Transakcija(
       IdTransakcije INTEGER NOT NULL AUTO_INCREMENT,
       BrojKarticeKorisnika BIGINT NOT NULL,
       Stanje VARCHAR(50) NOT NULL,
       CONSTRAINT transakcija_PK PRIMARY KEY (IdTransakcije),
       CONSTRAINT transakcija_FK FOREIGN KEY (BrojKarticeKorisnika) REFERENCES DRS_PROJEKAT.Korisnik (BrojKartice)
       
);