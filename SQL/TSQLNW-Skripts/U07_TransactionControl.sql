/*************************************************************************
				Arbeiten mit Transaktionen

				F�r Transaktionen gilt das ACID-Prinzip

				A-------Atomarit�t
				C-------Consistenz
				I-------Isolation
				D-------Dauerhaftigkeit

	Die nachfolgenden Beispiele sind f�r fiktive Tabellen geschrieben
	und daher nicht ausf�hrbar
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