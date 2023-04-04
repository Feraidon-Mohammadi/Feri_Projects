use northwind;
go

select	orderid,
			productid,
			quantity
from	[Order Details]
order by 2;		


select		SUM(quantity) as gesamtvolumen,
			COUNT(orderid) as bestellanzahl
from	[Order Details]		
;


select	productid,
			SUM(quantity) as gesamtvolumen,
			COUNT(orderid) as bestellanzahl
from	[Order Details]		
group by	ProductID
order by 1;


select	productid,
			YEAR(orderdate) as jahr,
			SUM(quantity) as gesamtvolumen,
			COUNT(o.orderid) as bestellanzahl
from		[Order Details] od
join		Orders o
on			od.OrderID=o.OrderID		
group by	ProductID,
			YEAR(OrderDate)
order by 1,2;


select	productname,
			YEAR(orderdate) as jahr,
			SUM(quantity) as gesamtvolumen,
			COUNT(o.orderid) as bestellanzahl
from		[Order Details] od
join		Orders o
on			od.OrderID=o.OrderID	
join		Products p
on			od.ProductID=p.ProductID	
group by	ProductName,
			YEAR(OrderDate)
order by jahr, gesamtvolumen;


select	productname,
			YEAR(orderdate) as jahr,
			SUM(quantity) as gesamtvolumen,
			COUNT(o.orderid) as bestellanzahl
from		[Order Details] od
join		Orders o
on			od.OrderID=o.OrderID	
join		Products p
on			od.ProductID=p.ProductID	
group by	ProductName,
			YEAR(OrderDate)
having		SUM(quantity)<=50			
order by jahr, gesamtvolumen;