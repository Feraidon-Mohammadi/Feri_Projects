										--einfaches Beispiel
select	productname,
		YEAR(orderdate) as jahr,
		SUM(quantity) as gesamtvolumen
from		[Order Details] od
join		Orders o
on			od.OrderID=o.OrderID	
join		Products p
on			od.ProductID=p.ProductID	
group by	ProductName,
			YEAR(OrderDate)
order by jahr, gesamtvolumen;


select	productname,
		[2008],
		[2009],
		[2010]
from
(		select	productname,
				YEAR(orderdate) as jahr,
				quantity
		from		[Order Details] od
		join		Orders o
		on			od.OrderID=o.OrderID	
		join		Products p
		on			od.ProductID=p.ProductID
) as prodorder	
pivot
(	sum(quantity) for jahr in([2008], [2009], [2010])) as pvt;






										--nicht so einfaches Beispiel

select 	shipcountry,
		year(orderdate) as jahr,
		datepart(q, orderdate) as quartal,
		sum(unitprice*quantity*(1-discount))
from	[order details] od
join	orders o
on		o.orderid=od.orderid

group by	shipcountry,
				year(orderdate), 
				datepart(q, orderdate);
				
				
				
				
				
				
select	jahr,
			quartal,
			Argentina, 
			Brazil, 
			Venezuela, 
			Mexico
																			--into analyse.dbo.pvt_umsatz_latino			
from							
(select		shipcountry,
			year(orderdate) as jahr,
			datepart(q, orderdate) as quartal,
			convert(money, unitprice*quantity*(1-discount)) as umsatz
from	[order details] od
join	orders o
on		o.orderid=od.orderid)	p
pivot
(	sum(umsatz)
	for shipcountry in (Argentina, Brazil, Venezuela, Mexico) )as pvt
order by jahr, quartal;



select * from analyse.dbo.pvt_umsatz_latino;


select jahr, quartal, shipcountry, umsatz
from
(	select	jahr, quartal, Argentina, Brazil, Mexico, Venezuela
	from analyse.dbo.pvt_umsatz_latino) p
unpivot
(	umsatz for shipcountry in(Argentina, Brazil, Mexico, Venezuela)) as upvt;	





