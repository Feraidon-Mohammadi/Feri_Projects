create database AWIndex;


use AWIndex;

									--für den Fall, dass die Tabelle
									--bereits existiert,
									--wird sie vorsichtshalber gelöscht

if exists
(	select * from sys.tables where name='orderdetails')
									
drop table orderdetails;




drop table if exists orderdetails ;	--seit SQL Server 2016
									


									--Fusionieren von Orders und
									--[Order Details] zu einer
									--hinreichend großen Tabelle
									--ohne Constraints und Indizes
select	soh.[SalesOrderID]
,		[CustomerID]
,		[OrderDate]
,		[DueDate]
,		[ShipDate]
,		[Status]
,		[OnlineOrderFlag]
,		[AccountNumber]
,		[SalesPersonID]
,		[TerritoryID]
,		[ShipMethodID]
,		[Freight]
,		[TaxAmt]
,		[ProductID]
,		[OrderQty]
,		[UnitPrice]
,		[UnitPriceDiscount]

into orderdetails

from [AdventureWorks2017].[Sales].[SalesOrderHeader] as soh
join	[AdventureWorks2017].[Sales].[SalesOrderDetail] as sod
on	soh.[SalesOrderID]=sod.[SalesOrderID];



drop table if exists orderdetails_ohneIX ;
									--Dieselbe Tabelle noch mal 
									--zu Vergleichszwecken
									--die bleibt ohne Index
select	soh.[SalesOrderID]
,		[CustomerID]
,		[OrderDate]
,		[DueDate]
,		[ShipDate]
,		[Status]
,		[OnlineOrderFlag]
,		[AccountNumber]
,		[SalesPersonID]
,		[TerritoryID]
,		[ShipMethodID]
,		[Freight]
,		[TaxAmt]
,		[ProductID]
,		[OrderQty]
,		[UnitPrice]
,		[UnitPriceDiscount]

into	orderdetails_ohneIX

from [AdventureWorks2017].[Sales].[SalesOrderHeader] as soh
join	[AdventureWorks2017].[Sales].[SalesOrderDetail] as sod
on	soh.[SalesOrderID]=sod.[SalesOrderID];


								
									--Tatsächlichen Ausführungsplan einschließen
select * from orderdetails;	
									--Erläutern:	Table Scan		Heap
													--Nachteile
													--Vorteile
														
											
dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;

									
select * from orderdetails			--Table Scan
where productid=780; 


create index ix_odetails_prodid				--Index erstellen
on orderdetails(productid);


dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;		



select * from orderdetails					--immer noch:	Table Scan
where productid=780;

								
									--Ermitteln von productid
									--mit hoher Selektivität
select productid, count(*)
from orderdetails
group by productid
order by 2;


									--Indexsuche vs. Tablescan
select * from orderdetails
where productid=950;

select * from orderdetails_ohneIX
where productid=950;

									--höchste Selektivität
									--trotzdem mehr Ressourcenverbrauch

select * from orderdetails
where productid=897;

select * from orderdetails_ohneIX
where productid=897;



									--Selektivität ist gerade noch gut genug 
									--für Indexsuche

select * from orderdetails
where productid=996;

select * from orderdetails_ohneIX
where productid=996;





dbcc show_statistics('orderdetails', 'productid');

select productid, count(*)
from orderdetails
where productid in(710, 709)
group by productid
order by 2;



--										--Unique Index
--										--als Alternativschlüssel
--create unique index ixuq_odetails_2col
--on orderdetails(orderid, productid);


--dbcc showcontig('orderdetails')
--with tableresults, all_indexes, all_levels;





										--Tablescan
select	salesorderid,
		productid,
		convert(money, unitprice*orderqty)as linetotal
from	orderdetails
where	salesorderid=72211;


select	salesorderid,
		convert(money, sum(unitprice*orderqty))as ordertotal
from	orderdetails
group by salesorderid;

										--Einspaltenindex
										
create index ix_odetails_ordid
on orderdetails(salesorderid);										
										
										--Indexsuche
select	salesorderid,
		productid,
		convert(money, unitprice*orderqty)as linetotal
from	orderdetails
where	salesorderid=72211;


select	salesorderid,
		convert(money, sum(unitprice*orderqty))as ordertotal
from	orderdetails
group by salesorderid;



dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;	



										--Mehrspaltenindex,
										
create index ix_odetails_multicol
on orderdetails(salesorderid, productid, unitprice, orderqty);

dbcc show_statistics('orderdetails', 'ix_odetails_multicol');


dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;



										--nutzt den Mehrspaltenindex
										--zum Abdecken der Abfrage(?)
select	salesorderid,
		productid,
		convert(money, unitprice*orderqty)as linetotal
from	orderdetails
where	salesorderid=72211;


										--Scant den Mehrspaltenindex
										--IndexScan
select	salesorderid,
		convert(money, sum(unitprice*orderqty))as ordertotal
from	orderdetails
group by salesorderid;	




select	salesorderid,
		productid,
		convert(money, unitprice*orderqty)as linetotal
from	orderdetails_ohneIX
where	salesorderid=72211;


										--Scant den Mehrspaltenindex
										--IndexScan(nicht in AdventureWorks)
select	salesorderid,
		convert(money, sum(unitprice*orderqty))as ordertotal
from	orderdetails_ohneIX
group by salesorderid;


										--Einspaltenindex auf Tabelle ohneIX
										--und Vergleich wiederholen
create index ix_od_ox_ordid
on orderdetails_ohneIX(salesorderid);


select	salesorderid,
		productid,
		convert(money, unitprice*orderqty)as linetotal
from	orderdetails
where	salesorderid=72211;


select	salesorderid,
		productid,
		convert(money, unitprice*orderqty)as linetotal
from	orderdetails_ohneIX
where	salesorderid=72211;


										--Mehrspaltenindex kann nicht helfen
										--weil Spalte DISCOUNT 
										--im Mehrspaltenindex fehlt
select	salesorderid,
		productid,
		convert(money, unitprice*orderqty*(1-unitpricediscount))as linetotal
from	orderdetails
where	salesorderid=72211;


select	salesorderid,
		productid,
		convert(money, unitprice*orderqty*(1-unitpricediscount))as linetotal
from	orderdetails
where	salesorderid=51120;






										--würde zwar gehen
										--würde aber auch Systemlast erzeugen
										--beim Erstellen und bei der Indexpflege
										--(nicht wirklich erstellen)
create index ix_odetails_multicovercol
on orderdetails(	salesorderid, customerid, orderdate, productid, 
					unitprice, orderqty, unitpricediscount);
							
					

										
										--Kompromiss
										--nicht alle Spalten sind Indexschlüssel
										--einige werden nur eingeschlossen
create index ix_odetails_covercol
on orderdetails(salesorderid, orderdate, customerid)
include(unitprice, orderqty, unitpricediscount, productid);



dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;		



									--es wird in allen drei Fällen 
									--der Mehrspaltenindex mit INCLUDE
									--verwendet
select	salesorderid,
		customerid,
		orderdate,
		productid,
		convert(money, unitprice*orderqty*(1-unitpricediscount) )as linetotal
from	orderdetails
where salesorderid=72211;


select	salesorderid,
		customerid,
		orderdate,
		convert(money, sum(unitprice*orderqty*(1-unitpricediscount) ))as linetotal
from	orderdetails
--where orderid=11000
group by salesorderid, customerid, orderdate;


select	salesorderid,
		customerid,
		orderdate,
		convert(money, sum(unitprice*orderqty*(1-unitpricediscount) ))as linetotal
from	orderdetails
where salesorderid=72211
group by salesorderid, customerid, orderdate;


select count(distinct productid) from orderdetails;		--266
dbcc show_statistics(orderdetails, ix_odetails_prodid);
dbcc show_statistics(orderdetails, ix_odetails_covercol);

exec sp_help orderdetails;

select * from orderdetails
where salesorderid=(	select max(salesorderid) from orderdetails);


								--Indizes und Schreibzugriffe
								--(hier:	INSERT)
insert into orderdetails_ohneIX(	salesorderid, customerid, orderdate, duedate, 
							status, onlineorderflag, shipmethodid, freight, taxamt, 
							productid, unitprice, orderqty, unitpricediscount)
									
values(	75123, 18759, '20140630', '20140712', 5, 1, 1, 4.7493, 15.1976, 841,  59.99, 4, 0);


insert into orderdetails(	salesorderid, customerid, orderdate, duedate, 
							status, onlineorderflag, shipmethodid, freight, taxamt, 
							productid, unitprice, orderqty, unitpricediscount)
									
values(	75123, 18759, '20140630', '20140712', 5, 1, 1, 4.7493, 15.1976, 841,  59.99, 4, 0);


select * from orderdetails
where salesorderid=75123;


delete from orderdetails_ohneIX
where salesorderid=75123 and productid=841;

delete from orderdetails
where salesorderid=75123 and productid=841;

/*ganz wichtig:			--im Ausführungsplan
						--beim Objekt Table Insert	
						--die Objekte anzeigen
********************************************************/	




									--Reorganisieren eines nonclustered index

drop index orderdetails.ix_odetails_prodid;


create index ix_odetails_prodid	--Index neu
on orderdetails(productid);	




								--neuere Methode der Indexauffrischung
alter index ix_odetails_prodid
on orderdetails
rebuild;

						



					
								--Anzeigen von Indexeigenschaften

dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;

								--Index mit FILLFACTOR

create index ix_odetails_prodid_50
on orderdetails(productid)
with(	fillfactor=50);	

								--Anzeigen und Vergleichen der Indexeigenschaften	
								
dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;

								--in regelmäßigen Abständen
alter index ix_odetails_prodid_50
on orderdetails
rebuild
with(	fillfactor=50);	
																

drop index orderdetails.ix_odetails_ordid;	--Löscht nur den Index

drop table orderdetails;		--Löschen der Tabelle löscht auch 
								--alle Indizes der Tabelle
								
--Kurz zu CLUSTERED INDEX						


select	soh.[SalesOrderID]
,		[CustomerID]
,		[OrderDate]
,		[DueDate]
,		[ShipDate]
,		[Status]
,		[OnlineOrderFlag]
,		[AccountNumber]
,		[SalesPersonID]
,		[TerritoryID]
,		[ShipMethodID]
,		[Freight]
,		[TaxAmt]
,		[ProductID]
,		[OrderQty]
,		[UnitPrice]
,		[UnitPriceDiscount]

into orderdetails

from [AdventureWorks2017].[Sales].[SalesOrderHeader] as soh
join	[AdventureWorks2017].[Sales].[SalesOrderDetail] as sod
on	soh.[SalesOrderID]=sod.[SalesOrderID];

	

create index ix_odetails_prodid				--Index neu(?)
on orderdetails(productid);


dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;	


							--Abfrageplan mit
							--Nonclustered Index auf Heap
select * from orderdetails
where productid=897;


alter table orderdetails
add constraint pk_od primary key(salesorderid, productid);	


dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;	


--alter table orderdetails
--drop constraint pk_od;


							--Abfrageplan mit
							--Nonclustered Index auf Clustered Index
select * from orderdetails
where productid=960;

select * from orderdetails
where productid=780;

select * from orderdetails_ohneIX
where productid=780;


dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;	

dbcc showcontig('orderdetails_ohneIX')
with tableresults, all_indexes, all_levels;	


							--Pflege eines Clustered Index
							--in regelmäßigen Zeitabständen
							
alter index pk_od
on orderdetails
rebuild
with (fillfactor=70);

alter index ix_odetails_prodid
on orderdetails
rebuild;


							--Emitteln des Grades
							--der Fragmentierung
select	a.index_id, name, avg_fragmentation_in_percent
from	sys.dm_db_index_physical_stats (	DB_ID('nwmewes'), 
											OBJECT_ID('orderdetails'),
											NULL, NULL, NULL) AS a
join	sys.indexes as b 
on		a.object_id = b.object_id 
and		a.index_id = b.index_id;


exec sp_help orderdetails;


--Empfehlung, welche Spalten in einem			Clustered Index

--PRIMARY KEY
	
	--wenn der Primärschlüssel NONCLUSTERED sein soll:
	
	-- alter table orders 
	-- add primary key nonclustered(orderid)
	
	
	--wenn PRIMARY KEY nicht CLUSTERED
	--dann:	Spalten, die häufig für Bereichssuchen verwendet werden, z.B.:
	
	--CREATE CLUSTERED INDEX ix_orders_odate_cl
	--ON orders(orderdate) 
	

--Empfehlung für											NonClustered Index

	--Spalten, die viel in der WHERE-Klausel verwendet werden
	--Spalten, die häufig in GROUP BY-Klauseln verwendet werden
	--Foreign Key-Spalten	
	--Spalten mit hoher Selektivität(relativ wenig Mehrfachnennungen)
	

	--Spaltengruppen für Mehrspaltenindizes, die sich für abgedeckte Abfragen eignen

							