/********************************************************************************************
	Wiederholung Mengenoperatoren
	UNION, UNION ALL, INTERSECT, EXCEPT
********************************************************************************************/


										--einfaches Beispiel:
										--Länder, in die im Juli 2021
										--bzw. im August 2021 geliefert wurde

select distinct shipcountry from orders;						--21 Zeilen
																					--alle Länder in der Spalte SHIPCOUNTRY



										--zuerst separat und mit DISTINCT

select	distinct shipcountry											--13 Zeilen
from	orders
where	orderdate between '1.7.2021' and '31.7.2021';


select	distinct shipcountry											--17 Zeilen
from	orders
where	orderdate between '1.8.2021' and '31.8.2021';



select	shipcountry														--19 Zeilen
from		orders																--(ohne DISTINCT!!!)
where	orderdate between '1.7.2021' and '31.7.2021'
union
select	shipcountry
from		orders
where	orderdate between '1.8.2021' and '31.8.2021';



select	shipcountry														--66 Zeilen
from		orders																--(ohne DISTINCT)
where	orderdate between '1.7.2021' and '31.7.2021'
union all
select	shipcountry														--jedes Land in der Anzahl der Bestellungen
from		orders
where	orderdate between '1.8.2021' and '31.8.2021'
order by 1;


select	distinct shipcountry											--30 Zeilen
from		orders														--(mit DISTINCT)
where	orderdate between '1.7.2021' and '31.7.2021'
union all
select	distinct shipcountry											--Land zweimal, wenn es in beiden Monaten vorkommt
from		orders														--Land einmal, wenn es in einem von beiden Monaten vorkommt
where	orderdate between '1.8.2021' and '31.8.2021'
order by 1;


select	shipcountry														--11 Zeilen
from		orders														--Länder, die in beiden Monaten vorkommen
where	orderdate between '1.7.2021' and '31.7.2021'
intersect
select	shipcountry
from		orders
where	orderdate between '1.8.2021' and '31.8.2021';



select	shipcountry														--2 Zeilen
from		orders														--Länder, die nur im Juli vorkommen
where	orderdate between '1.7.2021' and '31.7.2021'
except
select	shipcountry
from		orders
where	orderdate between '1.8.2021' and '31.8.2021';



select	shipcountry														--6 Zeilen
from		orders														--Länder, die nur im August vorkommen
where	orderdate between '1.8.2021' and '31.8.2021'
except
select	shipcountry
from		orders
where	orderdate between '1.7.2021' and '31.7.2021';



													--statt OUTER JOIN
													--Produkte, die 2022 verkauft wurden
													--mit Bestellvolumen und Bestellhäufigkeit

													--zuerst die Abfragen einzeln vorführen,
													--dann mit UNION

select	productname,														--76 Zeilen
		sum(quantity)				as bestellvolumen, 
		count(distinct o.orderid)	as anzahl_bestellungen
from	products p
join	[order details] od
on		p.productid=od.productid
join	orders o
on		o.orderid=od.orderid
where	datepart(year, orderdate)=2022
group by productname

union

select	productname, 0, 0											--1 Zeile
from	products
where	productid not in(	select	productid
							from		[order details] od
							join		orders o
							on			o.orderid=od.orderid
							where	datepart(year, orderdate)=2022)
order by anzahl_bestellungen


/**************************************************************
select	productname,														--76 Zeilen
		sum(quantity)				as bestellvolumen, 
		count(distinct o.orderid)	as anzahl_bestellungen
from	products p
left join	[order details] od
on		p.productid=od.productid

left join	orders o
on		o.orderid=od.orderid
and		datepart(year, orderdate)=2022
group by productname
order by anzahl_bestellungen
***************************************************************/




