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
select 	shipcountry,
		year(orderdate) as jahr,
		datepart(q, orderdate) as quartal,
		sum(unitprice*quantity*(1-discount)), 
		count(od.orderid)		as anzahl_bestellposten,
		count(distinct od.orderid)	as anzahl_bestellungen
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by	year(orderdate), 
			datepart(q, orderdate)
			
			
          

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




                 --with ROLLUP
                 --Ergebnis extra physisch speichern
                 --ABC-AB-A-NULLNULLNULL		
select 	shipcountry,
			year(orderdate) as jahr,
			datepart(q, orderdate) as quartal,
			sum(unitprice*quantity*(1-discount)), 
			count(od.orderid)		as anzahl_bestellposten--,
		--count(distinct od.orderid)	as anzahl_bestellungen
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

group by  rollup(	shipcountry,			--ab 2008
					year(orderdate), 
					datepart(q, orderdate));
					
					
					
					
select 	shipcountry,
        year(orderdate) as jahr,
        datepart(q, orderdate) as quartal,
        sum(unitprice*quantity*(1-discount)), 
		count(od.orderid)		as anzahl_bestellposten,
		count(distinct od.orderid)	as anzahl_bestellungen
from [order details] od
join orders o
on o.orderid=od.orderid

group by  rollup(	shipcountry,			--ab 2008
					(year(orderdate), datepart(q, orderdate)));					





                                        --with CUBE
                                        --Ergebnis extra physisch speichern
                                        --ABC-AB-A-AC-BC-B-C		
select 	shipcountry,
        year(orderdate) as jahr,
        datepart(q, orderdate) as quartal,
        sum(unitprice*quantity*(1-discount)) summe, 
		count(od.orderid)		as anzahl_bestellposten

--	count(distinct od.orderid)	as anzahl_bestellungen
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by  shipcountry,
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

group by  cube(	shipcountry,				--ab2008
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
							(ShipCountry, YEAR(OrderDate)),
							ShipCountry,
							YEAR(OrderDate)	);
											



