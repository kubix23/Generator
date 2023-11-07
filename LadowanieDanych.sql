DECLARE @Path AS VARCHAR(100)='C:\Users\kubix23\PycharmProjects\Generator\'

use BusTransport

EXEC('BULK INSERT dbo.Bilety FROM '''+@Path+'bilety0.bulk'' WITH (FIELDTERMINATOR='','')')
EXEC('BULK INSERT dbo.Punkty_trasy FROM '''+@Path+'punktyTrasy0.bulk'' WITH (FIELDTERMINATOR='','')')
EXEC('BULK INSERT dbo.Autobusy FROM '''+@Path+'autobusy0.bulk'' WITH (FIELDTERMINATOR='','')')
EXEC('BULK INSERT dbo.Kierowcy FROM '''+@Path+'kierowcy0.bulk'' WITH (FIELDTERMINATOR='','')')
EXEC('BULK INSERT dbo.Kursy FROM '''+@Path+'kursy0.bulk'' WITH (FIELDTERMINATOR='','')')
EXEC('BULK INSERT dbo.Skasowanie FROM '''+@Path+'skasowanie0.bulk'' WITH (FIELDTERMINATOR='','')')