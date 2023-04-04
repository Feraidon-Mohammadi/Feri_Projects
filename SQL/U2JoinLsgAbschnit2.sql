/****	uebungen Abschnitt 2
		Joins
******************************/


/****	a	Daten für Bestellungen mit den Daten für den dazugehörige Kunden mit 
	Ausgabe der folgenden Felder:
	orderid, customerid, companyname, orderdate, shipaddress, shipcity.
	داده‌های سفارشات همراه با داده‌های مربوط به مشتری مرتبط، با نمایش فیلدهای زیر:
شماره سفارش، شناسه مشتری، نام شرکت، تاریخ سفارش، آدرس ارسال، شهر ارسال.
****/
select	orderid, orders.customerid, 
		companyname, orderdate, shipaddress, shipcity
from	orders
join	customers
on		orders.customerid=customers.customerid;

select	orderid, orders.customerid, 
		companyname, orderdate, shipaddress, shipcity
from	orders,customers
where	orders.customerid=customers.customerid;




/****	b	Daten für Bestellungen mit den Daten für den dazugehörige Kunden mit 
	Ausgabe der folgenden Felder:
	orderid, customerid, companyname, orderdate, shipaddress, address(aus customers),
	shipcity, city(aus customers)
	sortiert nach city, address(aus customers).
	طلاعات سفارش‌ها همراه با اطلاعات مرتبط مشتریان با گرفتن فیلدهای زیر:
شماره سفارش، شناسه مشتری، نام شرکت، تاریخ سفارش، آدرس حمل‌ونقل، آدرس (از جدول مشتریان)، شهر حمل‌ونقل، شهر (از جدول مشتریان)
مرتب شده بر اساس شهر و آدرس (از جدول مشتریان)
****/
select	orderid, orders.customerid, 
		companyname, orderdate, 
		shipaddress, address,
		shipcity, city
from	orders,customers
where	orders.customerid=customers.customerid
order by city, address;	 





/****	c	Daten für Bestellungen mit den Daten für den dazugehörige Kunden mit 
	Ausgabe der folgenden Felder:
	orderid, customerid, companyname, orderdate, shipaddress, address(aus customers),
	shipcity, city(aus customers)
	dabei nur die Zeilen, bei denen shipcity und city ungleich sind.
	طلاعات سفارشات با اطلاعات مشتری مرتبط و بازگشت فیلدهای زیر:
شناسه سفارش، شناسه مشتری، نام شرکت، تاریخ سفارش، آدرس حمل و نقل، آدرس (از جدول مشتریان)، شهر حمل و نقل، شهر (از جدول مشتریان)
فقط ردیف هایی که شهر حمل و نقل و شهر مشتریان متفاوت هستند ، باید نمایش داده شوند.
****/

select	orderid, orders.customerid, 
		companyname, orderdate, 
		shipaddress, address,
		shipcity, city
from	orders,customers
where	orders.customerid=customers.customerid
and		shipaddress<>address
order by city, address;	


select	orderid, orders.customerid, 
		companyname, orderdate, 
		shipaddress, address,
		shipcity, city
from	orders inner join customers
on		orders.customerid=customers.customerid
and		shipaddress<>address
order by city, address;



/****	d	supplierid, companyname, contactname, phone, city aus der Tabelle Lieferanten
	(suppliers) mit productid, productname, categoryid, unitprice aus der Tabelle
	products für die Produkte des jeweiligen Lieferanten
****/

select	suppliers.supplierid, companyname, contactname, phone, city,
		productid, productname, categoryid, unitprice
from	suppliers, products
where	suppliers.supplierid=products.supplierid;


select	suppliers.supplierid, companyname, contactname, phone, city,
		productid, productname, categoryid, unitprice
from	suppliers 
join	products
on		suppliers.supplierid=products.supplierid;



/****	e	orderid, customerid, orderdate, productid, quantity, unitprice, discount
	aus den entsprechenden Tabellen 
	für das 3. Quartal 2021 bei denen die Lieferung nach Finland, Sweden, Norway
	oder Denmark geht.
	داده های سفارشات و مشتریان مرتبط با آن در جداول مربوطه برای سه ماهه سوم سال 2021 که ارسال آنها به فنلاند ، سوئد ، نروژ یا دانمارک انجام شده است.
****/

select	orders.orderid, customerid, orderdate,
		productid, quantity, unitprice, discount,
		shipcountry
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
where	datepart(q, orderdate)=3
and		year(orderdate)=2021
and		(shipcountry like 'Finland'
or		shipcountry like 'Sweden'
or		shipcountry like 'Norway'
or		shipcountry like 'Denmark');


select	orders.orderid, customerid, orderdate,
		productid, quantity, unitprice, discount,
		shipcountry
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
where	datepart(q, orderdate)=3
and		year(orderdate)=2021
and		shipcountry in ('Finland','Sweden','Norway','Denmark');



/****	f	orderid, orderdate, customerid, companyname, city, phone, 
	productid, productname, quantityperunit, categoryid, supplierid
	aus den erforderlichen Tabellen
****/

select	orders.orderid, orderdate, customers.customerid,
		companyname, city, customers.phone,
		products.productid, productname,
		quantityperunit, categoryid, supplierid
from	orders
join	customers
on		orders.customerid=customers.customerid
join	[order details]
on		orders.orderid=[order details].orderid
join	products
on		[order details].productid=products.productid;



/****	g	orderid, orderdate, customerid, companyname, city, phone, 
	productid, productname, quantityperunit, categoryid, supplierid
	aus den erforderlichen Tabellen für die Bestellungen der ersten 5 Monate
	des Jahres 2021 die von der Transportfirma Nr.3 (Spaltenwert für shipvia=3)
	nach Canada geliefert wurden.
****/

select	orders.orderid, orderdate, customers.customerid,
		companyname, city, customers.phone,
		products.productid, productname,
		quantityperunit, categoryid, supplierid
from	orders
join	customers
on		orders.customerid=customers.customerid
join	[order details]
on		orders.orderid=[order details].orderid
join	products
on		[order details].productid=products.productid
where	orderdate between '1.1.2021' and '31.5.2021 23:59:59.998'
and		shipvia = 3
and		shipcountry = 'Canada';



/****	h	die kompletten Datensätze der Kunden ohne eine einzige Bestellung.
	Hinweis:	Outer Join
****/

select	customers.*
from	customers
left outer join	orders
on		customers.customerid=orders.customerid
where	orderid is null;





/****	i	orderid, orderdate, customerid, 
companyname, city, phone (aus customers), 
	productid, productname, quantityperunit, categoryname, 
	unitprice(unitprice kommt in zwei Tabellen vor; wählen Sie die richtige aus, sprich:
	die Tabelle, in der der Preis gespeichert ist, der für die Bestellung gilt)
	companyname, phone, city(aus suppliers),
	companyname, phone (aus shippers)
	aus den erforderlichen Tabellen für die Bestellungen der ersten 10 Tagen
	des Jahres 2021 die nach Canada, USA oder Mexico geliefert wurden
****/

select	orders.orderid, orderdate, 
		customers.customerid, customers.companyname,
		customers.city, customers.phone,
		products.productid, productname,
		quantityperunit, 
		categoryname, 
		[order details].unitprice,
		suppliers.companyname, suppliers.phone,
		suppliers.city, 
		shippers.companyname, shippers.phone,
		shipcountry
from	customers
join	orders
on		customers.customerid=orders.customerid
join	[order details]
on		orders.orderid=[order details].orderid
join	products
on		[order details].productid=products.productid
join	suppliers
on		products.supplierid=suppliers.supplierid
join	categories
on		products.categoryid=categories.categoryid
join	shippers
on		shippers.shipperid=orders.shipvia
where	orderdate between '1.1.2021' and '10.1.2021 23:59:59:998'
and		shipcountry in('Canada', 'USA', 'Mexico');





/****	j	orderid, productid, productname, orderdate, unitprice(aus [order details]), 
	unitprice(aus products) aus den erforderlichen Tabellen, sortiert nach
	productid, orderdate.
****/

select	orders.orderid, products.productid,
		productname, orderdate, 
		[order details].unitprice, products.unitprice
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
join	products
on		[order details].productid=products.productid
order by productid, orderdate;







/****	k	Für die Bestellung Nr. 10999 die
	orderid, orderdate, shippeddate, shipcountry, shipcity, shipaddress,
	customerid, companyname, contactname, phone,
	lastname, firstname des Mitarbeiters, der die Bestellung angenommen hat
	(in einem Ausgabefeld stringverknüpft),
	companyname(aus shippers),
	productid, productname, categoryname, quantityperunit,
	quantity, unitprice, discount, sowie in einem berechneten Feld
	den Gesamtpreis für den jeweiligen Bestellposten der Zeile
	(Unter Einbeziehung von Stückzahl und Discount) im Währungsformat.
****/
select	[order details].orderid, orderdate, shippeddate, 
		shipcountry, shipcity, shipaddress,
		customers.customerid, customers.companyname, contactname, customers.phone,
		lastname+', '+firstname as Mitarbeiter,
		shippers.companyname, 
		products.productid, productname, 
		categoryname, quantityperunit,
		quantity, [order details].unitprice, discount,
		convert(money, [order details].unitprice*quantity*(1-discount)) as gesamtpreis
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
join	products
on		[order details].productid=products.productid
join	customers
on		orders.customerid=customers.customerid
join	employees
on		employees.employeeid=orders.employeeid
join	categories
on		categories.categoryid=products.categoryid
join	shippers
on		shippers.shipperid=orders.shipvia
where	orders.orderid=10999;






/****	l	Finden Sie orderid, customerid und orderdate heraus für Bestellungen, wo
	derselbe Kunde an ein und demselben Tag zweimal bestellt hat, d.h.
	ein und derselbe Kunde hat an demselben Tag zwei verschiedene Bestellnummern.
	Hinweis:	Sie müssen die Tabelle orders mit sich selbst verknüpfen.
****/
select	o1.orderid, o1.customerid, o1.orderdate
from	orders as o1
join	orders as o2
on		o1.orderdate=o2.orderdate
and		o1.customerid=o2.customerid
and		o1.orderid<>o2.orderid;



/****	m	die kompletten Datensätze der Produkte, die im Jahr 2022 noch gar nicht bestellt 
	wurden.
	Hinweis:	verknüpfen Sie zuerst orders und [order details] und dann mit 
			Outer Join products
****/
select	products.*
from	orders
join	[order details]
on		orders.orderid=[order details].orderid
and		year(orderdate)=2022
right join	products
on		[order details].productid=products.productid
where	orderdate is null;




select	products.*
from	orders
join	[order details]
on		orders.orderid=[order details].orderid

right join	products
on		[order details].productid=products.productid
and		year(orderdate)=2022
where	orderdate is null;









