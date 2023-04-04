use northwind
go


select * from products;
select * from suppliers;

					--SQL92

select *				
from products inner join suppliers
on products.supplierid=suppliers.supplierid;

select *				
from products inner join suppliers
on supplierid=supplierid;


					--SQL89
select *				
from products, suppliers
where products.supplierid=suppliers.supplierid;


					--Kreuzprodukt
select *				
from Products, Suppliers;


					--Fehlermeldung
select *				
from products join suppliers;


					--reguläres Kreuzprodukt	
select *											
from products cross join suppliers;

					--Fehlermeldung
select *											
from products cross join suppliers
on	 products.supplierid=suppliers.supplierid;

					
					--Produkte des Lieferanten
					--mit der Nr. 12
select	productid, 
		productname, 
		unitprice, categoryid, unitsinstock,
		suppliers.supplierid, 
		companyname, 
		country, city, phone
from	products 
join	suppliers
on		products.supplierid=suppliers.supplierid
where	suppliers.supplierid=12;


select		productid,				--mit Tabellenalias
			productname, 
			unitprice, categoryid, unitsinstock,
			s.supplierid, 
			companyname, 
			country, city, phone
from	products as p 
join	suppliers as s
on		p.supplierid=s.supplierid
where	s.supplierid=12;


						--Produkte,
						--die bestellt wurden
						--(kommen in [Order Details] vor)

select	orderid, orderdate,					--Kreuzproduct
		productid,							--weil [Order Details] fehlt
		productname, quantityperunit
from	orders,	products
on	;	


select	orders.orderid, orderdate,			--so gehts mit SQL89
		products.productid, 
		productname, quantityperunit
from	orders,	products, [order details]
where	orders.orderid=[order details].orderid
and		products.productid=[order details].productid;					


						
select	o.orderid, orderdate,			--und so mit SQL92		
		p.productid, 
		productname, quantityperunit
from	products			p 
join	[order details] od
on		p.productid=od.productid
join	orders o
on		o.orderid=od.orderid;


						--mit berechnetem Feld
						--ohne Formatierung
select		o.orderid,
			p.productid, 
			productname, quantityperunit,
			od.unitprice, quantity, discount,
			od.unitprice*quantity*(1-discount) as linetotal
from		products p 
join		[order details] od
on			p.productid=od.productid
join		orders o
on			o.orderid=od.orderid
where		o.orderid between 10200 and 10299
order by o.orderid;

						--Formatierung
						--und die Tabelle Orders
						--mit Zeiteinschränkung 4/2021
select	o.orderid, 
		orderdate, customerid,
		p.productid, 
		productname, quantityperunit,
		od.unitprice, quantity, discount,
		convert(money, od.unitprice*quantity*(1-discount)) as linetotal
from	products p 
join	[order details] od
on		p.productid=od.productid
join	orders o
on		o.orderid=od.orderid
where	datepart(yyyy, orderdate)=2021		--Synonym:	year(orderdate)=2021
and		datepart(q, orderdate)=4
order by o.orderid;


						--Bestellungen
						--des Kunden 'HUNGO'

select	o.orderid, 
		orderdate, customerid,
		p.productid, 
		productname, quantityperunit,
		od.unitprice, quantity, discount,
		convert(money, od.unitprice*quantity*(1-discount)) as linetotal
from	products p 
join	[order details] od
on		p.productid=od.productid
join	orders o
on		o.orderid=od.orderid
where	customerid='HUNGO'
and		datepart(year, orderdate)=2021		
and		datepart(q, orderdate)=4	
order by o.orderid;


						--für die Rechnung der Bestellung
						--Nr. 10999
select	o.orderid,	orderdate, 
		c.customerid,
		companyname, 
		address, postalcode, city,
		p.productid, 
		productname, quantityperunit,
		od.unitprice, quantity, discount,
		convert(money, od.unitprice*quantity*(1-discount)) as linetotal
from	products p 
join	[order details] od
on		p.productid=od.productid
join	orders o
on		o.orderid=od.orderid
join	customers c
on		c.customerid=o.customerid
where	o.orderid=10999	






						--OUTER JOIN	

						--alle Kunden
select	customerid,
		companyname,
		country,
		city
from customers;


						--Kundendaten
						--und Bestelldaten
select 	customers.customerid,
		companyname,
		country,
		city,
		orderid
from		customers
inner join 	orders
on 			customers.customerid=orders.customerid
order by 1;


							
select 	customers.customerid,
		companyname,
		country,
		city						--orderid herausgenommen
from		customers
inner join 	orders
on 			customers.customerid=orders.customerid
order by	customers.customerid;


						--Kunden
						--die eine Bestellung haben

select  distinct 
		customers.customerid,
		companyname,
		country,
		city
from	customers
join 	orders
on 		customers.customerid=orders.customerid;


						--alle Kunden
						--auch die ohne Bestellung
select 	customers.customerid,
		companyname,
		country,
		city,
		orderid						--orderid wieder eingefügt
from 	customers left outer join 	orders
on 		customers.customerid=orders.customerid

order by orderid;


						--nur die Kunden 
						--ohne Bestellungen
select 	customers.customerid,
		companyname,
		country,
		city,
		orderid
from		customers
left join	orders
on 			customers.customerid=orders.customerid

where orderid is null;


						--nur die Kunden 
						--ohne Bestellungen
						--im Jahr 2022		FEHLANZEIGE
select 	customers.customerid,
		companyname,
		country,
		city,
		orderid
from		customers
left join	orders
on 			customers.customerid=orders.customerid
where	orderid is null
and		year(orderdate)=2022;				--****


						--nur die Kunden 
						--ohne Bestellungen
						--im Jahr 2022		RICHTIG
select 	customers.customerid,
		companyname,
		country,
		city,
		orderid
from		customers
left join	orders
on 			customers.customerid=orders.customerid
and			year(orderdate)=2022			--****

where orderid is null;


						--beim INNER JOIN
						--sind die Ergebnisse gleich

						--ON-AND
select 	customers.customerid,
		companyname,
		country,
		city,
		orderid
from		customers
inner join	orders
on 			customers.customerid=orders.customerid
and			year(orderdate)=2022

						--ON-WHERE
select 	customers.customerid,
			companyname,
			country,
			city,
			orderid
from		customers
inner join orders
on 		customers.customerid=orders.customerid
where	year(orderdate)=2022



						--beim OUTER JOIN
						--sind sie es nicht

						--ON-AND
select 	customers.customerid,					--280 Zeilen
			companyname,
			country,
			city,
			orderid
from		customers
left join orders
on 		customers.customerid=orders.customerid
and		year(orderdate)=2022
order by orderid;

						--ON-WHERE
select 	customers.customerid,					--270 Zeilen
			companyname,						--(wie INNER JOIN)
			country,
			city,
			orderid								--Grund:
from		customers							--Filter erfolgt auf eine
left join orders								--Spalte in Orders
on 		customers.customerid=orders.customerid	--die ist für die 
where	year(orderdate)=2022					--OUTER-Datensätze NULL
order by orderid;














						--die Outer Joins
							--left
							--right
							--full


						--Inner					
select	employeeid
		, lastname
		, e.city
		, customerid
		, companyname
		, c.city
from	employees e inner join customers c 
on		e.city=c.city


						--Left
select	employeeid
		, lastname
		, e.city
		, customerid
		, companyname
		, c.city
from	employees e left outer join customers c 
on		e.city=c.city

						--Left
						--mit WHERE-Klausel
select	employeeid
		, lastname
		, e.city
		, customerid
		, companyname
		, c.city
from	employees e left outer join customers c 
on		e.city=c.city
where	c.city is null


						--Right
select	employeeid
		, lastname
		, e.city
		, customerid
		, companyname
		, c.city
from	employees e right join customers c 
on		e.city=c.city


						--Full
select	employeeid
		, lastname
		, e.city
		, customerid
		, companyname
		, c.city
from	employees e full join customers c 
on		e.city=c.city



						--SQL89
						--geht immer irgendwie
select	o.orderid,	orderdate, 
		c.customerid,
		companyname, 
		address, postalcode, city,
		p.productid, 
		productname, quantityperunit,
		od.unitprice, quantity, discount,
		convert(money, od.unitprice*quantity*(1-discount)) as linetotal

from	products p, [order details] od, orders o, customers c
where		p.productid=od.productid
and			o.orderid=od.orderid
and			c.customerid=o.customerid

and			o.orderid=10999
;




						--SQL92
						--wie es nicht funktioniert
select	o.orderid,	orderdate, 
		c.customerid,
		companyname, 
		address, postalcode, city,
		p.productid, 
		productname, quantityperunit,
		od.unitprice, quantity, discount,
		convert(money, od.unitprice*quantity*(1-discount)) as linetotal

from	products p join ([order details] od join (orders o join customers c
on		p.productid=od.productid)
on		o.orderid=od.orderid)
on		c.customerid=o.customerid

where	o.orderid=10999
;


						--SQL92
						--wie mans machen kann
select	o.orderid,	orderdate, 
		c.customerid,
		companyname, 
		address, postalcode, city,
		p.productid, 
		productname, quantityperunit,
		od.unitprice, quantity, discount,
		convert(money, od.unitprice*quantity*(1-discount)) as linetotal

from	products p join [order details] od join orders o join customers c
on		c.customerid=o.customerid
on		o.orderid=od.orderid
on		p.productid=od.productid

where	o.orderid=10999
;




select	orderid,
		[order details].productid,
		[order details].unitprice,
		IIF(	[Order Details].unitprice = products.unitprice, 
				'Aktueller Preis',
                'Das ist nicht der Listenpreis') as notice,
		quantity
from [Order Details] 
join products 
on [Order Details].ProductID = Products.ProductID










		






