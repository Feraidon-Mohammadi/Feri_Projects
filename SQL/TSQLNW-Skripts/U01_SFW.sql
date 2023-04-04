					--schneller Überblick

use nwmewes;
go

select * from employees;



select * from employees
where employeeid=5;

select 	firstname, lastname, title, hiredate
from 	employees
where 	employeeid=5;


select	firstname+' '+ lastname , title, hiredate
from 	employees
where 	employeeid=5;

select	firstname+' '+ lastname as empname, title, hiredate as "(kein Spaltenname)"
from 	employees
where 	employeeid=5;

select	concat(firstname,' ', lastname) as empname, title, hiredate
from 	employees
where 	employeeid=5;


					--wird oft abgeliefert
					--macht keinen Sinn
					--liefert keine Zeile
select 	firstname+' '+ lastname as empname, title, hiredate
from 	employees
where 	hiredate=2002;


					--so macht es Sinn
select	firstname+' '+ lastname as empname, title, hiredate
from 	employees
where 	year(hiredate)=2002;


					--so auch, wenn HIREDATE
					--vom Datentyp DATE ist
select 	firstname+' '+ lastname as empname, title, hiredate
from 	employees
where 	hiredate between '1.1.2002' and '31.12.2002';


					--Logische Operatoren

					--AND
select	productid, productname, unitprice, unitsonorder, categoryid
from 	products
where	categoryid=1
and 	unitprice>50;

					--OR	
select 	productid, productname, unitprice, unitsonorder, CategoryID
from 	products
where 	categoryid=1
or 		unitprice>50;

					--zweimal OR
select 	productid, productname, unitprice, unitsinstock, CategoryID
from 	products
where 	categoryid=1
or 		unitprice>50
or		UnitsInStock<10;

					--zweimal AND
select 	productid, productname, unitprice, unitsinstock, CategoryID
from 	products
where 	categoryid=1
and 	unitprice>50
and		UnitsInStock<10;



					--AND und OR
select 	productid, productname, unitprice, unitsonorder, CategoryID
from 	products
where 	categoryid=1
or 		categoryid=6
and		unitprice>50;

select 	productid, productname, unitprice, unitsonorder, CategoryID
from 	products
where (categoryid=1
or 		categoryid=6)
and		unitprice>50;


					--IN
select 	productid, productname, unitprice, unitsonorder
from	 products
where 	categoryid in(1,6)
and 	unitprice>50;


select	productid,								--keine Zeile
			productname, 
			unitprice, 
			unitsonorder,
			QuantityPerUnit
from	 products
where 	quantityperunit= '%bottle_';


select	productid,								--11 Zeilen 
			productname, 
			unitprice, 
			unitsonorder,
			QuantityPerUnit
from	 products
where 	quantityperunit like '%bottle_';


select	productid,								--12 Zeilen
			productname, 
			unitprice, 
			unitsonorder,
			QuantityPerUnit
from	 products
where 	quantityperunit like '%bottle%';



					--DISTINCT		(mit ORDER BY)

select categoryid
from 	products
order by categoryid;					
					
select 	distinct categoryid
from 	products
order by categoryid;

					
select 	supplierid, categoryid
from		products
order by supplierid;

select 	distinct supplierid, categoryid
from 	products
order by supplierid;


select 	distinct supplierid, categoryid, ProductName
from 	products
order by supplierid;



					--mehr Details


			--Spaltenalias
			--berechnete Felder
			--Literale
			--Funktionen

select	productname
		, productname as ProduktBezeichnung				
		, unitsinstock-unitsonorder
		, unitsinstock-unitsonorder as "Frei verfügbar"
		, 'Verfügbare Einheiten'				--Literal (Textkonstante)
		, convert(varchar, unitsinstock-unitsonorder)+' Verfügbare Einheiten'
		, concat(unitsinstock-unitsonorder,' Verfügbare Einheiten')
from 	products;



											--Funktionen für Datum/Uhrzeit
select	orderdate
		, year(orderdate) j				--Jahr von Zeitangabe
		, month(orderdate)	m			--Monat
		, day(orderdate)	t			--Tag
		, datepart(q,orderdate)	q		--Quartal
		, datepart(wk, orderdate) kw			--Kalenderwoche
		, datediff(yy,orderdate,getdate()) ddj		--Differenz in Jahren
		, datediff(dd,orderdate,getdate())	 ddt	--Differenz in Tagen
		, datediff(dd,getdate(),'24.12.23')	 ddw	--Differenz bis Heiligaben
		, getdate()	heute				--Systemdatum/-uhrzeit
		, convert(date,orderdate) c1
					
from orders;

																	--und noch eine Funktion
select	dateadd(dd,-336,getdate()), 
		getdate(),
		dateadd(wk,20,getdate()),
		getdate()+50, 
		dateadd(hh, 145, getdate());

																	--einfache Berechnungen mit Zeitangaben
						--Ergebnisse von Rechenoperationen
						--sind immer im größten Datentyp
						--der in Operanden vorkommt
select 21*3, 21/3, 20/3, 20/3.


select 	(20/3)*3
		,(20/3.)*3.
		,20/3.
		,convert(decimal(34,5),20)/3*3
		,convert(decimal(35,5),20)/3*3
		,convert(decimal(34,5),222522)/3*3;

						--Stringverkettung

											--cannot convert...
select unitprice+' Dollar' from products;
											--can convert...
select concat(unitprice,' Dollar') from products;

select	titleofcourtesy,firstname,lastname,region
from	employees;

select	titleofcourtesy+' '+firstname+' '+lastname+' '+region as empname,
		concat(titleofcourtesy,' ',firstname,' ',lastname, ' ', region) as concat_empname,
		right(concat(titleofcourtesy,' ',firstname,' ',lastname, ' ', region), 2),
		rtrim(concat(titleofcourtesy,' ',firstname,' ',lastname, ' ', region))/*,
		rtrim(concat(titleofcourtesy,' ',firstname,' ',lastname, ' ', region), 5)*/
from	employees;




/*****************************CASE***********************************/

select 	productname, categoryid from products

select categoryid, categoryname from categories


select 	productname,
		categoryid,
			case categoryid
				when 1 then 'Getränke'
				when 2 then 'Gewürze'
				when 3 then 'Backwaren'
				when 4 then 'Milchprodukte'
				when 5 then 'Körnerkram'
				else 'Was anderes'
			end							AS Kategorie
from products


select 	productname,
			categoryid,
			case 
				when categoryid=1 then 'Getränke'
				when categoryid=2 then 'Gewürze'
				when categoryid=3 then 'Backwaren'
				when categoryid=4 then 'Milchprodukte'
				when categoryid=5 then 'Körnerkram'
				else 'Was anderes'
			end												AS Kategorie	
from products



select 	productname, unitprice,
			case 
				when unitprice<=10 then 'Billig'
				when unitprice between 10.01 and 50		then 'Normal'
				when unitprice between 50.01 and 100	then 'Teuer'
				when unitprice>100 then 'Uff'
			end												AS Gefühlter_Preis	
from products


select 	productname, unitprice,
			case 
				when unitprice<=10 then 'Billig'
				when unitprice between 10 and 50	then 'Normal'
				when unitprice between 50 and 100	then 'Teuer'
				when unitprice>100 then 'Uff'
			end												AS Gefühlter_Preis	
from products


select 	productname, unitprice,
			case 
				when unitprice<=10 then 'Billig'
				when unitprice<50	then 'Normal'
				when unitprice<100	then 'Teuer'
				when unitprice>=100 then 'Uff'
			end												AS Gefühlter_Preis	
from products

/********************************************************************/ 



						--WHERE-Klausel
						--Prädikatenlogik

						

					--IN: Aufzählung zulässiger Werte
select orderid, customerid, orderdate, shipcity
from orders
where shipcity in('London', 'Barcelona', 'Brandenburg');

					--IN: Aufzählung nicht zulässiger Werte
select orderid, customerid, orderdate, shipcity
from orders
where shipcity not in('London', 'Barcelona', 'Brandenburg');


							

					--BETWEEN: Intervall
select productid, productname, unitprice, unitsinstock
from products
where unitprice between 10 and 20;

					--BETWEEN: Intervall
select productid, productname, unitprice, unitsinstock
from products
where unitprice>=10 and unitprice<=20;

																	--echtes ZWISCHEN
select productid, productname, unitprice, unitsinstock
from products
where unitprice>10 and unitprice<20;

																	--Ausschluss des Intervalls
select productid, productname, unitprice, unitsinstock
from products
where unitprice not between 10 and 20;



					--Zeitintervalle


					--SO NICHT!!!!!!!!!!!!!
select *
from Orders
where OrderDate=2021;

					--sondern so
select *
from Orders
where OrderDate between '1.1.2021' and '31.12.2021 23:59:59.998';



					--oder so
select *
from Orders
where year(OrderDate)=2021;



																	--ein Datensatz mit Uhrzeit <> 00:00
insert into Orders(CustomerID, OrderDate)
values('ALFKI', '31.07.2021 10:30');


			--Bestellungen von genau einem Tag
			
			--wenn der Datentyp von ORDERDATE
			--DATE wäre, dann wäre das OK

select * from orders
where orderdate='31.07.2021';

			--da der Datentyp von ORDERDATE
			--DATETIME ist, muss es so sein

select * from orders
where orderdate between '31.07.2021' and '31.07.2021 23:59:59.998';

											--oder so
select * from orders
where convert(date, orderdate)='31.07.2021';

select * from orders
where orderdate like '%2021-07-31%'

											--oder so
select * from orders
where	day(OrderDate)=31
and		month(orderdate)=7
and		year(OrderDate)=2021;


delete from orders where orderid>11077;






					--NULL-Prädikat

					--das liefert wieder mal  ein großes X

select orderid, customerid, shipregion, shipcountry
from orders                  
where shipregion=NULL;

select orderid, customerid, shipregion, shipcountry
from orders                  
where shipregion<>NULL;
					
						
select orderid, customerid, shipregion, shipcountry
from orders			
where shipregion IS NULL;

select orderid, customerid, shipregion, shipcountry
from orders
where shipregion IS  NOT NULL;

					

					--LIKE: Textmuster
					--NUR für die Datentypen

					--	char, varchar, text
					--	nchar, nvarchar, ntext


select distinct country, city from customers
where country='B%';

select distinct country, city from customers
where country like 'B%';


select distinct country, city from customers
where country like '__';

select distinct country, city from customers
where country like '___';

											--mind. 8 Zeichen
select distinct country, city from customers
where country like '________%';

select distinct country, city from customers
where country like '%land';



select distinct country, city from customers
where country like '[BI]%';

select distinct country, city from customers
where country like '[B-I]%';

select distinct country, city from customers
where country like '[B-IMS]%';

select distinct country, city from customers
where country like '_[RS]%';



select distinct country, city from customers 
where country like 'Au%'

select distinct country, city from customers 
where country like '[Au]%'  



select distinct country, city, postalcode from customers
where postalcode like '[0-9][0-9][0-9][0-9]';


																	----Suche nach einem Maskierungszeichen

																	--select lastname, title, country, notes
																	--from employees
																	--where notes like '%[[]%';

																	--select lastname, title, country, notes
																	--from employees
																	--where notes like '%[_]%'

																	--select lastname, title, country, notes
																	--from employees
																	--where notes like '%,%'

																	--select lastname, title, country, notes
																	--from employees
																	--where notes like '%!%%' escape '!';


																	--select lastname, title, country, notes
																	--from employees
																	--where notes like '%[%]%'






			--Sortieren der Ergebnisse

select orderid, customerid, shipregion, shipcountry
from orders
order by shipcountry;

select orderid, customerid, shipregion, shipcountry
from orders
order by 4;

select orderid, customerid, shipregion, shipcountry
from orders
order by shipcountry, customerid;

select orderid, customerid, shipregion, shipcountry
from orders
order by shipcountry, customerid desc;

select orderid, customerid, shipregion, shipcountry
from orders
order by shipcountry desc, customerid desc;




select orderid, 
		customerid, 
		shipregion, 
		shipcountry, 
		year(orderdate) as orderyear
from orders
where /*year(orderdate)*/orderyear<2022
order by orderyear desc;



											--Gültigkeit von Spaltenalias






					--TOP(n)	Ausschnitt aus dem Sortierergebnis

select  top(20) orderid, customerid, shipregion, shipcountry, freight
from orders


select  top(20) orderid, customerid, shipregion, shipcountry, freight
from orders
order by freight desc;


select  top(20)  percent orderid, customerid, shipregion, shipcountry, freight
from orders
order by freight desc;



select top(20)  *
from [order details]
order by quantity desc

select top(20) with ties *
from [order details]
order by quantity desc

					--OFFSET-FETCH	seitenweise blättern

select orderid, customerid, shipregion, shipcountry, freight
from orders
order by orderdate
offset 0 rows
fetch next 20 rows only;


select orderid, customerid, shipregion, shipcountry, freight
from orders
order by orderdate
offset 100 rows
fetch next 20 rows only;



declare @i int=0;

while @i<100
begin
	select orderid, customerid, shipregion, shipcountry, freight
	from orders
	order by orderdate
	offset @i rows
	fetch next 20 rows only;

	set @i=@i+20
end;

























