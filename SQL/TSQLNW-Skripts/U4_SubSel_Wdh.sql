
									/***	Produkte, die von derselben Kategorie sind,
											wie Produkt 37,
											aber von einem anderen Lieferanten		***/
select	productid,
		productname,
		unitprice,
		categoryid,
		supplierid
from	products
where	categoryid=(	select categoryid
						from products
						where productid=37)		
and supplierid<>(	select supplierid
					from products
					where productid=37)	

								/***	Produkte, die im Jahr 2010
										nicht bestellt wurden		***/				
select	productid,
		productname,
		unitprice
from products

where productid not in	(	select	distinct productid				--<>all
							from		[order details] od
							join		orders
							on			od.orderid=orders.orderid
							where	year(orderdate)=2010)	
									
					
								/***	alle die Kunden,
										deren Lieferaddresse in ihren Bestellungen
										mindestens einmal
										nicht gleich der Firmenadresse ist	***/																								

select	companyname,
		address,
		city
from	customers
where	address<>any	(	select	shipaddress
							from	orders
							where  customerid=customers.customerid)	
										
select	distinct
			companyname,
			address,
			city,
			shipaddress,
			shipcity
from		customers
join		orders
on			customers.customerid=orders.customerid
and		address<>shipaddress;


								/***	Äquivalent zur korrelierten Unterabfrage	***/
								
select	customerid,
			companyname,
			contactname,
			city,
			phone,
			(	select	count(*)
				from orders
				where customerid=customers.customerid)	as anzahl_bestellungen
from customers
where 10<(	select	count(*)
			from		orders
			where	customerid=customers.customerid);	
					
					
select	customers.customerid,
		companyname,
		contactname,
		city,
		phone,
		count(*) as anzahl_bestellungen
from customers
join	orders
on		customers.customerid=orders.customerid
group by	customers.customerid,
			companyname,
			contactname,
			city,
			phone
having count(*)>10;	


										
										
								/***	Einzeldaten aus Bestellung mit Gesamtbetrag	***/

select	orders.orderid,
		customerid,
		orderdate,
		productid,
		unitprice,
		quantity,
		discount,
		cast(unitprice*quantity*(1-discount )as decimal(10,2)) as linetotal
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
where	year(orderdate)=2010;	


select	orders.orderid,
		customerid,
		orderdate,
		productid,
		unitprice,
		quantity,
		discount,
		cast(unitprice*quantity*(1-discount )as decimal(10,2)) as linetotal,
		(	select	sum(cast(unitprice*quantity*(1-discount )as decimal(10,2)))
			from		[order details]
			where	orderid=orders.orderid) as ordertotal
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
where	year(orderdate)=2010;																											