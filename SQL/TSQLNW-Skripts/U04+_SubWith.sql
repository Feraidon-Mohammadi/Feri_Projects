USE Northwind;
GO



/******			Problem bei Abfragen mit Aggregatfunktionen:
				man ist durch die Logik auf die Spalten in der GROUP BY-Klausel eingeschränkt	***/
select	o.orderid,
		orderdate,
		c.customerid,
		companyname,
		contactname,
		city,
		phone,
		country,
		count(*) as order_cnt,
		sum(cast(unitprice*quantity*(1-discount) as decimal(10,2)))+freight as order_amt
from customers c
join	orders o
on		c.customerid=o.customerid
join	[order details] od
on		od.orderid=o.orderid
group by	o.orderid,				--liefert die Umsatzsumme für eine Bestellung
			orderdate,				--die Hinzunahme von Product-Information würde sie 
			c.customerid,			--Summe verändern
			companyname,
			contactname,
			city,
			phone,
			country,
			freight;

									--Vereinbarkeit von Detailinformation und
									--Zusammenfassungsinformation

									--Variante 1:	Korrelierte Unterabfragen
									--				(einfache eingebettete gehen auch)
select	o.orderid,
		orderdate,
		c.customerid,				--Abfragepläne!!!
		companyname,
		contactname,
		city,
		phone,
		productid,
		discount,
		(	select	count(*)
			from	[order details]
			where	orderid= o.orderid)						as order_cnt,
		(	select	sum(cast(unitprice*quantity*(1-discount) as decimal(10,2)))
			from	[order details]
			where	orderid=o.OrderID)						as order_amt,
		(	select	sum(cast(unitprice*quantity*(1-discount) as decimal(10,2)))
			from	[order details]
			where	orderid=o.OrderID) + freight			as incl_freight
from customers c
join	orders o
on		c.customerid=o.customerid
join [order details] od
on		o.orderid=od.orderid;



									--Variante 2:	Subselect in der FROM-Klausel
									--				(Join erforderlich)
select	o.orderid,
		customerid,
		orderdate,
		ord_amt,
		freight,
		ord_amt+freight as to_pay
from	orders o
		join(	select	orders.orderid, 
				convert(money, SUM(unitprice*quantity*(1-discount))) as ord_amt
				from	Orders
				join	[Order Details] od
				on		Orders.OrderID=od.OrderID
				group by Orders.OrderID	)	sumsub
on		o.OrderID=sumsub.OrderID
where	YEAR(OrderDate)=2010;





					--Subselect
					--in der WITH-Klausel	-->eine Art Zwischenergebnis
					--(	beliebige SELECTs 
					--	auf das Subselect sind mgl)

with cte_cube_analyse
as(
	select 	shipcountry,
			year(orderdate)							as rp_year,
			datepart(q, orderdate)					as rp_quarter,
			sum(unitprice*quantity*(1-discount))	as ord_amt, 
			count(od.orderid)						as od_cnt,

			count(distinct od.orderid)				as order_cnt
	from	[order details] od
	join	orders o
	on		o.orderid=od.orderid

	group by cube(	shipcountry,
					year(orderdate), 
					datepart(q, orderdate))
)
select	shipcountry, rp_year, ord_amt, order_cnt
from	cte_cube_analyse
where	rp_year=2010 
and		rp_quarter is null;




with cte_order_join
as(
	select 	o.orderid,
			shipcountry,
			orderdate,
			cast(unitprice*quantity*(1-discount) as decimal(20,2)) as linetotal 
	from	[order details] od
	join	orders o
	on		o.orderid=od.orderid
)
, cte_cube
as(
	select 	shipcountry,
			year(orderdate)				as rp_year,
			datepart(q, orderdate)		as rp_quarter,
			sum(linetotal)				as ord_amt, 
			count(orderid)			as od_cnt,
			count(distinct orderid)	as order_cnt
	from	cte_order_join
	group by cube(	shipcountry,
					year(orderdate), 
					datepart(q, orderdate))
)
select shipcountry, rp_year, ord_amt, order_cnt
from	cte_cube
where rp_year=2010 
and rp_quarter is null;
											--beim Abfrageplan schneidet die Variante
											--ohne WITH(s.u.) besser ab

select 	shipcountry,
		year(orderdate)							as rp_year,
		datepart(q, orderdate)					as rp_quarter,
		sum(unitprice*quantity*(1-discount))	as ord_amt, 
		count(od.orderid)						as od_cnt,
		count(distinct od.orderid)				as order_cnt
from	[order details] od
join	orders o
on		o.orderid=od.orderid
where	year(orderdate)=2010

group by cube(	shipcountry,
				year(orderdate), 
				datepart(q, orderdate))
having		datepart(q, orderdate) is null
and			year(orderdate) is not null;





														--Hierarchische Abfrage
														--durch Rekursion

WITH DirectReports (ManagerID, EmployeeID, Title, LastName, FirstName, Level)
AS
(
-- Anchor member definition
    SELECT ReportsTo, EmployeeID, Title, LastName, FirstName, 0 AS Level
    FROM Employees
    WHERE ReportsTo IS NULL
    UNION ALL
-- Recursive member definition
    SELECT e.ReportsTo, e.EmployeeID, e.Title, e.LastName, e.FirstName, Level + 1
    FROM Employees AS e
	JOIN DirectReports AS d
        ON e.ReportsTo = d.EmployeeID
)
-- Statement that executes the CTE
SELECT ManagerID, EmployeeID, Title, LastName, FirstName, Level
FROM DirectReports
--OPTION (maxrecursion n)
;

GO 


----------------------------------------Performance-Vergleiche------------------------------

										--Vergleich:	temporäre Tabelle
										--Erzeugen einer temporären Tabelle
select 	shipcountry,
		year(orderdate)							as rp_year,
		datepart(q, orderdate)					as rp_quarter,
		sum(unitprice*quantity*(1-discount))	as ord_amt, 
		count(od.orderid)						as od_cnt,
		count(distinct od.orderid)				as order_cnt

into	#cube_analyse					-------------INTO

from	[order details] od
join	orders o
on		o.orderid=od.orderid
group by cube(	shipcountry,
				year(orderdate), 
				datepart(q, orderdate));


												--Abfragen der temporären Tabelle
select	shipcountry, rp_year, ord_amt, order_cnt
from	#cube_analyse
where	rp_year=2010 
and		rp_quarter is null;

												--Abfragen permanenter Tabellen mit WITH

												--laut Vergleich der Abfragepläne ist
												--das Abfragen temporärer Tabellen 
												--um Größenordnungen günstiger als Abfrage mit WITH
with cte_cube_analyse
as(
	select 	shipcountry,
			year(orderdate)							as rp_year,
			datepart(q, orderdate)					as rp_quarter,
			sum(unitprice*quantity*(1-discount))	as ord_amt, 
			count(od.orderid)						as od_cnt,

			count(distinct od.orderid)				as order_cnt
	from	[order details] od
	join	orders o
	on		o.orderid=od.orderid

	group by cube(	shipcountry,
					year(orderdate), 
					datepart(q, orderdate))
)
select	shipcountry, rp_year, ord_amt, order_cnt
from	cte_cube_analyse
where	rp_year=2010 
and		rp_quarter is null;


											--nun noch der Vergleich mit einer Variable 
											--vom Datentyp TABLE

declare @cube_analyse table(	shipcountry		varchar(50),
								rp_year			smallint,
								rp_quarter		tinyint,
								ord_amt			decimal(20,2),
								od_cnt			smallint,
								order_cnt		smallint);	

insert into @cube_analyse	select 	shipcountry,
									year(orderdate),
									datepart(q, orderdate),
									sum(unitprice*quantity*(1-discount)), 
									count(od.orderid),
									count(distinct od.orderid)
							from	[order details] od
							join	orders o
							on		o.orderid=od.orderid
							group by cube(	shipcountry,
											year(orderdate), 
											datepart(q, orderdate));

select	shipcountry, rp_year, ord_amt, order_cnt
from	@cube_analyse
where	rp_year=2010 
and		rp_quarter is null;


select	shipcountry, rp_year, ord_amt, order_cnt
from	#cube_analyse
where	rp_year=2010 
and		rp_quarter is null;


----------------------------------------------------------drop table #cube_analyse


												--zum Schluss noch der Vergleich 
												--mit Abfrage auf View
create view v_cube_analyse
as
select 	shipcountry,
		year(orderdate)							as rp_year,
		datepart(q, orderdate)					as rp_quarter,
		sum(unitprice*quantity*(1-discount))	as ord_amt, 
		count(od.orderid)						as od_cnt,
		count(distinct od.orderid)				as order_cnt
		from	[order details] od
		join	orders o
		on		o.orderid=od.orderid
		group by cube(	shipcountry,
						year(orderdate), 
						datepart(q, orderdate));

exec sp_help 'v_cube_analyse';

												--Zugriff auf View
select	shipcountry, rp_year, ord_amt, order_cnt
from	v_cube_analyse
where	rp_year=2010 
and		rp_quarter is null;
												--Beim Vergleich der Abfragepläne
												--ist die temporäre Tabelle überdeutlich
												--im Vorteil
												--weil beim View die Ergebnisdaten
												--erst beim Aufruf erzeugt werden
												--bei temporären Tabellen liegen sie vor


												--Zugriff auf temporäre Tabelle
select	shipcountry, rp_year, ord_amt, order_cnt
from	#cube_analyse
where	rp_year=2010 
and		rp_quarter is null;
	










                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  