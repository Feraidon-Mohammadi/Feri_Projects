								--Vordefinierte Funktionen

select getdate()

select year(getdate())

select pi(), sin(pi()/2), sin(120), exp(20)

select original_login()

select upper(city) from customers;


/**********************************************************************
	InLine-Funktionen		können wie Views verwendet werden
									bieten aber höhere Funktionalität
									und Flexibilität
**********************************************************************/		


/***	InLine-Funktion
		zeigt pro ausgewählten Lieferanten
		pro Kategorie die Anzahl der Produkte
		und den Durchschnittspreis
*******************************************************************/

																				--zum Vergleich ein unflexibles View

create view v_cat_avg_supp12
as
	select		companyname,
				categoryid,
				count(*) as anzahl,
				avg(unitprice) as durchschnittspreis
	from		products
	join		suppliers
	on			suppliers.supplierid=products.supplierid
	where		suppliers.supplierid=12
	group by	companyname,
				categoryid
;	

select * from v_cat_avg_supp12;

																				--dagegen die InLine-Funktion
create function udf_cat_avg
(@suppid	int)
returns table
as
return
(	select		companyname,
				categoryid,
				count(*) as anzahl,
				avg(unitprice) as durchschnittspreis
	from		products
	join		suppliers
	on			suppliers.supplierid=products.supplierid
	where		suppliers.supplierid=@suppid
	group by	companyname,
				categoryid
);	

select * from udf_cat_avg(12);	

select * from udf_cat_avg(21);

select * from udf_cat_avg(31);	

select * from udf_cat_avg();

select * from udf_cat_avg((select supplierid from suppliers where companyname='Lyngbysild'));



create function udf_od
(@orderid	int=10500)
returns table
as
return
(	select	 * 
	from	v_orderdetails_total
	where	orderid=@orderid);



select * from udf_od(11000);

select * from udf_od(11010);

select * from udf_od(11011);

select * from udf_od();


select * from udf_od(default);	--richtiges Ergebnis


								--die höhere Funktionalität
								--gegenüber den Views
												
								--hier ein unflexibles View
create view v_bestelldaten2020
as
select		orderid, orderdate, shipcountry, shipcity, shipaddress,
			companyname, contactname, c.country, c.city, c.address,
			lastname+', '+firstname as bearbeiter
from		orders o
join		customers c
on			o.customerid=c.customerid
join		employees e
on			o.employeeid=e.employeeid			
where		orderdate between '1.1.2020' and '31.12.2020 23:59:59'


												--hier die viel flexiblere Inline-Funktion
create function udf_bestelldaten
(	@anfang		datetime='1.1.2000',
	@ende		datetime='31.12.2099')
returns table

as
return
(	select		orderid, orderdate, shipcountry, shipcity, shipaddress,
				companyname, contactname, c.country, c.city, c.address,
				lastname+', '+firstname as bearbeiter
	from		orders o
	join		customers c
	on			o.customerid=c.customerid
	join		employees e
	on			o.employeeid=e.employeeid			
	where		orderdate between @anfang and @ende
);	


select * from udf_bestelldaten('1.8.2020', '31.7.2021 23:59:59');	

select * from udf_bestelldaten();			--so gehts nicht

select * from udf_bestelldaten(default, default);

select * from udf_bestelldaten(default, '7.9.2021');

exec sp_help 'dbo.udf_bestelldaten';

exec sp_helptext 'dbo.udf_bestelldaten';





/*****************************************************************
Skalare Funktionen
*****************************************************************/

create function	udf_linetotal
(	@unitprice	money,
	@quantity	smallint,
	@discount	float							
)
returns money
as
begin
	return   @unitprice*@quantity*(1-@discount);
end;


select	dbo.udf_linetotal(4.99, 23, 0.03);


								--Verwendung in der Abfrage von s.o.
								--auf die InLine-Funktion UDF_OD
select *, dbo.udf_linetotal(unitprice, quantity, discount)
from udf_od(11000);



create function	udf_linetotal_v2
(	@unitprice	money,
	@quantity	smallint,
	@discount	float							
)
returns money
as
begin
	
	declare @result money;
	
	set @result=@unitprice*@quantity*(1-@discount);
	
	return @result; 
	
end;

									/*	FREIGHT lässt sich nicht ohne weiteres
										einmalig zur Summe der Bestelldetails
										addieren												*/

select		orders.orderid,
			customerid,
			orderdate,
			freight,
			sum(dbo.udf_linetotal(unitprice, quantity, discount))  as ordertotal
			,sum(dbo.udf_linetotal(unitprice, quantity, discount))+freight as 'ordertotal incl. freight'
from		orders
join		[order details]
on			orders.orderid=[order details].orderid	
group by	orders.orderid,
			customerid,
			orderdate,
			freight;
				
					
				
									/*	Funktion, die zur Summe der Bestelldetails
										einmalig die Frachtkosten addiert					*/
										
										
create function udf_order_total(@orderid		int)
returns	money
as
begin
		declare		@total		money,
					@sumdetails	money;
						
		set @sumdetails=(	select	sum(dbo.udf_linetotal(unitprice, quantity, discount))
							from	[order details]
							where	orderid=@orderid						
						);
		set @total=@sumdetails+(	select	freight
									from	orders
									where	orderid=@orderid
												);									
		return @total;
end;	


select	orderid,
		customerid,
		orderdate,
		freight,
		dbo.udf_order_total(orderid) as 'Bestellung gesamt'
from orders;				


select dbo.udf_order_total(11000);

select		orders.orderid,
			customerid,
			orderdate,
			sum(dbo.udf_linetotal(unitprice, quantity, discount))  as ordertotal,
			freight
			,dbo.udf_order_total(orders.orderid) as 'ordertotal incl. freight'
from		orders
join		[order details]
on			orders.orderid=[order details].orderid	
group by	orders.orderid,
			customerid,
			orderdate,
			freight;



											--Verwendung in der InLine-Funktion
											--UDF_BESTELLDATEN
alter function udf_bestelldaten
(	@anfang		datetime='1.1.2000',
	@ende		datetime='31.12.2020')
returns table
as
return
(	select	orderid, orderdate, shipcountry, shipcity, shipaddress,

			dbo.udf_order_total(orderid) as order_total,

			companyname, contactname, c.country, c.city, c.address,
			lastname+', '+firstname as bearbeiter
	from	orders o
	join	customers c
	on		o.customerid=c.customerid
	join	employees e
	on		o.employeeid=e.employeeid			
	where	orderdate between @anfang and @ende
);	

select * from udf_bestelldaten('1.8.2020', '31.7.2021 23:59:59');		


									/*	einfache Skalarfunktion
										zum Konvertieren von datetime
										in einfaches Datum						*/
										
create function	udf_ansi_datum(@datum	datetime)
returns date
as
begin
	return convert(date, @datum);
end;		


select	getdate(),
		dbo.udf_ansi_datum(getdate());	
			
select	orderid,
		customerid,
		dbo.udf_ansi_datum(orderdate)			
from	orders;	



select * from orders
where dbo.udf_ansi_datum(orderdate) 
between '2021-05-13' and '2021-09-14';	



/***		Skalare Funktion ermittelt den enthaltenen
			Umsatzsteuerbetrag (10%)
			für den Gesamtbetrag einer Bestellung
**************************************************************/		
create function udf_tax(@orderid	int)
returns money
as
begin
	return (select (	select	sum(dbo.udf_linetotal(unitprice, quantity, discount))
						from	[order details]
						where	orderid=@orderid						
					)	*10/(110))
end
;	

select dbo.udf_order_total(10520), dbo.udf_tax(10520);



alter function udf_tax(@orderid	int, @mwstsatz int)
returns money
as
begin
	return (select (	select	sum(dbo.udf_linetotal(unitprice, quantity, discount))
							from	[order details]
							where	orderid=@orderid						
					)	*@mwstsatz/(100+@mwstsatz))
end
;	

select dbo.udf_order_total(10520), dbo.udf_tax(10520, 30);


select	dbo.udf_order_total(orderid) as ordertotal, 
		dbo.udf_tax(orderid, 19) as ordertax, 
			*
from orders;

													--Test mit ca.
													--690000 Zeilen
select		--dbo.udf_order_total(orderid) as ordertotal, 
			--dbo.udf_tax(orderid, 10) as ordertax, 
			*
from (select o1.* from orders o1, orders o2) o;	
													--Ausführen ohne Funktionen:	6s
													--Ausführen mit Funktionen:		226s(387s)




													--Skalarfunktion mit 
													--Rückgabedatentyp XML

--select * from v_orders_summ

create function udf_custom_order()
returns xml
as
begin
	return(
				select		companyname,
							city,
							orderid,
							orderdate,
							ordertotal
				from		customers customer
				join		v_orders_summ [order]
				on			customer.customerid=[order].customerid
				order by	companyname
				for xml auto);
end;	
 
select dbo.udf_custom_order();	


alter function udf_custom_order(@custid char(5))
returns xml
as
begin
	return(
				select	companyname,
						city,
						orderid,
						orderdate,
						ordertotal
				from	customers customer
				join	v_orders_summ [order]
				on		customer.customerid=[order].customerid
				where	customer.customerid=@custid
				order by companyname
				for xml auto);
end;	

select dbo.udf_custom_order('ALFKI');	

select	customerid,
		phone,
		country,
		dbo.udf_custom_order(customerid)
from	customers;		
			




/***************************************************************************
Funktion mit Tabellenrückgabe und Programmierung
***************************************************************************/


create function udf_od2(@orderid int)
returns	@od2 table (	bestellid		int,
						produktid		int,
						stckpreis		money,
						menge			smallint,
						preisnachlass	real)
as
begin
	if	(@orderid is null)
		begin
			insert into @od2
			select * from [order details];
		end;
	else
		begin
			insert into @od2
			select * from [order details]
			where orderid=@orderid;
		end;
	return;
end;		

select * from udf_od2(11000);		

select * from udf_od2(default);	--alle Datensätze	

select * from udf_od2();			--Fehlermeldung	

select * from udf_od2(12000);









/**********************************************************************************************

	Weitere InLine-Funktionen
	
**********************************************************************************************/


																--Beispiel von vorhin mit berechnetem Feld
create function udf_odx(@orderid	int)
returns table
as
return
(	select *, dbo.udf_linetotal(unitprice, quantity, discount) as linetotal
	from [order details]
	where orderid=@orderid);
	
select * from udf_odx(10999);	

begin tran;								--DELETE funktioniert sogar mit dem 
	delete from udf_odx(10999)			--berechneten Feld
	where productid=77;
	
	select * from udf_odx(10999);
	
	select * from [order details] where orderid=10999;
rollback tran;	



create function udf_jahr_lfland(@jahr smallint)
returns table 
as
return(
select 	shipcountry,
			year(orderdate) as jahr,
			datepart(q, orderdate) as quartal,
			sum(dbo.udf_linetotal(unitprice, quantity, discount) ) as umsatzsumme, 
			count(od.orderid)		as anzahl_bestellposten
from [order details] od
join orders o
on o.orderid=od.orderid
where year(orderdate)=@jahr
group by  shipcountry,
          year(orderdate), 
          datepart(q, orderdate)
with rollup
);

select * from udf_jahr_lfland(2020);
select * from udf_jahr_lfland();



/*	Hier unten kommt noch ein ganz fettes Beispiel
	mit UNION										*/


create function udf_jahresanalysen(@jahr smallint)
returns table 
as
return(
select 	shipcountry,
        year(orderdate) as jahr,
        datepart(q, orderdate) as quartal,
        sum(unitprice*quantity*(1-discount)) as umsatzsumme, 
		count(od.orderid)		as anzahl_bestellposten
from [order details] od
join orders o
on o.orderid=od.orderid
where year(orderdate)=@jahr
group by  shipcountry,
          year(orderdate), 
          datepart(q, orderdate)
with rollup

union

select 	null,
        year(orderdate) as jahr,
        datepart(q, orderdate) as quartal,
        sum(unitprice*quantity*(1-discount)), 
	count(od.orderid)		as anzahl_bestellposten
from [order details] od
join orders o
on o.orderid=od.orderid
where year(orderdate)=@jahr
group by  year(orderdate), 
          datepart(q, orderdate)
with rollup
)

select * from udf_jahresanalysen(2021)
select * from udf_jahresanalysen()


	
	
/***************************************************************************************

	Weitere Funktionen mit Tabellenrückgabe und Programmierung
	
***************************************************************************************/		

				
create function udf_jahr_lfland2(@jahr smallint=null)

returns @jahr_lfland2 table
						(shipcountry	varchar(20)
						,jahr			smallint
						,quartal		tinyint
						,umsatz			money
						,anz_posten     int
						) 
as

begin
	if @jahr is null
		
		insert into @jahr_lfland2
		
		select	shipcountry,
					year(orderdate) as jahr,
					datepart(q, orderdate) as quartal,
					sum(unitprice*quantity*(1-discount)) as umsatzsumme, 
					count(od.orderid)as anzahl_bestellposten
		from	[order details] od
		join	orders o
		on		o.orderid=od.orderid
										--Hier fehlt die WHERE-Klausel
										--mit Parameter
		group by	shipcountry,
					year(orderdate), 
					datepart(q, orderdate)
		with rollup
		
	else
		insert into @jahr_lfland2
		
		select	shipcountry,
					year(orderdate) as jahr,
					datepart(q, orderdate) as quartal,
					sum(unitprice*quantity*(1-discount)) as umsatzsumme, 
					count(od.orderid)as anzahl_bestellposten
		from	[order details] od
		join	orders o
		on		o.orderid=od.orderid

		where year(orderdate)=@jahr

		group by	shipcountry,
						year(orderdate), 
						datepart(q, orderdate)
		with rollup;


		
	return;
end;

select * from udf_jahr_lfland2(2020);
select * from udf_jahr_lfland2(2021);

select * from udf_jahr_lfland2();					--so gehts nicht



select * from udf_jahr_lfland2(default);			--so gehts




								/*		Die Jahresanalysen mit vorbelegtem Parameter
										und IF-Verzweigung													*/		
			
create function udf_jahresanalysen2(@jahr smallint=null)
returns @jahresanalysen table
	(shipcountry	varchar(20)
	,jahr		smallint
	,quartal	tinyint
	,umsatz		money
    ,anz_posten     int
     ) 
as
begin
	if @jahr is null
		
		insert into @jahresanalysen
		select 	shipcountry,
        year(orderdate) as jahr,
        datepart(q, orderdate) as quartal,
        sum(unitprice*quantity*(1-discount)) as umsatzsumme, 
	count(od.orderid)		as anzahl_bestellposten
from [order details] od
join orders o
on o.orderid=od.orderid

group by  shipcountry,
          year(orderdate), 
          datepart(q, orderdate)
with rollup

union

select 	null,
        year(orderdate) as jahr,
        datepart(q, orderdate) as quartal,
        sum(unitprice*quantity*(1-discount)), 
	count(od.orderid)		as anzahl_bestellposten
from [order details] od
join orders o
on o.orderid=od.orderid

group by  year(orderdate), 
          datepart(q, orderdate)
with rollup
		
		
else
		insert into @jahresanalysen
		select 	shipcountry,
        year(orderdate) as jahr,
        datepart(q, orderdate) as quartal,
        sum(unitprice*quantity*(1-discount)) as umsatzsumme, 
	count(od.orderid)		as anzahl_bestellposten
from [order details] od
join orders o
on o.orderid=od.orderid
where year(orderdate)=@jahr
group by  shipcountry,
          year(orderdate), 
          datepart(q, orderdate)
with rollup

union

select 	null,
        year(orderdate) as jahr,
        datepart(q, orderdate) as quartal,
        sum(unitprice*quantity*(1-discount)), 
	count(od.orderid)		as anzahl_bestellposten
from [order details] od
join orders o
on o.orderid=od.orderid
where year(orderdate)=@jahr
group by  year(orderdate), 
          datepart(q, orderdate)
with rollup
		
	return
end

select * from udf_jahresanalysen2(2006)
select * from udf_jahresanalysen2(2021)
select * from udf_jahresanalysen2()					--so gehts nicht



select * from udf_jahresanalysen2(default)			--so gehts

			
			
												