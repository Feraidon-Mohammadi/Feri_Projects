/*************************************************************************
				Arbeiten mit Transaktionen

				Für Transaktionen gilt das ACID-Prinzip

				A-------Atomarität
				C-------Consistenz
				I-------Isolation
				D-------Dauerhaftigkeit

	Die nachfolgenden Beispiele sind für fiktive Tabellen geschrieben
	und daher nicht ausführbar
**************************************************************************/


												--ANSI-SQL(Standard)
update personal
set gehalt=gehalt*1.04

commit;


update giro
set kontostand=kontostand-betrag
where kontonr=meine_kontonr

update barauszahlung
set kontostand=kontostand+betrag
where kontonr=meine_kontonr

commit; 


												--Transact-SQL(Microsoft SQL Server)

								--automatisch commitete Transaktion
update personal
set gehalt=gehalt*1.04;---------AUTOcommit;



								--explizite Transaktion
begin transaction

update giro
set kontostand=kontostand-betrag
where kontonr=meine_kontonr

update barauszahlung
set kontostand=kontostand+betrag
where kontonr=meine_kontonr

commit transaction; 


exec sp_lock;

go
update giro
set kontostand=kontostand-betrag
where kontonr=meine_kontonr

update barauszahlung
set kontostand=kontostand+betrag
where kontonr=meine_kontonr
go