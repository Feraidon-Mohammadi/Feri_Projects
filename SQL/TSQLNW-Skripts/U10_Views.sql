								/*	einfaches View am Anfang	*/

use nwmewes;

						--vom Client-Programm
						--ohne View
select	productid, 
		productname,
		supplierid,
		quantityperunit,
		unitprice
from	products
where	categoryid=1;	



						--View auf dem Server erstellen
create view v_beverages
as
select	productid, 
		productname,
		supplierid,
		quantityperunit,
		unitprice
from	products
where	categoryid=1;	


						--vom Client-Programm
						--mit View					
select * from v_beverages
order by supplierid;




select * from v_beverages
where supplierid=16;


exec sp_help v_beverages;
exec sp_helptext v_beverages;





								/*	meckert wegen IDENTITY */

insert into v_beverages
values(100, 'Neustrelitzer Dünnbier', 12, '0,5 Liter Flaschen', 10);

insert into v_beverages
values( 'Neustrelitzer Dünnbier', 12, '0,5 Liter Flaschen', 10);



select * from Products
where ProductID>77;
								/*	SELECT zeigt die Zeile nicht an
									weil im View die Spalte categoryid
									fehlt, und sie damit beim INSERT
									nicht 1 werden konnte			*/
select * from v_beverages
where ProductID>77;



alter view v_beverages
as
select	productid, 
		productname,
		categoryid,
		supplierid,
		quantityperunit,
		unitprice
from products
where categoryid=1;	

insert into v_beverages
values( 'Neustrelitzer Dünnbier', 1, 12, '0,5 Liter Flaschen', 10);
	

select * from v_beverages
where productid>77;

select * from products
where productid>77;

								/*	UPDATE sowieso	*/

update v_beverages
set categoryid=1
where productid=78;

update products
set categoryid=1
where productid=78;


update v_beverages
set quantityperunit='0.5 ltr bottles'
where productid=78;

								/*	dieses INSERT erzeugt eine Zeile,
									die das View gar nicht zeigen kann	*/
									
insert into v_beverages
values( 'Lausitzer Salzbrezeln', 3, 11, '500g Pack.', 2.50);	


select * from v_beverages
where productid>77;

								/*	Die Zeile ist nur in der Tabelle 
									sichtbar							*/
select * from products
where productid>77;


								/*	View mit CHECK OPTION ergänzen		*/
alter view v_beverages
as
select	productid, 
		productname,
		categoryid,
		supplierid,
		quantityperunit,
		unitprice,
		discontinued
from	products
where	categoryid=1
with check option;


								/*	Dieser Datensatz geht jetzt 
									nicht mehr über das View(!!!)	*/
insert into v_beverages
values('Das Harzer Käsewunder', 4, 12, '200g Rolle', 2.50);


								/*	View mit CHECK OPTION
									und vier Filtern in der
									WHERE-Klause					*/
									
create view v_beverages2
as
select	productid, 
		productname,
		categoryid,
		supplierid,
		quantityperunit,
		unitprice
from	products

where	categoryid=1
and		unitprice<10
and		supplierid between 10 and 20

with check option;


select * from v_beverages2;

							--scheitert
update v_beverages2
set unitprice=unitprice+5;
							--scheitert
update v_beverages2
set supplierid=5;
							--geht
update v_beverages2
set unitprice=unitprice+1;										



					/*	View mit berechnetem Feld	*/

drop view v_orderdetails_total;
								
create view v_orderdetails_total
as
select	orderid,
		productid,
		unitprice,
		quantity,
		discount,
		unitprice*quantity*(1-discount) as linetotal
from	[order details];	


select * from [order details];


select * from v_orderdetails_total
where orderid=11000;



								--geht
update	v_orderdetails_total
set		discount=0.1
where	orderid=11000
and		productid=77;


								--geht nicht
update	v_orderdetails_total
set		linetotal=300
where	orderid=11000
and		productid=77;

	
								--geht
begin tran;

delete from v_orderdetails_total
where		orderid=11000
and			productid=77;

select * from	v_orderdetails_total
where			orderid=11000;

rollback tran;	

						--INSERT scheitert 
insert into v_orderdetails_total
values(11000, 10, 31, 10, 0, 310);

insert into v_orderdetails_total
values(11000, 10, 31, 10, 0);

						--so gehts(Spalte LINETOTAL weggelassen)

insert into v_orderdetails_total(orderid, productid, unitprice, quantity, discount)
values(11000, 10, 31, 10, 0);


/***********************************************************	
	Alternativ:
	Berechnetes Feld in der Basistabelle	

alter table [order details]
add linetotal as (unitprice*quantity*(1-discount)) persisted;

exec sp_help [order details];

select	name,
		definition,
		object_id,
		column_id
from sys.computed_columns;

									--so nicht
insert into [order details]
values(11000, 10, 31, 10, 0, 310);
									--aber so
insert into [order details]
values(11000, 50, 16.25, 10, 0);


		--jetzt ist das View natürlich doppelt gemoppelt
								
select * from [order details]
where orderid=11000;	

alter table [order details]
drop column linetotal;



***********************************************************/


					/*	View mit Join
						und Rechenausdruck		*/
create view v_orders_complett
as
select	orders.orderid,
		customerid,
		orderdate,
		shipvia,
		freight,
		productid,
		unitprice,
		quantity,
		discount,										--so ein Spaltenalias
		convert(decimal(10,2),linetotal) as linetotal	--geht in Access gar nicht
from	orders
join	v_orderdetails_total
on		orders.orderid=v_orderdetails_total.orderid
where	year(orderdate)=2021;


select * from v_orders_complett;
												
								--geht
update	v_orders_complett
set		discount=.1
where	orderid=10400
and		productid=29;

select * from	v_orders_complett
where			orderid=10400;

select * from	[order details]
where			orderid=10400;


begin tran;
								--geht nicht
delete from	v_orders_complett
where		orderid=10400
and			productid=29;

select * from	v_orders_complett
where			orderid=10400;

--select * from [order details]
--where orderid=10400;

--select * from orders
--where orderid=10400;

rollback tran;

select * from v_orders_complett
where orderid=10807;

								--geht nicht
insert into v_orders_complett
values(10807, 'FRANS', '31.12.2021', 1, 1.36, 41, 9.65, 20);



										/*	View mit GROUP BY
											und Aggregat			*/
											
create view v_orders_summ
as
select	orderid,
		customerid,
		orderdate,
		sum(convert(decimal(10,2),linetotal)) as ordertotal	
from	v_orders_complett

group by	orderid,
			customerid,
			orderdate;
			
			
			
select * from v_orders_summ;
	
							--keine Art von DML-Operation möglich
							
delete from v_orders_summ where orderid=10400;

update	v_orders_summ
set		ordertotal=2500
where	orderid=10400;		

update	v_orders_summ
set		customerid='ALFKI'
where	orderid=10400;


						/*	Vier Ergebnisse zu einem vereinigen			*/
						
select 	shipcountry,
		year(orderdate) as jahr,
		datepart(q, orderdate) as quartal,
		sum(unitprice*quantity*(1-discount)) as umsatzsumme, 
		count(od.orderid)		as anzahl_bestellposten
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by	shipcountry,
			year(orderdate), 
			datepart(q, orderdate);
          
          
select 	year(orderdate) as jahr,
		sum(unitprice*quantity*(1-discount)), 
		count(od.orderid)		as anzahl_bestellposten
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by  year(orderdate);



select 	shipcountry,
		sum(unitprice*quantity*(1-discount)) as umsatzsumme, 
		count(od.orderid)		as anzahl_bestellposten
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by  shipcountry;						


						/*	großer Vorteil von Views:
							komplexer Quelltext liegt auf dem Server
							vom Frontend genügt eine simple Abfrage		*/				

create view v_analysen_nach_land_und_jahr
as

select 	shipcountry,
		year(orderdate) as jahr,
		datepart(q, orderdate) as quartal,
		sum(unitprice*quantity*(1-discount)) as umsatzsumme, 
		count(od.orderid)		as anzahl_bestellposten
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by  shipcountry,
          year(orderdate), 
          datepart(q, orderdate)

union

select 	null as lieferland,
		year(orderdate) as jahr,
		datepart(q, orderdate) as quartal,
		sum(unitprice*quantity*(1-discount)), 
		count(od.orderid)		as anzahl_bestellposten
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by  year(orderdate), 
          datepart(q, orderdate)

union

select 	null as lieferland,
		year(orderdate) as jahr,
		null as quartal,
		sum(unitprice*quantity*(1-discount)), 
		count(od.orderid)		as anzahl_bestellposten
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by  year(orderdate)

union

select 	shipcountry,
		null as jahr,
		null as quartal,
		sum(unitprice*quantity*(1-discount)) as umsatzsumme, 
		count(od.orderid)		as anzahl_bestellposten
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by  shipcountry;


select * from v_analysen_nach_land_und_jahr; 
          



select	shipcountry, 
		jahr, 
		quartal, 
		convert (money, umsatzsumme) as umsatzsumme
from	v_analysen_nach_land_und_jahr
where	jahr=2020
and		umsatzsumme>20000
order by 2;


/*******************************************************************************************
Schreibzugriffe auf Views sind nur dann uneingeschränkt möglich, wenn
-	das View nur auf eine Basistabelle zugreift
-	alle NOT NULL-Spalten der Basistabelle enthält
-	und das View keines der folgenden Konstrukte enthält:
	-	DISTINCT
	-	berechnete Felder
	-	Join	(UPDATE möglich)
	-	GROUP BY und Aggregatfunktion(SUM, AVG, MIN, MAX, COUNT,...)
	-	UNION, INTERSECT, EXCEPT
*********************************************************************************************/



/********************************************************************************************

 
		
*********************************************************************************************/