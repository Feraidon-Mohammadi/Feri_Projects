/****	�bungen Abschnitt 3
		Aggregatfunktionen
		und GROUP BY
******************************/


/****	a	den Durchschnittspreis für alle Produkte****/

select	avg(unitprice) as durchschnittspreis
from	products;



/****	b	den Durchschnittspreis, Minimalpreis, Maximalpreis, Durchschnittslagerbestand
	für alle Produkte
 ****/
select	avg(unitprice) as durchschnittspreis,
		min(unitprice) as minimalpreis,
		max(unitprice) as maximalpreis,
		avg(unitsinstock) as durchschnittslagerbestand
from	products;	 



/****	c	den Durchschnittspreis pro Kategorie(categoryid)****/

select	avg(unitprice), categoryid
from	products
group by categoryid;



/****	d	den Durchschnittspreis und die Anzahl der Produkte in einer Kategorie****/

select	avg(unitprice), count(productid) as anzahl_produkte, categoryid
from	products
group by categoryid;	



/****	e	den Durchschnittspreis und die Anzahl der Produkte je Lieferant(supplierid)****/

select	avg(unitprice) as durchschnittspreis,
		count(productid) as menge,
		supplierid
from	products
group by supplierid;



/****	f	den Durchschnittspreis und die Anzahl der Produkte für den Lieferanten mit
	der Nummer 12
****/

select	avg(unitprice) as durchschnittspreis,
		count(productid) as menge,
		supplierid
from	products
where	supplierid=12
group by supplierid;	


select	avg(unitprice) as durchschnittspreis,
		count(productid) as menge,
		supplierid
from	products
group by supplierid
having	supplierid=12;



/****	g	den Durchschnittspreis und die Anzahl der Produkte je Lieferant
	für Produkte der Kategorie 4
****/

select	avg(unitprice) as durchschnittspreis,
		count(productid) as menge,
		supplierid
from	products
where	categoryid=4
group by supplierid;		



/****	h	die Summe der bestellten Einheiten(unitsonorder) pro Kategorie für Produkte
	mit einem Stückpreis größer als 20 absteigend sortiert nach den Summen
****/

select	sum(unitsonorder) as summe_bestellte_einheiten,
		categoryid
from	products
where	unitprice>20
group by categoryid
order by 1 desc;




/****	i	den Durchschnittspreis und die Anzahl der Produkte je Lieferant und Kategorie****/

select	avg(unitprice) as durchschnittspreis,
		count(productid) as menge,
		supplierid as lieferant,
		categoryid as kategorie
from	products
group by categoryid, supplierid;


/****	j	den Durchschnittspreis und die Anzahl der Produkte in einer Kategorie
	mit Ausgabe des Kategorienamens an Stelle der ID
****/

select	avg(unitprice) as durchschnittspreis,
		count(productid) as menge,
		categories.categoryname as categoryname
from	products
join	categories
on		products.categoryid=categories.categoryid
group by categoryname;



/****	k	den Durchschnittspreis und die Anzahl der Produkte je Lieferant
	mit Ausgabe des Firmennamens(companyname) an Stelle der ID
****/

select	avg(unitprice) as durchschnittspreis,
		count(productid) as menge,
		companyname 
from	products
join	suppliers
on		products.supplierid=suppliers.supplierid
group by companyname;



/****	l	den Durchschnittspreis und die Anzahl der Produkte je Lieferant und Kategorie
	mit Ausgabe des Firmennamens(companyname) an Stelle der ID
	und des Kategorienamens an Stelle der KategorieID
****/

select	avg(unitprice) as durchschnittspreis,
		count(productid) as menge,
		companyname,
		categoryname
from	products
join	suppliers
on		products.supplierid=suppliers.supplierid
join	categories
on		products.categoryid=categories.categoryid
group by companyname, categoryname;	



/****	m	den Durchschnittspreis und die Anzahl der Produkte je Lieferant und Kategorie
	mit Ausgabe des Firmennamens(companyname) an Stelle der ID
	und des Kategorienamens an Stelle der KategorieID;
	es sollen nur die Produkte berücksichtigt werden, bei denen der Wert für die
	bestellten Einheiten(unitsonorder) größer 20 ist.
****/

select	avg(unitprice) as durchschnittspreis,
		count(productid) as menge,
		companyname,
		categoryname
from	products
join	suppliers
on		products.supplierid=suppliers.supplierid
join	categories
on		products.categoryid=categories.categoryid
where	unitsonorder>20
group by companyname, categoryname;	




/****	n	den Durchschnittspreis und die Anzahl der Produkte je Lieferant und Kategorie
	mit Ausgabe des Firmennamens(companyname) an Stelle der ID
	und des Kategorienamens an Stelle der KategorieID;
	es sollen nur die Produktgruppen berücksichtigt werden, bei denen die Summe für die
	bestellten Einheiten(unitsonorder) größer 70 ist.
****/
select	avg(unitprice) as durchschnittspreis,
		count(productid) as menge,
		companyname,
		categoryname,
		sum(unitsonorder) as sum_units_onorder
from	products
join	suppliers
on		products.supplierid=suppliers.supplierid
join	categories
on		products.categoryid=categories.categoryid
group by companyname, categoryname
having	sum(unitsonorder)>70;	




/****	o	Wieviel Stück wurden von jedem Produkt bisher insgesamt bestellt?
	Verwenden Sie quantity aus [order details] und geben Sie den Produktnamen aus.
****/

select	productname,
		sum(quantity) as stueck
from	products
join	[order details]
on		products.productid=[order details].productid
group by productname
order by stueck;



/****	p	Wieviel Stück wurden von jedem Produkt im Jahr 2021 bestellt?****/

select	productname,
		--year(orderdate) as Jahr,
		sum(quantity) as stueck
from	products
join	[order details]
on		products.productid=[order details].productid
join	orders
on		orders.orderid=[order details].orderid
where	year(orderdate)=2021
group by productname--, year(orderdate)
order by productname;




/****	q	Wieviel Stück wurden von Produkten jeder Kategorie im Jahr 2021 bestellt?
	Hinweis:	Gruppieren Sie nur nach Kategorie, nicht nach Produkte
****/

select	categoryid,
		sum(quantity) as stueck
from	products
join	[order details]
on		products.productid=[order details].productid
join	orders
on		orders.orderid=[order details].orderid
where	year(orderdate)=2021
group by categoryid
;	




/****	r	Wieviel Stück wurden von Produkten jeder Kategorie im Jahr 2021 pro Monat
bestellt? Geben Sie den Kategorienamen aus.
Hinweis:	Auch hier keine Gruppierung nach Produkt bitte.
****/

select	categoryname,
		month(orderdate) as monat,
		sum(quantity) as stueck
from	products
join	[order details]
on		products.productid=[order details].productid
join	orders
on		orders.orderid=[order details].orderid
join	categories
on		categories.categoryid=products.categoryid
where	year(orderdate)=2021
group by categoryname, month(orderdate)
order by categoryname, monat;		




/****	s	Ermitteln Sie die Umsatzsumme pro Jahr. 
	Bilden Sie dazu aus 3 Feldern der Tabelle [order details] ein berechnetes Feld.
****/

select	sum(convert(money, unitprice*quantity*(1-discount))),
		year(orderdate)
from	[order details]
join	orders
on		[order details].orderid=orders.orderid
group by year(orderdate);





/****	t	Ermitteln Sie die Umsatzsumme pro Jahr und Land, in das geliefert wurde.****/

select	sum(convert(money, unitprice*quantity*(1-discount))),
		year(orderdate),
		shipcountry
from	[order details]
join	orders
on		[order details].orderid=orders.orderid
group by year(orderdate), shipcountry
order by year(orderdate), 1 desc;	




/****	u	Ermitteln Sie die Umsatzsumme pro Jahr , das Land, in das geliefert wurde, und pro
Kunde.
****/

select	sum(convert(money, unitprice*quantity*(1-discount))),
		year(orderdate),
		shipcountry,
		orders.customerid,
		companyname
from	[order details]
join	orders
on		[order details].orderid=orders.orderid
join	customers
on		customers.customerid=orders.customerid
group by year(orderdate), shipcountry, orders.customerid, companyname
order by year(orderdate), 1 desc;	




/****	v	Ermitteln Sie die Umsatzsumme pro Jahr , das Land, in das geliefert wurde, und pro
Kunde, bei denen die Umsatzsumme weniger als 100 beträgt.
****/

select	sum(convert(money, unitprice*quantity*(1-discount))),
		year(orderdate),
		shipcountry,
		companyname
from	[order details]
join	orders
on		[order details].orderid=orders.orderid
join	customers
on		customers.customerid=orders.customerid
group by year(orderdate), shipcountry, companyname
with rollup
order by year(orderdate) desc, shipcountry desc, companyname desc
;


select	sum(convert(money, unitprice*quantity*(1-discount))),
		year(orderdate),
		shipcountry,
		orders.customerid,
		companyname
from	[order details]
join	orders
on		[order details].orderid=orders.orderid
join	customers
on		customers.customerid=orders.customerid
group by rollup(	year(orderdate), 
					shipcountry, 
					(orders.customerid, companyname)
				)

order by year(orderdate) desc, shipcountry desc, companyname desc
;




/****	w	****/

select	sum(convert(money, unitprice*quantity*(1-discount))),
		year(orderdate),
		shipcountry,
		orders.customerid,
		companyname
from	[order details]
join	orders
on		[order details].orderid=orders.orderid
join	customers
on		customers.customerid=orders.customerid
group by cube(	year(orderdate), 
					shipcountry, 
					(orders.customerid, companyname)
				)

order by year(orderdate) desc, shipcountry desc, companyname desc
;




/****	x	****/

select	sum(convert(money, unitprice*quantity*(1-discount))),
		year(orderdate),
		shipcountry,
		orders.customerid,
		companyname
from	[order details]
join	orders
on		[order details].orderid=orders.orderid
join	customers
on		customers.customerid=orders.customerid
group by year(orderdate), shipcountry, orders.customerid, companyname
having	sum(convert(money, unitprice*quantity*(1-discount)))<100

order by year(orderdate), 1 desc;		















