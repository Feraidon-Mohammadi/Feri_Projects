/****	Übungen Abschnitt 1
		SFW
******************************/

/****	a Von allen Bestellungen(Tabelle Orders) die orderid, customerid, orderdate,
	shippeddate, shipcountry, shipcity, freight.	****/

select	orderid, customerid, orderdate, shippeddate,
		shipcountry, shipcity, freight
from	orders;



/****	b -Die kompletten Daten(=alle Spalten)  des Kunden mit der customerid ‚SAVEA‘	****/

select	*
from	customers
where	customerid='SAVEA';




/****	c  Die kompletten Daten aller Produkte der Kategorie 7.	****/

select	*
from	products
where	categoryid in(7);






/****	d Productid, productname, unitprice, categoryid, unitsinstock der Produkte
	der Kategorien 1, 4, 5 oder 7.	****/

select	productid, productname, unitprice, 
		categoryid, unitsinstock
from	products
where	categoryid in(1, 4, 5, 7);





/****	e- Productid, productname, unitprice, categoryid, unitsinstock der Produkte
	der Kategorien 1, 4, 5 oder 7 mit einem Lagerbestand unter 50 Einheiten.	****/

select	productid, productname, unitprice, 
		categoryid, unitsinstock
from	products
where	categoryid in(1, 4, 5, 7)
and		unitsinstock<50; 






/****	f-Für alle Produkte productid, productname, unitsinstock( der aktuelle Lagerbestand)
	und die Differenz zwischen unitsinstock und unitsonorder mit dem Spaltenalias
	‚verfügbar‘.	****/

select	productid, productname, unitprice, categoryid,
		unitsinstock, unitsinstock-unitsonorder as "verfügbar"
from	products;





/****	g Für alle Produkte productid, productname, categoryid, unitprice
	sortiert nach categoryid.	****/

select	productid, productname, categoryid, unitprice
from	products
order by categoryid;




/****	h Für alle Produkte productid, productname, categoryid, unitprice
	sortiert nach categoryid und unitprice(nach unitprice absteigend).	****/

select	productid, productname, categoryid, unitprice
from	products
order by categoryid, unitprice desc;





/****	i 	Die kompletten Daten für die Bestellungen des Jahres 2021.****/

select	*
from	orders
where	year(orderdate)=2021;

select	*
from	orders
where	orderdate between '1.1.2021' and '31.12.2021 23:59:59.998';






/****	j -orderid, customerid, orderdate, shipcountry, shipcity für die Bestellungen
	aus dem Zeitraum vom 01. Juli 2021 bis zum 31. August 2021.	****/

select	orderid, customerid, orderdate, 
		shipcountry, shipcity
from	orders
where	orderdate between '1.7.2021' and '31.8.2021 23:59:59.998';


select	orderid, customerid, orderdate, 
		shipcountry, shipcity
from	orders
where	year(orderdate)=2021
and		month(orderdate) in(7,8);


select	orderid, customerid, orderdate, 
		shipcountry, shipcity
from	orders
where	year(orderdate)=2021
and		(month(orderdate)=7
or		month(orderdate)=8);






/****	k	orderid, customerid, orderdate, shipcountry, shipcity für die Bestellungen
	aus dem Zeitraum vom 01. Juli 2021 bis zum 31. August 2021
	sortiert nach der customerid. ****/

select	orderid, customerid, orderdate, 
		shipcountry, shipcity
from	orders
where	orderdate between '1.7.2021' and '31.8.2021 23:59:59.998'
order by customerid;






/****	l- orderid, customerid, orderdate, shipcountry, shipcity für die Bestellungen
	aus dem Zeitraum vom 01. Juli 2021 bis zum 31. August 2021
	sortiert nach der customerid und orderdate.	****/

select	orderid, customerid, orderdate, 
		shipcountry, shipcity
from	orders
where	orderdate between '2021.07.01' and '2021.8.31 23:59:59.998'
order by customerid, orderdate;







/****	m	orderid, customerid, orderdate, shipcountry, shipcity für die Bestellungen
	aus dem Zeitraum vom 01. Juli 2021 bis zum 31. August 2021
	bei denen der Wert für shipcity mit ‚St‘ beginnt
	sortiert nach der customerid und orderdate.****/

select	orderid, customerid, orderdate, 
		shipcountry, shipcity
from	orders
where	orderdate between '2021.7.01' and '2021.8.31 23:59:59.998'
and		shipcity like 'St%'
order by customerid, orderdate;







/****	norderid, customerid, orderdate, shipcountry, shipcity sowie der Kalenderwoche
	für orderdate mit dem Spaltenalias ‚Kalenderwoche‘ für die Bestellungen
	aus dem Zeitraum vom 01. Juli 2021 bis zum 31. August 2021
	bei denen der Wert für shipcity mit ‚St‘ beginnt
	sortiert nach der customerid und orderdate.	****/

select	orderid, customerid, orderdate, 
		shipcountry, shipcity,
		datepart(wk, orderdate) as 'kalenderwoche'
from	orders
where	orderdate between '2021-07-01' and '2021.08.31 23:59:59.998'
and		shipcity like 'St%'
order by customerid, orderdate;






/****	o		orderid, customerid, orderdate, shipcountry, shipcity für die Bestellungen
	aus dem 1. Halbjahr 2022, deren Wert für shippeddate NULL ist.****/


select	orderid, customerid, orderdate, 
		shipcountry, shipcity, shippeddate
from	orders
where	orderdate between '1.1.2022' and '30.6.2022 23:59:59.998'
and		shippeddate is null;

--chat gpt fixed 
SELECT orderid, customerid, orderdate, shipcountry, shipcity
FROM orders
WHERE orderdate BETWEEN '2022-01-01' AND '2022-06-30 23:59:59.998'
AND shippeddate IS NULL;





/****	p  productid und unitprice aus [order details]. Führen Sie die Abfrage aus und beachten 
	Sie die Anzahl der Ergebniszeilen. Sorgen Sie in einer zweiten Abfrage dafür, dass 
jede Kombination aus productid und unitprice nur einmal ausgegeben wird. Beachten Sie die Anzahl der Ergebniszeilen. Beachten Sie die Ergebnisdaten. Wie ist das Ergebnis zu verstehen?  ****/
select	productid, unitprice
from	[order details]
order by productid;

select	distinct productid, unitprice
from	[order details]
order by productid;






/****	q	orderid, customerid, orderdate, shipcountry, shipcity so wie die Differenz 
	zwischen requireddate und dem aktuellen Datum in Wochen mit dem
	Spaltenalias Wochen_ueberfaellig für die Bestellungen aus dem April 2022
	deren Wert für shippeddate NULL ist und bei denen die customerid mit einem
	Buchstaben aus dem Bereich A bis F beginnt.****/

select	orderid, customerid, orderdate, shipcountry,
		shipcity, 
		datediff(ww, requireddate, getdate()) as 'Wochen_überfällig'
from	orders
where	orderdate between '1.4.2022' and '30.4.2022 23:59:59.998'
and		shippeddate is null
and		customerid like '[a-f]%';


-- chat gpt corrected 
SELECT orderid, customerid, orderdate, shipcountry, shipcity, 
       DATEDIFF(ww, requireddate, GETDATE()) AS "Wochen_überfällig"
FROM orders
WHERE orderdate BETWEEN '2022-04-01' AND '2022-04-30 23:59:59.998'
  AND shippeddate IS NULL
  AND customerid LIKE '[a-f]%' ;




/****	r-	orderid, customerid, orderdate, shipcountry, shipcity für die Bestellungen 
	 aus den Jahren 2021 und 2022, bei denen die customerid mit einem Buchstaben aus 
	dem Bereich A bis F beginnt das zweite Zeichen ein E, I, R, H oder L ist und 
	das letzte Zeichen ein S, sortiert nach customerid und orderdate.****/
select	orderdate, orderid, customerid, 
		shipcountry, shipcity
from	orders
where	orderdate between '1.1.2021' and '31.12.2022 23:59:59.998'
and		customerid like '[a-f][eirhl]%s'
order by customerid, orderdate;






/****	s	orderid, customerid, orderdate, shipcountry, shipcity für die Bestellungen 
	des Kunden mit der customerid ‚GREAL‘ aus dem 2. Quartal 2021
	mit Frachtkosten unter 100.****/

select	orderdate, orderid, customerid, 
		shipcountry, shipcity, freight as fracht
from	orders
where	customerid='GREAL' 
and		datepart(quarter, orderdate)=2 
and		year(orderdate)=2021
and		freight<100;






/****	t	customerid, companyname, contactname, country, city, postalcode, address der 
	Kunden(customers), deren postalcode genau aus 5 Ziffern besteht, sortiert nach
	country und postalcode.****/

select	customerid, companyname, contactname,
		country, city, postalcode, address
from	customers
where	postalcode like '_____'
order by country, postalcode;

select	customerid, companyname, contactname,
		country, city, postalcode, address
from	customers
where	postalcode like '[0-9][0-9][0-9][0-9][0-9]'
order by country, postalcode;






/****	u	employeeid, firstname und lastname in einem Feld stringverknüpft, birthdate,
	hiredate, title der Mitarbeiter(employees), die zum Zeitpunkt ihrer Einstellung
	(hiredate) älter als 40 Jahre alt waren. Lassen Sie zur Kontrolle das Alter zum
	Zeitpunkt der Einstellung ausgeben und vergeben Sie einen Spaltenalias****/

select employeeid,
		firstname+' '+lastname as name,
		concat(firstname,' ', lastname) as agent,
		firstname+lastname,
		birthdate,
		hiredate,
		title,
		datediff(year, birthdate, hiredate) as hireage
from	employees
where	datediff(year, birthdate, hiredate)>40;





