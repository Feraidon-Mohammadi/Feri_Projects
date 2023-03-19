/****	�bungen Abschnitt 4
		Unterabfragen
******************************/


/****	a	Productid, productname, unitprice, categoryid der Produkte, die in der selben
	Kategorie sind wie das Produkt Nr. 37.
****/

select	productid, productname, unitprice, categoryid
from	products
where	categoryid=(	select	categoryid
						from	products
						where	productid=37);



/****	b	Productid, productname, unitprice, categoryid der Produkte, die in der selben
	Kategorie sind wie das Produkt Nr. 37 und vom selben Lieferanten kommen.
****/

select	productid, productname, unitprice, categoryid, supplierid
from	products
where	categoryid=(	select	categoryid
						from	products
						where	productid=37)
and		supplierid=(	select	supplierid
						from	products
						where	productid=37);	 



/****	c	Productid, productname, unitprice, categoryid der Produkte, die in der selben
	Kategorie sind wie das Produkt Nr. 37 und nicht vom selben Lieferanten kommen.
****/

select	productid, productname, unitprice, categoryid, supplierid
from	products
where	categoryid=(	select	categoryid
						from	products
						where	productid=37)
and		supplierid!=(	select	supplierid
						from	products
						where	productid=37);	



/****	d	Companyname, contactname, city, phone der Lieferanten, die Produkte der
	Kategorie 5 liefern.
****/

select	companyname, contactname, city, phone
from	suppliers
where	supplierid in(	select	supplierid
						from	products
						where	categoryid=5);	



/****	e	Companyname, contactname, city, phone der Lieferanten, die keine Produkte der
	Kategorie 5 liefern.
****/

select	companyname, contactname, city, phone
from	suppliers
where	supplierid not in(	select	supplierid
							from	products
							where	categoryid=5);

select	companyname, contactname, city, phone
from		suppliers
left join	products
on			suppliers.supplierid=products.supplierid
and			categoryid=5
where		productid is null;


select	companyname, contactname, city, phone
from	suppliers
where	not exists(	select	*
					from	products
					where	categoryid=5
					and		supplierid=suppliers.supplierid);



/****	f	Companyname, contactname, city, phone der Kunden, die im 2. Halbjahr 2021
mehr als 10 Bestellungen haben.
****/
select	customerid, companyname, contactname, city, phone
from	customers
where	10<(	select	count(*)
				from	orders
				where	orderdate between '1.7.2021' and '31.12.2021 23:59:59.998'
				and		customerid=customers.customerid);	





/****	g	productid, productname, categoryid, unitprice, quantityperunit für die Produkte,
deren Stückpreis unterhalb des Durchschnittspreises ihrer Kategorie liegt.
****/
select	productid, productname, categoryid, unitprice, quantityperunit
from	products as aussen 
where	unitprice<(	select	avg(unitprice)
					from	products
					where	categoryid=aussen.categoryid
					);		





/* Kür  - verschachtelt */
/****	h	Companyname, contactname, city, phone der Lieferanten, die Produkte der
Kategorie 5 liefern und wo bei den Produkten in der Verkpackungsgröße
(quantityperunit) der Ausdruck ‚250 g‘ vorkommt.
****/
select	companyname, contactname, city, phone
from	suppliers
where	supplierid=any(	select	supplierid	
						from	products
						where	categoryid=5
						and		quantityperunit like '%250 g%');




/****	i	Companyname, contactname, city, phone der Kunden, die im 2. Halbjahr 2021
keine Bestellung haben.
****/

select	companyname, contactname, city, phone
from	customers
where	customerid not in(	select	customerid
							from	orders
							where	orderdate between '20210701' and '20211231 23:59:59.998');


/****	j	Companyname, contactname, city, phone der Kunden, die im 2. Halbjahr 2021
kein Produkt der Kategorie 5 bestellt haben.
****/

select	companyname, contactname, city, phone
from	customers
where	customerid not in(	select	customerid
							from	orders
							where	orderdate between '20210701' and '20211231 23:59:59.998'
							and		orderid in(	select	orderid
												from	[order details]
												where	productid in(	select	productid
																		from	products
																		where	categoryid=5)
												)
						);

select	companyname, contactname, city, phone
from	customers
where	customerid not in(	select	customerid
							from	orders
							join	[order details]
							on		[order details].orderid=orders.orderid
							join	products
							on		[order details].productid=products.productid
							where	orderdate between '20210701' and '20211231 23:59:59.998'
							and		categoryid=5)






/**** ---korreliert---	k-	productid, productname, categoryid, unitprice, quantityperunit für die Produkte,
deren Stückpreis unterhalb des Durchschnittspreises ihres Lieferanten für diese Kategorie liegt.
****/

select	productid, productname, supplierid, categoryid, unitprice, quantityperunit,
		(	select	avg(unitprice)
			from	products
			where	supplierid=pa.supplierid
			and		categoryid=pa.categoryid) as avgpricepercat
from	products pa
where	unitprice<(	select	avg(unitprice)
					from	products
					where	supplierid=pa.supplierid
					and		categoryid=pa.categoryid);



/****	l	Companyname, contactname, city, phone der Lieferanten, die Produkte anbieten,
deren Einzelpreis unter dem Durchschnitt ihrer Kategorie liegt.
****/

select	companyname, contactname, city, phone
from	suppliers
where	supplierid in(	select	supplierid
						from	products paussen
						where	unitprice<(	select	avg(unitprice)
											from	products
											where	categoryid=paussen.categoryid)
					)
order by companyname;


select	distinct companyname, contactname, city, phone
from	suppliers
join	products as paussen
on		suppliers.supplierid=paussen.supplierid
where	unitprice<(	select	avg(unitprice)
					from	products
					where	categoryid=paussen.categoryid)
					;


/****	m	****/

select	companyname, contactname, country, city,
		orderid, orderdate
from	customers
join	orders
on		customers.customerid=orders.customerid
where	orderid =(		select	max(orderid)
						from	orders
						where	customerid=customers.customerid)
order by orderid;















