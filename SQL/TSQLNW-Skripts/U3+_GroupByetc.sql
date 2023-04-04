--select orders.orderid,
--		customerid,
--		orderdate,
--		shipcity,
--		[order details].*
--from	orders
--join	[order details]
--on		orders.orderid=[order details].orderid

--									--Umsatz pro Bestellung
--									--(ohne Details)

--select	orders.orderid,
--		sum(quantity*unitprice*(1-discount)) as gesamtsumme
--from	orders
--join	[order details]
--on		orders.orderid=[order details].orderid	
--group by orders.orderid
--order by 1	


--									--(mit Details)									
--select	orders.orderid,
--		customerid,
--		sum(quantity*unitprice*(1-discount)) as gesamtsumme
--from	orders
--join	[order details]
--on		orders.orderid=[order details].orderid	
--group by orders.orderid,
--		customerid
--order by 1

--									--(mit Details)
--select	orders.orderid,
--		customerid,
--		orderdate,
--		shipcity,
--		sum(quantity*unitprice*(1-discount)) as gesamtsumme
--from		orders
--join		[order details]
--on			orders.orderid=[order details].orderid	
--group by orders.orderid,
--		customerid,
--		orderdate,
--		shipcity
--order by 1	

									
									
									--Umsatz pro Kunden
									--mit CustomerID
select	customerid,
		sum(quantity*unitprice*(1-discount)) as gesamtsumme
from		orders
join		[order details]
on			orders.orderid=[order details].orderid	
group by customerid
order by 2 desc		

									--Umsatz pro Kunden
									--mit Companyname
select	companyname,
		sum(quantity*unitprice*(1-discount)) as gesamtsumme
from		orders
join		[order details]
on			orders.orderid=[order details].orderid
join		customers
on			customers.customerid=orders.customerid	
group by companyname
order by 2 desc	


									--Umsatz pro Jahr
									--und Kunde
select	year(orderdate) as jahr,
		companyname,
		sum(quantity*unitprice*(1-discount)) as gesamtsumme
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
join	customers
on		customers.customerid=orders.customerid	
group by year(orderdate),companyname
order by 3 desc


									--Umsatz pro City, Jahr
									--und Kunde
select	city,
		year(orderdate) as jahr,
		companyname,
		sum(quantity*unitprice*(1-discount)) as gesamtsumme
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
join	customers
on		customers.customerid=orders.customerid	
group by city, year(orderdate),companyname
order by 1,2	

									--Umsatz pro City, Jahr
									--und Kunde
									--mit ROLLUP(SQLServer2005)
									
									--erzeugt folgende Gruppierungsvarianten
									--ABC--AB--A--NULLNULLNULL	
select	city,
		year(orderdate) as jahr,
		companyname,
		sum(quantity*unitprice*(1-discount)) as gesamtsumme
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
join	customers
on		customers.customerid=orders.customerid	
group by city, year(orderdate),companyname
with rollup	


									--Umsatz pro City, Jahr
									--und Kunde
									--mit ROLLUP(SQLServer2008, Oracle)
select	city,
		year(orderdate) as jahr,
		companyname,
		sum(quantity*unitprice*(1-discount)) as gesamtsumme
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
join	customers
on		customers.customerid=orders.customerid	
group by rollup (	city, 
					year(orderdate),
					companyname)
							

									--Umsatz pro City, Jahr
									--und Kunde
									--mit CUBE(SQLServer2005)
									
									--erzeugt alle Gruppierungsvarianten
                                    --ABC--AB--A--AC--BC--B--C--NULLNULLNULL																			
select	city,
		year(orderdate) as jahr,
		companyname,
		sum(quantity*unitprice*(1-discount)) as gesamtsumme
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
join	customers
on		customers.customerid=orders.customerid	
group by city, year(orderdate),companyname
with cube	


									--Umsatz pro City, Jahr
									--und Kunde
									--mit CUBE(SQLServer2008, Oracle)
select	city,
		year(orderdate) as jahr,
		companyname,
		sum(quantity*unitprice*(1-discount)) as gesamtsumme
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
join	customers
on		customers.customerid=orders.customerid	
group by cube( (city, year(orderdate)),companyname);


									--Umsatz pro City, Jahr
									--und Kunde
									--mit GROUPING SETS
									--(SQLServer2008, Oracle)
select	city,
		year(orderdate) as jahr,
		companyname,
		sum(quantity*unitprice*(1-discount)) as gesamtsumme
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
join	customers
on		customers.customerid=orders.customerid	
group by grouping sets(	city,
						companyname,
						(city, year(orderdate)),
						(companyname, year(orderdate))
									);								
							
	