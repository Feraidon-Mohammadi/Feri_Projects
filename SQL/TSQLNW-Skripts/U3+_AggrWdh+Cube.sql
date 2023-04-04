use northwind;
go



select productid, quantity
from		[order details]
order by productid;


select	orderid,
			productid,
			quantity
from	[Order Details]
order by 2;	


select	sum(quantity) as summe,
		avg(quantity) as durchschnitt
from	[order details];


select	productid,
		sum(quantity) as summe,
		avg(quantity) as durchschnitt,
		count(*) as wie_oft
from	[order details]
group by	productid
order by	productid;


select	productid,
			discount,
			sum(quantity) as summe,
			avg(quantity) as durchschnitt,
			count(*) as wie_oft
from	[order details]
group by	productid,
			discount
order by	productid;


select	productid,
			discount,
			sum(quantity) as summe,
			avg(quantity) as durchschnitt,
			count(*) as wie_oft
from	[order details]
group by	productid,
				discount
having		count(*)<5
order by	productid;


select	productid,
			discount,
			sum(quantity) as summe,
			avg(quantity) as durchschnitt,
			count(*) as wie_oft
from	[order details]
group by	productid,
				discount
having		count(*)<5
and			avg(quantity)<25				
order by	productid;



---------------------------------------------------------------------------------Neues Beispiel
select 	datepart(q, orderdate) as quartal,
			
		sum(unitprice*quantity*(1-discount)), 
		count(od.orderid)		as anzahl_bestellposten,
		count(distinct od.orderid)	as anzahl_bestellungen
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by	datepart(q, orderdate) 
order by 1,2                                                    
	



			--Die Anzahl der Einzelausdrücke in der SELECT-Klausel
			--darf nicht größer sein, als die Anzhal der Einzelaus-
			--drücke in der GROUP BY-Klausel

select 	--shipcountry,
			year(orderdate) as jahr,
			datepart(q, orderdate) as quartal,

			sum(unitprice*quantity*(1-discount)), 
			count(od.orderid)		as anzahl_bestellposten,
			count(distinct od.orderid)	as anzahl_bestellungen
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by	year(orderdate), 
			datepart(q, orderdate);
			
			
          

              --mit der zusätzlichen Spalte
              --im GROUP BY
              --werden aber die Ergebnisse
              --der Aggregatfunktionen andere
select 	shipcountry,
		year(orderdate) as jahr,
		datepart(q, orderdate) as quartal,

		sum(unitprice*quantity*(1-discount)), 
		count(od.orderid)		as anzahl_bestellposten,
		count(distinct od.orderid)	as anzahl_bestellungen
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by	shipcountry,
			year(orderdate), 
			datepart(q, orderdate)   
order by 2,3    


              --Filtern nach Zusammenfassungsergebnissen
select 	shipcountry,
			year(orderdate) as jahr,
			datepart(q, orderdate) as quartal,

			sum(unitprice*quantity*(1-discount)), 
			count(od.orderid)		as anzahl_bestellposten,
			count(distinct od.orderid)	as anzahl_bestellungen
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by	shipcountry,
				year(orderdate), 
				datepart(q, orderdate)  

having 		sum(unitprice*quantity*(1-discount))<1000
 
order by 2,3       




                 --with ROLLUP
                 --Ergebnis extra physisch speichern
                 --ABC-AB-A-NULLNULLNULL		
select 	shipcountry,
			year(orderdate) as jahr,
			datepart(q, orderdate) as quartal,

			sum(unitprice*quantity*(1-discount)), 
			count(od.orderid)		as anzahl_bestellposten,
			count(distinct od.orderid)	as anzahl_bestellungen
from [order details] od
join orders o
on o.orderid=od.orderid

group by  shipcountry,
          year(orderdate), 
          datepart(q, orderdate)
with rollup									--bis 2005




select 	shipcountry,
			year(orderdate) as jahr,
			datepart(q, orderdate) as quartal,

			sum(unitprice*quantity*(1-discount)), 
			count(od.orderid)		as anzahl_bestellposten,
			count(distinct od.orderid)	as anzahl_bestellungen
from [order details] od
join orders o
on o.orderid=od.orderid

group by  rollup(	shipcountry,			--ab 2020
					year(orderdate), 
					datepart(q, orderdate));
					
					
					
					
select 	shipcountry,
			year(orderdate) as jahr,
			datepart(q, orderdate) as quartal,

			sum(unitprice*quantity*(1-discount)), 
			count(od.orderid)		as anzahl_bestellposten,
			count(distinct od.orderid)	as anzahl_bestellungen
from		[order details] od
join		orders o
on			o.orderid=od.orderid

group by  rollup(	shipcountry,			--ab 2020
					(year(orderdate), datepart(q, orderdate))
						);					





                                        --with CUBE
                                        --Ergebnis extra physisch speichern
                                        --ABC-AB-A-AC-BC-B-C		
select 	shipcountry,
			year(orderdate) as jahr,
			datepart(q, orderdate) as quartal,

			sum(unitprice*quantity*(1-discount)) summe, 
			count(od.orderid)		as anzahl_bestellposten,
			count(distinct od.orderid)	as anzahl_bestellungen
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by	shipcountry,
			year(orderdate), 
			datepart(q, orderdate)
with cube									--bis 2005							



select 	shipcountry,
			year(orderdate) as jahr,
			datepart(q, orderdate) as quartal,

			sum(unitprice*quantity*(1-discount)), 
			count(od.orderid)		as anzahl_bestellposten,
			count(distinct od.orderid)	as anzahl_bestellungen
from [order details] od
join orders o
on o.orderid=od.orderid

group by  cube(	shipcountry,				--ab2020
				year(orderdate), 
				datepart(q, orderdate));



select 	shipcountry,
			year(orderdate) as jahr,
			datepart(q, orderdate) as quartal,

			sum(unitprice*quantity*(1-discount)) summe, 
			count(od.orderid)		as anzahl_bestellposten,
			count(distinct od.orderid)	as anzahl_bestellungen
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by  grouping sets(	(shipcountry, year(orderdate), datepart(q, orderdate)),
							(ShipCountry, year(OrderDate)),
							ShipCountry,
							year(OrderDate)	);
											



