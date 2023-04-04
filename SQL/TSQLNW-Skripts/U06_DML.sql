/*************************************************
DML (Data Manipulation Language) - Anweisungen

	INSERT
	UPDATE
	DELETE

**************************************************/


/*************************************************
Bereitstellung

(	Die folgende Anweisung ist KEINE DML-Anweisung.
	Sie dient zur Bereitstellung einer neuen Tabelle,
	an der man bedenkenlos herummurkeln kann,
	ohne die vorhandene Northwind-Datenbank
	zu versaubeuteln.
	Es handelt sich um eine 
	DDL(Data Definition Language)-Anweisung
	zur Erstellung der Tabelle departments	)
**************************************************/
use NWMewes;
go

create table departments
(	deptid			char(3)			not null ,
	deptname		varchar(20)		not null,
	deptlocationid	tinyint			null		default 1,
	deptchiefempno	tinyint			null,
	budget			money			null		default 100000
);

select * from departments;



exec sp_help 'dbo.departments';

/***	Schreibender Zugriff auf Daten
***/

								--INSERT
--Syntax:
--			INSERT INTO <tabellenname>	[	(<spaltenliste>)	]
--			VALUES(<werteliste|ausdruckliste>)


						--Standardeingabe

select * from departments;

insert into departments
values('A01', 'Direktion', 1, 2, 450000);

select * from departments;


						--explizite Eingabe von NULL

insert into departments
values('A02', 'Entwicklung', null, null, null);

select * from departments;



insert into departments			
values('A02', 'Entwicklung', null, 5, null);

select * from departments;

--auf doppelte Schlüssel hinweisen
--Ausschluss wird später bei CONSTRAINTS behandelt



			--implizite Eingabe von NULL

insert into departments(deptid, deptname)
values('A03', 'Marketing');

select * from departments;


			--NULL oder DEFAULT

insert into departments
values('A04', 'Shopping', default, default, default);

select * from departments;	




/***	INSERT auf Spalten 
		mit der Eigenschaft IDENTITY	***/

select * from shippers;	

exec sp_help 'dbo.shippers';

insert into shippers
values(4, 'Rolling Packages', null);

insert into shippers
values('Rolling Packages', null);

select * from shippers;	


insert into shippers
values('Crash Tumbling Packages', null);

select * from shippers;

						--eine Lücke entsteht
delete from shippers
where shipperid=5;



							--IDENTITY_INSERT ON

	set identity_insert shippers on

	insert into shippers values('HappyHappyTransport','(503)999123')

	insert into shippers(shipperid, companyname, phone)
	 values(5,'HappyHappyTransport','(503)999123')

	insert into shippers(shipperid, companyname, phone)
	values(4,'HappyHappyTransport','(503)999123')

	insert into shippers(shipperid, companyname, phone)
	values(13,'SlowbutVeryVeryGood','(503)123999')


	select * from shippers

	set identity_insert shippers off

							--IDENTITY_INSERT OFF


insert into shippers values('FlyingIstheBest',null)

select * from shippers


				--zu einem Eintrag in Orders
				--gehört mindestens ein Eintrag in [Order Details]
				--dort muss genau die OrderID verwendet werden
				--die auch in Orders eingegeben wurde
				--die ist aber auch mit IDENTITY erzeugt worden
				--wie ermittelt man den IDENTITY-Wert?

begin tran

insert into orders(customerid, orderdate)
values ('ALFKI', getdate());

select * from orders
where orderid=(	select max(orderid) from orders);


/****************************************Funktionen zum Ermitteln
										 des letzten IDENTITY-Werts

select	@@identity,
		ident_current('orders'), 
		scope_identity()
****************************************************/

--insert into [order details]			--so nicht!!!
--values(scope_identity, ...)


declare @id	int;

set @id=(select scope_identity())

insert into [order details]
values(@id, ...)

select * from orders
where orderid=scope_identity();

rollback tran


					--Startwert und Schrittweite

--bei Bedarf:	create database beispieldb

--use beispieldb;

create table testident
(	sp1	int	identity(20000,-500),
	sp2	char(10),
	sp3 smallmoney
);

insert into testident values('Franz', 500);
insert into testident values('Waldemar', 1500);
insert into testident values('Gertrud', 700);

select * from testident;

set identity_insert testident on

insert into testident(sp1, sp2, sp3)
values(0,'Franz', 500);

select * from testident;

set identity_insert testident off



drop table testident;








				--Datentyp uniqueidentifier

create table testguid
(	guid	uniqueidentifier default newid() unique
	,xname	varchar(20))

insert into testguid values(newid(),'XXYZ')
insert into testguid values(default,'XXYZ')
insert into testguid values('ED48D507-9E13-40BE-97B3-0BC95CCA921C','XXYZ')

alter table testguid
add constraint df_uq default newid() for guid;


select * from testguid

select newid()

drop table testguid;


					--INSERT mit Unterabfrage

insert into [order details](orderid, productid, unitprice, quantity, discount)
values(11076, 21, ???, 10, 0);




insert into [order details](orderid, productid, unitprice, quantity, discount)
values(	11076, 
		21, 
		(select unitprice from products where productid=21),
		10, 
		0);

select * from [order details]
where orderid=11076;





select * from departments;

insert into departments
values('A04', 'Sales', 3, 5, 40000);

insert into departments
values('A05', 'Sales', 3, 5, 40000);

select * from departments;


create table demo
(	sp1		rowversion,			--früher: timestamp
	sp2		varchar(20));

insert into demo
values	(default, 'Sabine'),
		(default, 'Claudia');

select * from demo;

update demo
set sp2='Erna Sabine'
where sp2='Sabine';

drop table demo;




							---UPDATE
--Syntax:
--			UPDATE	<tabellenname>	
--			SET		<spaltenname>=<ausdruck>
--				[,	<spaltenname>=<ausdruck>[,...]]
--		[	WHERE	<prüfausdruck>	]


select * from departments;

update departments
set	deptchiefempno=5
where	deptid='A03';

select * from departments;

update departments
set budget=budget+100000;

select * from departments;


update departments
set budget=coalesce(budget, 0)-100000;

select * from departments;


update departments
set		budget=null,
		deptlocationid=4
where deptid='A02';

select * from departments;



update departments
set	budget=budget*.95		--budget=*.95		
where deptid='A01';

select * from departments;



update departments
set deptchiefempno=	case deptid
						when 'A02' then 9
						when 'A03' then 1
						when 'A04' then 4
					else deptchiefempno
					end;

select * from departments;



update departments
set	deptchiefempno=(	select employeeid
						from employees
						where lastname='Davolio'	)
where deptid='A01';

select * from departments;

update departments
set deptchiefempno=11
where deptid='A03';

select * from departments;

								--UPDATE mit Unterabfrage

update departments
set deptchiefempno=NULL
where deptchiefempno not in(	select employeeid
								from employees);

select * from departments;


								--DELETE
--Syntax:
--			DELETE FROM	<tabellenname>	
--		[	WHERE	<prüfausdruck>	]
									
delete * from departments;		--GIBTS NICHT!!!!!
									

delete from departments
where budget is null;

select * from departments;


								--Standard-DELETE
								--Ausnahmen sollten eher selten sein
delete from departments
where deptid='A03';

select * from departments;

								--DELETE mit Unterabfrage

delete from departments
where deptchiefempno not in(	select employeeid
								from employees);




begin transaction

delete from departments;

select * from departments;

--if <bedingung>
--	commit tran
--else
rollback tran

select * from departments;



select * from departments

begin tran
						
truncate table departments;	--setzt IDENTITY-Wert auf Startwert zurück

select * from departments

rollback tran

select * from departments

											--Bericht >>Datenträgerverwendung öffnen

											--richtig große Tabelle kopieren
											--(121317 Zeilen)
select soh.*,
		[CarrierTrackingNumber],
		[OrderQty],
		[ProductID],
		[SpecialOfferID],
		[UnitPrice],
		[UnitPriceDiscount],
		[LineTotal]
into	salesod
from adventureworks2016.sales.salesorderdetail sod
join adventureworks2016.sales.salesorderheader soh
on	soh.SalesOrderID=sod.SalesOrderID;


select * from salesod;
											--DELETE dauert länger

declare @vor	datetime2,
		@nach	datetime2;

set	@vor=CURRENT_TIMESTAMP;

delete from salesod;

set	@nach=CURRENT_TIMESTAMP;

select datediff(ms, @vor, @nach);

											--Erneutes Kopieren der Daten
											--aus der AdventureWorksDB
insert into salesod
select soh.*,
		[CarrierTrackingNumber],
		[OrderQty],
		[ProductID],
		[SpecialOfferID],
		[UnitPrice],
		[UnitPriceDiscount],
		[LineTotal]

from adventureworks2016.sales.salesorderdetail sod
join adventureworks2016.sales.salesorderheader soh
on	soh.SalesOrderID=sod.SalesOrderID;


select * from salesod;

											--TRUNCATE geht schnell

declare @vor	datetime2,
		@nach	datetime2;

set	@vor=CURRENT_TIMESTAMP;

truncate table salesod;

set	@nach=CURRENT_TIMESTAMP;

select datediff(ms, @vor, @nach);



