/****	�bungen Abschnitt 5
		Mengenoperatoren
******************************/


/****	a	a)	Vereinigen Sie in einer einzigen Abfrage die Adressinformationen(country, region, address, city, postalcode) aus den Tabellen customers, employees und suppliers.****/

select	country, region, city, address, postalcode, 'Kundenadresse' as herkunft
from	customers
union
select	country, region, city, address, postalcode, 'Mitarbeiteradresse' as herkunft
from	employees
union
select	country, region, city, address, postalcode, 'Lieferantenadresse' as herkunft
from	suppliers;



/****	b	Schreiben Sie eine Abfrage auf die Tabelle orders mit folgenden Spalten in der Ausgabe:	orderid, customerid, orderdate, shipcity, freight.
	In einer zusätzlichen Literal-Spalte sollen die Frachtkosten der jeweiligen Bestellung kommentiert werden, und zwar in folgender Weise:
	Frachtkosten über 1000:		Sehr teure Fracht
	Frachtkosten von 500 bis 1000	Teure Fracht
	Frachtkosten von 100 bis 499.99	Auch noch ziemlich teuer
	Frachtkosten von 10 bis 99.99	Normale Fracht
	Frachtkosten unter 10			Billigfracht
	Falls keiner der genannten Fälle zutrifft, soll als Literal ‚Kein Kommentar‘ erscheinen.

	Welche Alternative gäbe es zu einer Abfrage mit UNION.
****/

select	orderid, customerid, orderdate, shipcity, freight, 'Sehr teure Fracht' as Kosten
from	orders
where	freight>1000

union

select	orderid, customerid, orderdate, shipcity, freight, 'Teure Fracht' 
from	orders
where	freight between 500 and 1000

union

select	orderid, customerid, orderdate, shipcity, freight, 'Auch noch ziemlich teuer' 
from	orders
where	freight between 100 and 499.99

union

select	orderid, customerid, orderdate, shipcity, freight, 'Normale Fracht' 
from	orders
where	freight between 10 and 99.99

union

select	orderid, customerid, orderdate, shipcity, freight, 'Billige Fracht'
from	orders
where	freight<10

union

select	orderid, customerid, orderdate, shipcity, freight, 'Kein Kommentar' 
from	orders
where	freight is null
order by freight desc;	 


select	orderid, customerid, orderdate, shipcity, freight, 
		(	case
			when freight>1000 then 'Sehr teure Fracht'
			when freight>=500 then 'Teure Fracht'
			when freight>=100 then 'Auch noch ziemlich teuer'
			when freight>=10 then 'Normale Fracht'
			when freight<10 then 'BilligFracht'
			else 'Kein Kommentar'
			end	) as Kommentar
from	orders;


select	orderid, customerid, orderdate, shipcity, freight, 
		(	case
			when freight>1000 then 'Sehr teure Fracht'
			when freight between 500 and 1000 then 'Teure Fracht'
			when freight between 100 and 499.99 then 'Auch noch ziemlich teuer'
			when freight between 10 and 99.99 then 'Normale Fracht'
			when freight<10 then 'BilligFracht'
			else 'Kein Kommentar'
			end	) as Kommentar
from	orders;



/****	c	Ermitteln Sie companyname, contactname, city und phone von Lieferanten, die sowohl
Produkte der Kategorie 2 als auch Producte der Kategorie 5 liefern.
****/

select	companyname, contactname, city, phone
from	suppliers
join	products
on		suppliers.supplierid=products.supplierid
where	categoryid=5
intersect
select	companyname, contactname, city, phone
from	suppliers
join	products
on		suppliers.supplierid=products.supplierid
where	categoryid=2;



											--richtiges Ergebnis																			--dasselbe Ergebnis(2 Zeilen)
select	companyname, contactname, city, phone
from		suppliers
where supplierid in(select supplierid from products where categoryid=2)
and supplierid in(select supplierid from products where categoryid=5)


											--falsches Ergebnis																			--nicht dasselbe Ergebnis(11 Zeilen)
select	distinct companyname, contactname, city, phone, categoryid
from		suppliers as s
join		products as p
on			s.supplierid=p.supplierid
where	p.categoryid in(2, 5);




/****	d	Ermitteln Sie companyname, contactname, city und phone von Lieferanten, die ausschließlich Produkte der Kategorie ‚beverages‘(Getränke) liefern.****/

select	companyname, contactname, city, phone
from	suppliers
join	products
on		suppliers.supplierid=products.supplierid
join	categories
on		products.categoryid=categories.categoryid
where	categoryname='Beverages'
except
select	companyname, contactname, city, phone
from	suppliers
join	products
on		suppliers.supplierid=products.supplierid
join	categories
on		products.categoryid=categories.categoryid
where	categoryname<>'Beverages';


--Alternative mit NOT IN

select	distinct companyname,
						contactname,
						city,
						phone
from		suppliers
join		products
on			suppliers.supplierid=products.supplierid
join		categories
on			categories.categoryid=products.categoryid
where	categoryname='Beverages'
and		products.supplierid not in

(	select supplierid
	from		products
	join		categories
	on			categories.categoryid=products.categoryid
	where	categoryname<>'Beverages')


												--weitere Alternative
select	companyname, contactname, city, phone
from	suppliers as s
where	exists(	select	productid
				from	products
				where	s.supplierid=supplierid
				and		categoryid in(	select	categoryid	
										from	categories
										where	categoryname='beverages'
										)
				)
and not exists(	select	productid
				from	products
				where	s.supplierid=supplierid
				and		categoryid in(	select	categoryid	
										from	categories
										where	categoryname<>'beverages'
										)
				)



/****	e	In einem Abfrageergebnis mit 4 Spalten sollen gemeinsam erscheinen:

	Vor- und Nachname (in einem Feld) des Mitarbeiters, seinen employeeid, die Anzahl der aufgenommenen Bestellungen und in einem Literal die Ausgabe ‚Mitarbeiter‘ von allen Mitarbeitern, die mehr als 50 Bestellungen aufgenommen haben

	Kontaktname, customerid, Anzahl der Bestellungen und in einem Literal die Ausgabe ‚Kunde‘ von allen Kunden, die mehr als 5 Bestellungen aufgegeben haben.
****/

select	firstname+' '+lastname as name,
		convert(char, employees.employeeid) as ID,
		count(orderid) as ordercnt,
		'Mitarbeiter' as origin
from	employees
join	orders
on		employees.employeeid=orders.employeeid
group by	employees.employeeid,
			firstname+' '+lastname
having	count(orderid)>50

union

select	contactname,
		orders.customerid,
		count(orderid),
		'Kunde'
from	customers
join	orders
on		customers.customerid=orders.customerid
group by	orders.customerid,
			contactname
having	count(orderid)>5;


											--Version 2
select	firstname+' '+lastname as Name,
		cast(employeeid as char) as ID,
			(	select count(*) 
				from orders
				where orders.employeeid=employees.employeeid)as Anzahl_Bestellungen,
			'Mitarbeiter' as Typ
from		employees
where	(	select count(*) 
				from orders
				where employeeid=employees.employeeid)>50
union all
select	contactname,
			customerid,
			(	select count(*)
				from orders
				where orders.customerid=customers.customerid),
			'Kunde'
from		customers
where	(	select count(*)
				from orders
				where orders.customerid=customers.customerid)>5;



											--Version 3
select	concat(e.firstname, ' ', e.lastname),
		convert(char, e.employeeid),
		(	select	count(*)
			from	orders as o
			where	o.employeeid=e.employeeid),
		'Mitarbeiter'
from	employees as e
where	(	select	count(*)
			from	orders as o
			where	o.employeeid=e.employeeid)>50

union

select	c.contactname,
		c.customerid,
		(	select	count(*)
			from	orders as o
			where	o.customerid=c.customerid),
		'Kunde'
from	customers as c
where	(	select	count(*)
			from	orders as o
			where	o.customerid=c.customerid)>5


















