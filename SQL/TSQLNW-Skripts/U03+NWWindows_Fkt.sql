		--Order Details mit Zeilensumme und Bestellsumme
		--per Windows-Funktion
		--ohne GROUP BY

USE NORTHWIND;
GO



select * from [order details];

												--order details
												--mit Zeilengesamt
select	*,
		cast(unitprice*quantity*(1-discount) as decimal(10,2)) as linetotal
from	[order details];

												--Umsatzsumme
												--pro Bestellung
select	orderid,
		sum(unitprice*quantity*(1-discount) ) as ordertotal
from	[order details]
group by orderid;

												--CAST-SUM
select	orderid,
		cast(sum(unitprice*quantity*(1-discount) ) as decimal(10,2)) as ordertotal
from	[order details]
group by orderid;

												--SUM-CAST
select	orderid,
		sum(cast(unitprice*quantity*(1-discount) as decimal(10,2))) as ordertotal
from	[order details]
group by orderid;
---------------------------------------Dreifachausführung zum Vergleich der Abfragepläne

												--Einzeldaten und Summe
												--geht so leider nicht
												--nur mit korrelierter Unterabfrage oder GROUP BY
select	*,
		unitprice*quantity*(1-discount) as linetotal,
		sum(unitprice*quantity*(1-discount)) 
from [order details];

select	orderid,
		sum(unitprice*quantity*(1-discount)) 
from [order details]
group by orderid;

												--mit OVER BY(Windows-Funktion) gehts
select	*,
		unitprice*quantity*(1-discount) as linetotal,
		sum(cast(unitprice*quantity*(1-discount) as decimal(10,2))) over(partition by  orderid) as ordertotal
from [order details];


												--auch mit Gesamtsumme
select	*,
		unitprice*quantity*(1-discount) as linetotal,
		sum(cast(unitprice*quantity*(1-discount) as decimal(10,2))) over(partition by  orderid) as ordertotal,
		sum(cast(unitprice*quantity*(1-discount) as decimal(10,2))) over() as totaltotal
from [order details];



												--und mit Summierungen über 
												--verschiedene Gruppenkriterien
select	o.orderid,
		orderdate,
		customerid,
		shipcountry,
		cast(unitprice*quantity*(1-discount) as decimal(10,2)) as linetotal,
		sum(cast(unitprice*quantity*(1-discount) as decimal(10,2))) over(partition by  od.orderid) as ordertotal,
		sum(cast(unitprice*quantity*(1-discount) as decimal(10,2))) over() as totaltotal,
		sum(cast(unitprice*quantity*(1-discount) as decimal(10,2))) over(partition by  shipcountry) as countrytotal,
		sum(cast(unitprice*quantity*(1-discount) as decimal(10,2))) over(partition by  year(orderdate)) as yeartotal,
		sum(cast(unitprice*quantity*(1-discount) as decimal(10,2))) over(partition by  shipcountry, year(orderdate)) as countryyeartotal
from	[order details] od
join	orders o
on		od.orderid=o.orderid;


												--Wechsel des Beispiels
												--SUM(quantity) statt SUM(linetotal)
select	o.orderid,
		orderdate,
		year(orderdate) as rp_year,
		customerid,
		shipcountry,
		productname,
		quantity,
		sum(quantity) over(partition by p.productid) as prod_qty,
		sum(quantity) over(partition by p.productid, year(orderdate)) as prod_year_qty,
		sum(quantity) over(partition by p.productid, shipcountry) as prod_country_qty,
		sum(quantity) over(partition by p.productid, shipcountry, year(orderdate)) as prod_country_year_qty
from	[order details] od
join	orders o
on		o.orderid=od.orderid
join	products p
on		p.productid=od.productid;


												--natürlich gehen auch andere Aggregatfunktionen
select	o.orderid,
		orderdate,
		year(orderdate) as rp_year,
		customerid,
		shipcountry,
		productname,
		quantity,
		sum(quantity) over(partition by p.productid, year(orderdate)) as prod_year_qty,
		avg(quantity) over(partition by p.productid, year(orderdate)) as prod_year_avg,
		
		min(quantity) over(partition by p.productid, year(orderdate)) as prod_year_min,
		max(quantity) over(partition by p.productid, year(orderdate)) as prod_year_max
from	[order details] od
join	orders o
on		o.orderid=od.orderid
join	products p
on		p.productid=od.productid;


												--mit ORDER BY im INPUT
												--erhält man laufende Summen 
select	o.orderid,
		orderdate,
		year(orderdate) as rp_year,
		month(orderdate) as rp_month,
		customerid,
		shipcountry,
		productname,
		quantity,
		sum(quantity) over(partition by p.productid order by orderdate) as daily_running_prod_qty,
		sum(quantity) over(partition by p.productid order by year(orderdate), month(orderdate)) as monthly_running_prod_qty
from	[order details] od
join	orders o
on		o.orderid=od.orderid
join	products p
on		p.productid=od.productid
order by p.productid, orderdate;


												--täglich oder monatlich
select	o.orderid,
		orderdate,
		year(orderdate) as rp_year,
		month(orderdate) as rp_month,
		customerid,
		shipcountry,
		productname,
		quantity,
		sum(quantity) over(partition by p.productid order by orderdate) as daily_running_prod_qty,
		sum(quantity) over(partition by p.productid order by year(orderdate), month(orderdate)) as monthly_running_prod_qty
from	[order details] od
join	orders o
on		o.orderid=od.orderid
join	products p
on		p.productid=od.productid
order by p.productid, orderdate;


											--hier die eigentlichen Datenfenster
											--die vorhergenden 5 Tage
											--die nachfolgenden 5 Tage
											--5 Tage vorher und nachher
select	o.orderid,
		orderdate,
		year(orderdate) as rp_year,
		month(orderdate) as rp_month,
		customerid,
		shipcountry,
		productname,
		quantity,
		sum(quantity) over(partition by p.productid order by orderdate) as daily_running_prod_qty,
		sum(quantity) over(	partition by p.productid order by orderdate
							rows between  5 preceding and current row) as window5_prec,
		sum(quantity) over(	partition by p.productid order by orderdate
							rows between current row and 5 following) as window5_follow,
		sum(quantity) over(	partition by p.productid order by orderdate
							rows between 5 preceding and 5 following) as window5_prec_and_follow
from	[order details] od
join	orders o
on		o.orderid=od.orderid
join	products p
on		p.productid=od.productid
order by p.productid, orderdate;










											--und noch etwas Neues
											--zuerst ein View,
											--dass die Basisdaten bereitstellt

create view v_month_qty
as
select	productname,
		year(orderdate) as rp_year,
		month(orderdate) as rp_month,
		sum(quantity)as monthly_prod_qty
from	[order details] od
join	orders o
on		o.orderid=od.orderid
join	products p
on		p.productid=od.productid
group by	productname,
			year(orderdate),
			month(orderdate);

											--neben der monatlichen Bestellmenge
											--kann mit LAG die vom Vormonat
											--und mit LEAD die vom Folgemonat ausgegeben werden
											--oder auch die 3 Monate zuvor bzw. danach
											--3.Parameter(NULL) ist der Wert, falls es keinen
											--führenden oder nachfolgenden gibt

select	productname, rp_year, rp_month,
		monthly_prod_qty,
		lag(monthly_prod_qty,1,0) over(order by productname, rp_year, rp_month) as prec_month_qty,
		lead(monthly_prod_qty,1,null) over(order by productname,rp_year, rp_month) as follow_month_qty,
		lag(monthly_prod_qty,3,0) over(order by productname,rp_year, rp_month) as prec_3month_qty,
		lead(monthly_prod_qty,3,null) over(order by productname,rp_year, rp_month) as follow_3month_qty
from	v_month_qty
order by productname;


	



	
		
			