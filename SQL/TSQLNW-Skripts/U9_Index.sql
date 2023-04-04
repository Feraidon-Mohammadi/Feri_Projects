create database NWIndex;


use NWIndex;

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
select		o.*,
			ProductID,
			Quantity,
			UnitPrice,
			Discount

into orderdetails

from Northwind.dbo.Orders o
join Northwind.dbo.[Order Details] od
on	o.OrderID=od.OrderID;



drop table if exists orderdetails_ohneIX ;
									--Dieselbe Tabelle noch mal 
									--zu Vergleichszwecken
									--die bleibt ohne Index
select		o.*,
			ProductID,
			Quantity,
			UnitPrice,
			Discount

into orderdetails_ohneIX

from Northwind.dbo.Orders o
join Northwind.dbo.[Order Details] od
on	o.OrderID=od.OrderID;


								
									--Tatsächlichen Ausführungsplan einschließen
select * from orderdetails;	
									--Erläutern:	Table Scan		Heap
													--Nachteile
													--Vorteile
														
											
dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;

									
select * from orderdetails			--Table Scan
where productid=77; 


create index ix_odetails_prodid				--Index erstellen
on orderdetails(productid);


dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;		



select * from orderdetails					--immer noch:	Table Scan
where productid=77;

								
									--Ermitteln von productid
									--mit hoher Selektivität
select productid, count(*)
from orderdetails
group by productid
order by 2;


									--Indexsuche
select * from orderdetails
where productid=9;

select * from orderdetails_ohneIX
where productid=9;


select * from orderdetails
where productid=8;


dbcc show_statistics('orderdetails', 'productid');

select productid, count(*)
from orderdetails
where productid in(28,29)
group by productid
order by 2;

									--weiter Table Scan
									--(bei geringer Selektivität
									-- resp. hoher Dichte)
select * from orderdetails	
where productid=16;



--										--Unique Index
--										--als Alternativschlüssel
--create unique index ixuq_odetails_2col
--on orderdetails(orderid, productid);


--dbcc showcontig('orderdetails')
--with tableresults, all_indexes, all_levels;		


										--Tablescan
select	orderid,
		productid,
		convert(money, unitprice*quantity)as linetotal
from	orderdetails
where orderid=11000;


select	orderid,
		convert(money, sum(unitprice*quantity))as ordertotal
from	orderdetails
group by orderid;

										--Einspaltenindex
										
create index ix_odetails_ordid
on orderdetails(orderid);										
										
										--Indexsuche
select	orderid,
		productid,
		convert(money, unitprice*quantity)as linetotal
from	orderdetails
where orderid=11000;

										--Tablescan
select	orderid,
		convert(money, sum(unitprice*quantity))as ordertotal
from	orderdetails
group by orderid;										



										--Mehrspaltenindex,
										
create index ix_odetails_multicol
on orderdetails(orderid, productid, unitprice, quantity);

dbcc show_statistics('orderdetails', 'ix_odetails_multicol');


dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;



										--nutzt den Mehrspaltenindex
										--zum Abdecken der Abfrage(?)
select	orderid,
		productid,
		convert(money, unitprice*quantity)as linetotal
from	orderdetails
where orderid=11000;

										--Scant den Mehrspaltenindex
										--IndexScan
select	orderid,
		convert(money, sum(unitprice*quantity))as ordertotal
from	orderdetails
group by orderid;	


select	orderid,
		productid,
		convert(money, unitprice*quantity)as linetotal
from	orderdetails_ohneIX
where orderid=11000;

										--Scant den Mehrspaltenindex
										--IndexScan
select	orderid,
		convert(money, sum(unitprice*quantity))as ordertotal
from	orderdetails_ohneIX
group by orderid;


										--Einspaltenindex auf Tabelle ohneIX
										--und Vergleich wiederholen
create index ix_od_ox_ordid
on orderdetails_ohneIX(orderid);


select	orderid,
		productid,
		convert(money, unitprice*quantity)as linetotal
from	orderdetails
where orderid=11000;


select	orderid,
		productid,
		convert(money, unitprice*quantity)as linetotal
from	orderdetails_ohneIX
where orderid=11000;


										--Mehrspaltenindex kann nicht helfen
										--weil Spalte DISCOUNT 
										--im Mehrspaltenindex fehlt
select	orderid,
		productid,
		convert(money, unitprice*quantity*(1-discount))as linetotal
from	orderdetails
where orderid=11000;


select	orderid,
		productid,
		convert(money, unitprice*quantity*(1-discount))as linetotal
from	orderdetails
where orderid=11077;



drop index orderdetails.ix_odetails_multicol;

drop index orderdetails.ix_odetails_ordid;


										--würde zwar gehen
										--würde aber auch Systemlast erzeugen
										--beim Erstellen und bei der Indexpflege
										--(nicht wirklich erstellen)
create index ix_odetails_multicovercol
on orderdetails(	orderid, customerid, orderdate, productid, 
					unitprice, quantity, discount);
							
drop index orderdetails.ix_odetails_multicovercol;						

										
										--Kompromiss
										--nicht alle Spalten sind Indexschlüssel
										--einige werden nur eingeschlossen
create index ix_odetails_covercol
on orderdetails(orderid, orderdate, customerid)
include(unitprice, quantity, discount, productid);



dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;		



									--es wird in allen drei Fällen 
									--der Mehrspaltenindex mit INCLUDE
									--verwendet
select	orderid,
		customerid,
		orderdate,
		productid,
		convert(money, unitprice*quantity*(1-discount) )as linetotal
from	orderdetails
where orderid=11000;


select	orderid,
		customerid,
		orderdate,
		convert(money, sum(unitprice*quantity*(1-discount) ))as linetotal
from	orderdetails
--where orderid=11000
group by orderid, customerid, orderdate;


select	orderid,
		customerid,
		orderdate,
		convert(money, sum(unitprice*quantity*(1-discount) ))as linetotal
from	orderdetails
where orderid=11000
group by orderid, customerid, orderdate;


dbcc show_statistics(orderdetails, ix_odetails_prodid);
dbcc show_statistics(orderdetails, ix_odetails_covercol);

exec sp_help orderdetails;


								--Indizes und Schreibzugriffe
								--(hier:	INSERT)


insert into orderdetails(	orderid, customerid, orderdate,
							productid, unitprice, quantity, discount)
									
values(	11079, 'TRAIH', getdate(), 44,  19.45, 12, 0);

select * from orderdetails
where orderid>11070;

delete from orderdetails
where orderid=11079;

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


select	Orders.*,
		ProductID,
		Quantity,
		UnitPrice,
		Discount
into orderdetails
from Orders
join	[Order Details] od
on	Orders.OrderID=od.OrderID;	

	

create index ix_odetails_prodid				--Index neu(?)
on orderdetails(productid);


dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;	


							--Abfrageplan mit
							--Nonclustered Index auf Heap
select * from orderdetails
where productid=9;


alter table orderdetails
add constraint pk_od primary key(orderid, productid);	


dbcc showcontig('orderdetails')
with tableresults, all_indexes, all_levels;	


--alter table orderdetails
--drop constraint pk_od;


							--Abfrageplan mit
							--Nonclustered Index auf Clustered Index
select * from orderdetails
where productid=9;

select * from orderdetails
where productid=77;

select * from orderdetails_ohneIX
where productid=77;





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

							