/********************************	Gegenüberstellung	SELECT INTO
																			INSERT SELECT
											
											einfaches Beispiel
*******************************************************************************/

									--neue Tabelle region_kopie
									--wird erstellt
									--Ergebnis der SELECT-Anweisung
									--wird in diese Tabelle physisch gespeichert
									--bei Microsoft SQL Server!!!
									
									--geeignet für:	einmaliges Kopieren
select *
into	region_kopie
from northwind.dbo.region;

select * from region_kopie;

truncate table region_kopie;


/*******************************bei		Oracle,
										MySQL,
										PostgreSQL geht das so:
													
create table region_kopie
as
select * from northwind.dbo.region
***************************************************************************/

									--geeignet für:	regelmäßiges Kopieren
									
									--Zieltabelle muss vorhanden sein
insert into region_kopie
select * from northwind.dbo.region;


	
	
									--etwas komplexeres Beispiel											

create table address
(	city		varchar(50),
	country		varchar(50),
	postalcode	varchar(10),
	streetnumber varchar(100)
);

select * from address;

exec sp_help address;

insert into address
--( city, country, postalcode, streetnumber)
select	city,
		country,
		postalcode,
		address
from customers
union all
select	city,
		country,
		postalcode,
		address
from suppliers;







--Gegenüberstellung:	SELECT INTO

select	city, address, postalcode, 'Kundenadresse' as herkunft
into adresstabelle
from	customers

union

select	city, address, postalcode, 'Mitarbeiteradresse' as addresstyp
from	employees

union

select city, address, postalcode, 'Lieferantenadresse'
from	suppliers;



select * from adresstabelle;




															--Mehrzeilen-INSERT
insert into shippers
values	('Firma1', '12345'),
		('Firma2', '54321');
			
select * from shippers;		








