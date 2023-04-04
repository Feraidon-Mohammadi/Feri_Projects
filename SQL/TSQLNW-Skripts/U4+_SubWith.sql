USE Northwind;
GO

					--Subselect
					--in der FROM-Klausel
					--(Join erforderlich)
select	o.orderid,
		customerid,
		orderdate,
		summe,
		freight,
		summe+freight as gesamt
from	orders o
		join(	select	orders.orderid, 
				convert(money, SUM(unitprice*quantity*(1-discount))) as summe
				from	Orders
				join	[Order Details] od
				on		Orders.OrderID=od.OrderID
				group by Orders.OrderID	)	sumsub
on		o.OrderID=sumsub.OrderID
where	YEAR(OrderDate)=2010;



					--Subselect
					--in der WITH-Klausel
					--(	beliebige SELECTs 
					--	auf das Subselect sind mgl)

with cube_analyse
as(
	select 	shipcountry,
			year(orderdate) as jahr,
			datepart(q, orderdate) as quartal,
			sum(unitprice*quantity*(1-discount)) summe, 
			count(od.orderid)		as anzahl_bestellposten,

			count(distinct od.orderid)	as anzahl_bestellungen
	from	[order details] od
	join	orders o
	on		o.orderid=od.orderid

	group by cube(	shipcountry,
					year(orderdate), 
					datepart(q, orderdate))
)
select shipcountry, jahr, summe, anzahl_bestellungen
from	cube_analyse
where jahr=2010 
and quartal is null;




						--Hierarchische Abfrage
						--durch Rekursion

select employeeid, lastname, reportsto
from employees;


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
FROM DirectReports;

GO                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       