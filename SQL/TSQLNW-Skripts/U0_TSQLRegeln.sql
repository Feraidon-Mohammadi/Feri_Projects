use northwind;

--Zeilenkommentar...die nächste nicht gekennzeichnete Zeile
--wird wieder als Anweisung interpretiert

select * from products;		--Semikolon als Befehlsbegrenzer
							--kann, muss nicht

/*	Block-Kommentar
	gilt bis zum Erscheinen
	der Ende-Begrenzung
*/

/************************************************************
	Eignet sich zum Hervorheben
	von Überschriften
	und Erläuterungstext, Hinweisen etc.
************************************************************/


			--auch mehrzeilige Anweisungen
			--könnne auskommentiert werden

/***********************************************************
	update northwind.dbo.products
	set unitprice=unitprice*1.3;
***********************************************************/


/*	Bezeichnerregeln:	max. 128 Zeichen
						alphanumerisch + _ + $ + # + @
						[erlaubt auch Blanks und Bindestrich]
						"dsgl, wenn die entsprechende
						 SET-Option gesetzt ist"
						@für lokale Variable und Parameter
						#für temporäre Objekte

	
	Objekt								...from Products
	Schema.Objekt						...from dbo.Products
	Datenbank.Schema.Objekt				...from Northwind.dbo.Products
	Datenbank..Objekt					...from Northwind..Products
*/

use BeispielDB

select * from dbo.kunden;

select * from products

select * from dbo.products

select * from northwind.dbo.products

select * from northwind.products

select * from northwind..products

--Batch-Verarbeitung

/***	Anw.		Gemeinsam kompilierte Anweisungen
		Anw.
		GO
		
		Anw.		jedoch keine Garantie 
		Anw.		für gemeinsame Ausführung
		Anw.
		GO

	lokale Variable existieren nur innerhalb des Batches,
	in dem sie deklariert werden,
	ergo auch nur innerhalb der Prozedur, Funktion...
***/

use Northwind;


declare	@va decimal(8,2);

set			@va=10999.45;

print			@va;



declare @va decimal(8,2)

select	@va=unitprice
from		products 
where	productid=5

print @va



declare @va decimal(8,2)

set		@va=(	select unitprice
				from products 
				where productid=7
			)

print 'Produkt Nr. 7 kostet $'+cast(@va as char(8))



create database db1
go
use db1

if exists (	select * from sys.objects
			where name='address'
			and type='U')
begin
	drop table address
end;

create table address
(	plz			char(5),
	ort			varchar(50),
	strasse		varchar(80)
);

								--seit SQLServer2017
drop table if exists address ;




	