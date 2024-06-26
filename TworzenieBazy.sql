CREATE DATABASE BusTransport
GO

USE BusTransport
GO

CREATE TABLE Bilety
(
    ID_Biletu INTEGER IDENTITY(0,1) PRIMARY KEY,
	Data_sprzeadazy SMALLDATETIME NOT NULL,
	Kwota INTEGER NOT NULL,
	Rodzaj_biletu INTEGER CHECK (Rodzaj_biletu IN (1,2,3,4,5)) NOT NULL,
	Ulgowy BIT NOT NULL,
)
GO

CREATE TABLE Punkty_trasy
(
	ID_Punktu_trasy INTEGER IDENTITY(0,1) PRIMARY KEY,
	Miasto VARCHAR(50) NOT NULL,
	Ulica VARCHAR(255) NOT NULL,
	Adres VARCHAR(25) NOT NULL,
)
GO

CREATE TABLE Autobusy
(
	ID_Autobusu INTEGER IDENTITY(0,1) PRIMARY KEY,
	Data_zakupu SMALLDATETIME NOT NULL,
	Ilosc_miesc SMALLINT NOT NULL,
	Numer_rejestracyjny VARCHAR(255) NOT NULL,
)
GO

CREATE TABLE Kierowcy
(
	ID_Kierowcy INTEGER IDENTITY(0,1) PRIMARY KEY,
	Imie VARCHAR(63) NOT NULL,
	Nazwisko VARCHAR(63) NOT NULL,
	Nr_prawa_jazdy VARCHAR(14) NOT NULL,
	Nr_dowodu VARCHAR(14) NOT NULL,
	Data_zatrudnienia SMALLDATETIME NOT NULL,
	Miasto VARCHAR(63) NOT NULL,
	Zarobki INTEGER NOT NULL,
)
GO

CREATE TABLE Kursy
(
	ID_kursu INTEGER IDENTITY(0,1) PRIMARY KEY,
	Data_rozpoczecia_kursu SMALLDATETIME NOT NULL,
	Data_zakonczenia_kursu SMALLDATETIME NOT NULL,
	Planowana_data_rozpoczecia_kursu SMALLDATETIME NOT NULL,
	Planowana_data_zakonczenia_kursu SMALLDATETIME NOT NULL,
	Dlugosc_trasy INTEGER NOT NULL,
	ID_Autobusu INTEGER NOT NULL FOREIGN KEY REFERENCES Autobusy,
	ID_Kierowcy INTEGER NOT NULL FOREIGN KEY REFERENCES Kierowcy,
	ID_Punktu_trasy_poczatkowy INTEGER NOT NULL FOREIGN KEY REFERENCES Punkty_trasy,
	ID_Punktu_trasy_koncowy INTEGER NOT NULL FOREIGN KEY REFERENCES Punkty_trasy,
)

CREATE TABLE Skasowanie
(
	ID_kursu INTEGER FOREIGN KEY REFERENCES Kursy  NOT NULL,
	ID_Biletu INTEGER FOREIGN KEY REFERENCES Bilety  NOT NULL,
	Data_skasowania TIME NOT NULL,
	PRIMARY KEY (ID_kursu, ID_Biletu)
)
GO