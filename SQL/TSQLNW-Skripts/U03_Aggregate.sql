use northwind;
go


select 	orderid, freight, shipcountry, customerid, orderdate
from 	orders;



select avg(freight) as mittlere_frachtkosten from orders;

select avg(freight) as mittlere_frachtkosten, shipcountry from orders;



select	avg(freight) as durchschnitt,
		min(freight) as minimum,
		max(freight) as maximum,
		sum(freight) as summe,
		count(freight) as anzahl_der_werte,
		count(shippeddate) as anzahl_lieferdatum,
		count(distinct shippeddate) as anzahl_dist_lieferdatum,
		count(*) as anzahl_der_zeilen,
		stdev(freight) as standardabweichung,
		var(freight) as varianz,
		var(year(shippeddate)) as varianz_ld
from	orders;


select	avg(freight) as durchschnitt,
		min(freight) as minimum,
		max(freight) as maximum,
		count(*) as anzahl
from 	orders
where	year(orderdate)=2020;


select	avg(freight) as durchschnitt,
		min(freight) as minimum,
		max(freight) as maximum,
		count(*) as anzahl
from 	orders
where	year(orderdate) in(2020, 2021, 2022);

----------------------------------------------------Wirkungsweise von GROUP BY
select	orderid,
		orderdate,
		datepart(q, orderdate) as quarter,
		datepart(yy, orderdate) as year
from	orders;



select datepart(q, orderdate) as quartal
from orders
group by datepart(q, orderdate);


select	year(orderdate) as jahr,
		datepart(q, orderdate) as quartal
from orders
group by year(orderdate),datepart(q, orderdate);	

-----------------------------------------------------------------------------------

select	year(orderdate) as jahr,
		avg(freight) as durchschnitt,
		min(freight) as minimum,
		max(freight) as maximum,
		count(*) as anzahl
from 	orders
group by year(orderdate);	



select	shipcountry,
		avg(freight) as durchschnitt,
		min(freight) as minimum,
		max(freight) as maximum,
		count(*) as anzahl
from 	orders
group by shipcountry
order by 2 desc;


					--VERBOTEN!!!!!!!!!!!!!!!!!!!!!!!!!
					--wann immer Aggregatfunktionen
					--in der SELECT-Klausel verwendet werden,
					--dürfen nur die Detail-Ausdrücke 
					--in der SELECT-Klausel stehen, 
					--die auch in der GROUP BY-Klausel stehen
select	shipcountry,
		shipvia,
		avg(freight) as durchschnitt,
		min(freight) as minimum,
		max(freight) as maximum,
		count(*) as anzahl
from 	orders
group by shipcountry
order by 1;


					--so darfs sein
select	shipcountry,					--1
		shipvia,
		avg(freight) as durchschnitt,	--3
		min(freight) as minimum,
		max(freight) as maximum,
		count(*) as anzahl
from 	orders
group by shipcountry, shipvia
order by 1, 3 desc;	


select	shipcountry,					--1
		shipvia,
		avg(freight) as durchschnitt,	--3
		min(freight) as minimum,
		max(freight) as maximum,
		count(*) as anzahl
from 	orders
group by shipcountry, shipvia
order by shipcountry, avg(freight) desc;	



select	shipcountry,
		companyname,
		avg(freight) as durchschnitt,
		min(freight) as minimum,
		max(freight) as maximum,
		count(*) as anzahl
from 	orders
join 	shippers							--****
on		orders.shipvia=shippers.shipperid	--****
where	year(orderdate)=2021				--****
group by shipcountry, companyname
order by 2, 3 desc;


												--HAVING				
select	shipcountry,
		companyname,
		avg(freight) as durchschnitt,
		min(freight) as minimum,
		max(freight) as maximum,
		count(*) as anzahl
from 	orders
join 	shippers
on		orders.shipvia=shippers.shipperid
--where  avg(freight)<50
group by shipcountry, companyname
having	avg(freight)<50
order by 1, 3 desc;





					--Order Details
					--wie sie gespeichert ist
select 	* 
from	[order details];


					--mit Umsatz pro Bestellzeile
					--!!!Mehrfachausgabe von OrderID beachten!!!				
select 		*,		unitprice*quantity*(1-discount)
from		[order details];


					--Gesamtumsatz
					--pro Bestellung
select	orderid,
		sum(unitprice*quantity*(1-discount))	as ordertotal
from	[order details]
group by orderid;



select	orderid,
		convert( decimal(10,2),sum(unitprice*quantity*(1-discount)))
		as ordertotal
from	[order details]
group by orderid;
					
					
select	orderid,
		sum(convert( decimal(10,2),unitprice*quantity*(1-discount)))
		as ordertotal
from	[order details]
group by orderid;


					--Bestellungen
					--mit einem Umsatz über 10000
select	orderid,
		sum(convert(decimal(10,2),	unitprice*quantity*(1-discount)))
		as ordertotal
from	[order details]
group by orderid
having	sum(unitprice*quantity*(1-discount))>10000;


					--zzgl. Kundeninformation
select	orders.orderid,
		companyname, city,											--**** 
		convert(decimal(7,2), sum(unitprice*quantity*(1-discount)))
		as gesamt
from	[order details] od
join	orders														--****
on 		orders.orderid=od.orderid
join	customers													--****
on 		orders.customerid=customers.customerid
group by orders.orderid, 
		companyname, city											--****
having	sum(unitprice*quantity*(1-discount))>10000

order by companyname;




--Aggregate mit DISTINCT
select	year(orderdate) as jahr,
		count(*) as anzahl_bestellungen		
from	orders
group by year(orderdate);


select	year(orderdate) as jahr,
		count(*) as anzahl_bestellungen,
		count(orderid) as anzahl_bestellnummern,
		count(customerid) as [anzahl kunden?]
from	orders
group by year(orderdate);


select	year(orderdate) as jahr,
		count(*) as anzahl_bestellungen,
		count(orderid) as anzahl_orderid,
		count(customerid) as auch_anzahl_bestellungen,
		count(distinct customerid) as anzahl_kunden,
		count(distinct shipcountry) as anzahl_bestimmungslaender,
		count(shipcountry)
from	orders
group by year(orderdate);



---------------------------------------------------------------------------zusätzliche
---------------------------------------------------------------------------wichtige
---------------------------------------------------------------------------Informationen

																															--Verschachtelung geht nicht
select count(min(freight)) from orders;


							--Umgang mit NULLs	
							
				
							
use beispieldb

create table tab(sp1 int, sp2 int);

insert into tab values(3 ,4)
insert into tab values(3 ,7)
insert into tab values(3 ,5)
insert into tab values(3 ,null)

select sp1, sp2, sp1+sp2		--NULL ist nicht operabel
from tab;

select	sum(sp1),
		sum(sp2)				--Summe2 wird trotzdem berechnet
from tab;

drop table tab;


use northwind
										--Kontrollabfragen zu NULLs								

select	count(shippeddate), 
		count(*), 
      	count(*)-count(shippeddate),
		round(100.*(count(*)-count(shippeddate))/count(*),4) as Prozent_NULL,
		count(isnull(shippeddate,getdate())),
		max(shippeddate),
		max(isnull(shippeddate,getdate())),
		max(coalesce(shippeddate, getdate()))
from 	orders

		



