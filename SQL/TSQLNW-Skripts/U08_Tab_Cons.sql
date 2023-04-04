/***Abschnitt 8:	Tabellen und Einschränkungen
									(Constraints)
****************************************************/


use northwind;
go

drop table departments;		--purge

create table dbo.departments
(	deptid				char(3)			not null
,	deptname			varchar(30)		not null
,	deptlocationid		tinyint				null
,	deptchiefempno		int					null
,	budget				money				null
);



select * from departments;

insert into departments
values('A01', 'Direktion', 1, 2, 450000);

insert into departments
values('X&Y', 'Kaffeebereitstellung', 1, 99, 99999999999999); 
 

/********************************Domänenintegrität
									
											in einer Spalte sind nur
											gültige(sinnvolle) Werte zulässig
******************************************************************************/

					--DEFAULT-Constraint
					--(Standardwert)

alter table departments
add default 1 for deptlocationid;

alter table departments
add default 1 for deptchiefempno;

insert into departments
values('A03', 'Einkauf', default, default, default);

select * from departments;

exec sp_help departments;

exec sp_helpconstraint departments;

alter table departments
drop constraint DF__departmen__deptc__534D60F1;

alter table departments
drop constraint DF__departmen__deptl__52593CB8;



alter table departments
add constraint df_dept_loc 
default 1 for deptlocationid;

alter table departments
add constraint df_dept_chief
default 1 for deptchiefempno;

exec sp_helpconstraint departments;

---------------------------------ein Funktionswert als Standardwert
exec sp_helpconstraint orders;

alter table orders
add constraint df_orders_odate
default getdate() for orderdate;


						--DEFAULT	erzwingt nichts
insert into departments
values('A04', 'Verkauf', default, 2, 50000);

select * from departments;


						--CHECK-Constraint
						--gibt vor, welche Werte
						--für eine Spalte
						--zulässig sind

alter table departments	 with nocheck
add constraint ck_dept_budget
check(budget between 0 and 1000000)
;
									--WITH NOCHECK ist eine Option
									--d.h. es geht u.U. auch ohne sie
									--z.B. immer, wenn die Tabelle noch leer ist



exec sp_helpconstraint departments;

select * from departments
where budget<0 or budget>1000000;

update departments
set budget=99999
where deptid='X&Y';

update departments
set budget=9999999
where deptid='X&Y';


							--Beachte:	ohne Constraint-Name
							--			ohne WITH NOCHECK
alter table departments
add check(deptlocationid>0);

select * from information_schema.check_constraints
where constraint_name like '%dep%';

select * from departments;

-------------------------------------Test
update departments
set budget=budget*3;

select * from departments;

-------------------------------------Neues Constraint und Tests
alter table departments with nocheck
add check(deptid like'A[0-9][0-9]');

update departments
set		deptid='A44'
where deptid='A04';

select * from departments;


update departments
set		deptid='B04'
where	deptid='A44';

select * from departments;


alter table orders
add constraint ck_orders_ordate_shipdate
check(orderdate<=shippeddate);

insert into orders(customerid, orderdate, shippeddate)
values('OTTIK', getdate(), getdate()+10);

insert into orders(customerid, orderdate, shippeddate)
values('HUNGO', getdate(), '20211217');






/*************************************Entitäts-Integrität

									Jede Zeile innerhalb einer Tabelle
									muss eindeutig identifizierbar sein
***********************************************************/

							--5mal ausführen
insert into departments
values('A04', 'Spaß & Spiel', default, 5, 500000);

select * from departments;

										--schlägt fehl
alter table departments with nocheck	--wenn Eindeutigkeit gefordert ist
add primary key(deptid);				--ist WITH NOCHECK keine Option


										--Kontrolle auf Eindeutigkeit von Werten
										--in einer Spalte die als 
										--Schlüsselspalte vorgesehen ist
							
select		deptid,
			count(*) as anzahl
from		departments
group by	deptid
having		count(*)>1;	
		
										--Problem
delete from departments
where deptid='A04';
										--Lösung
delete top(6) from departments
where deptid='A04';

delete top(1) from departments
where deptid='A01';

										--Lösung im Batch
declare @zahl int=(select count(*)-1 from departments where deptid='A04');

delete top(@zahl) from departments
where deptid='A04';

select * from departments;

										--Erstellen eines Primary Key
										--einfach so
alter table departments
add constraint pk_dept
primary key(deptid);

/************************	Die bessere Variante

							Erstellen eines Primary Key
							mit Constraint-Namen

							alter table departments
							add constraint pk_dept_deptid
							primary key(deptid);
***********************************************************************/

exec sp_helpconstraint departments;

insert into departments
values('A05', 'Spaß & Spiel', default, 5, 500000);

select * from departments;

delete from departments
where deptid='A05';

									--2. Primärschlüssel in einer Tabelle
									--geht nicht
alter table departments
add primary key(deptname);

									--statt dessen sollte man einen
									--Alternativschlüssel einrichten
									--(ohne Constraint-Namen)
alter table departments
add constraint uq_dept_name
unique(deptname);


update		departments
set			deptname='Verkauf'
where		deptid='A04';

update		departments
set			deptname='Verkauf2'
where		deptid='A04';

/***********************	Erstellen eines Unique-Constraint
							mit Constraint-Namen)

							alter table departments
							add constraint uq_dept_deptname
							unique(deptname);
**********************************************************************/


							--Zusammengesetzter Primärschlüssel
							--gleich in der CREATE TABLE-Anweisung
							--(ohne Constraint-Name)
create table income_delivery
(	supplierid		int				not null
,	productid		int				not null
,	deliverydate	datetime		not null
,	quantity		smallint		not null
,	primary key( supplierid, productid, deliverydate)
);

exec sp_help income_delivery;

insert into income_delivery
values( 7, 18, '10.10.2020', 50);

insert into income_delivery
values( 7, 18, '10.11.2020', 50);

insert into income_delivery
values( 7, 18, '10.11.2020 10:00', 50);

insert into income_delivery
values( 7, 18, '10.11.2020 16:00', 50);

insert into income_delivery
values( 7, 18, getdate(), 50);

select * from income_delivery;


--Übung:	PRIMARY KEY für [ORDER DETAILS]

select * from [order details];


alter table [order details]
add primary key(orderid);


alter table [order details]
add primary key(orderid, productid);



drop table income_delivery;

create table income_delivery
(	deliveryid		int				not null identity primary key
,	supplierid		int				not null
,	productid		int				not null
,	deliverydate	datetime		not null
,	quantity		smallint		not null
,	unique( supplierid, productid, deliverydate)
);

exec sp_help income_delivery;

insert into income_delivery
values( 7, 18, '10.10.2020', 50);

insert into income_delivery
values( 7, 34, '10.10.2020', 50);


select * from income_delivery;




delete from departments
where deptid='X&Y';


/**************************	Referenzielle Integrität
							
									jeder Fremdschlüsselwert verweist auf einen
									existierenden Primärschlüssel(Datensatz)
*******************************************************************************/
select * from departments;


exec sp_helpconstraint departments;


							--durch CHECK abgewehrt
insert into departments
values('X&Y', 'Kaffeebereitstellung', 1, 99, 99999999999999); 

insert into departments
values('X&Y', 'Kaffeebereitstellung', 1, 99, 99999); 
							
insert into departments
values('A07', 'Kaffeebereitstellung', 1, 99, 99999); 

insert into departments		--durch PRIMARY KEY abgewehrt
values('A07', 'Kaffeebereitstellung', 1, 99, 99999);

insert into departments		--durch UNIQUE abgewehrt
values('A08', 'Kaffeebereitstellung', 1, 99, 99999);

insert into departments		--jetzt sind alle Constraints einverstanden
values('A08', 'Ein_sinnvoller_Abteilungsname', 1, 99, 99999);

							--aber da ist noch was falsch im Datensatz...

select * from departments;

exec sp_helpconstraint departments;


alter table employees
add primary key(employeeid);

										--Beachte:	wieder mit WITH NOCHECK
alter table departments with nocheck
add	constraint fk_dept_emp
	foreign key(deptchiefempno) 
	references employees--(employeeid);
		

										--Ermitteln vorhandener ungültiger
										--(Fremdschlüssel)-Werte
select *
from	departments
where	deptchiefempno not in(	select employeeid
								from employees);	


select * from departments;

update departments
set deptchiefempno=5
where deptid='A07';

update departments
set deptchiefempno=1
where deptid='A08';



						--schlägt fehl
update departments
set deptchiefempno=17
where deptid='A07';

						--schlägt fehl
delete from employees
where employeeid=5;


										--rekursive Referenz								
select employeeid, lastname, reportsto
from	employees;


alter table employees
add		constraint fk_emp_emp
		foreign key(reportsto) references employees;








alter table products add primary key(productid);

alter table suppliers add primary key(supplierid);




						--zwei Constraints
						--in einer Anweisung	(geht)
alter table income_delivery
add	foreign key(supplierid)
	references suppliers,
	foreign key(productid)
	references products;


-----------------------------------	andere Schreibweisen
-----------------------------------	(gleich in die CREATE TABLE-Anweisung)

drop table departments;

drop table income_delivery;



create table departments
(	deptid		char(3)		not null
							primary key
							check(deptid like 'A[0-9][0-9]')
,	deptname	varchar(20)	not null
							unique
,	deptlocationid	tinyint	null
							default 1
							check(deptlocationid>0)
,	deptchiefempno	int		null
							constraint uq_dept_chief unique
							constraint fk_dept_emp references employees
,	budget			money	null
							default 100000
							check(budget between 0 and 1000000)						
);	


							--das geht so nicht !!!
create table income_delivery
(	supplierid		int			not null		primary key		references suppliers
,	productid		int			not null		primary key		references products
,	deliverydate	datetime	not null		primary key 
,	quantity		smallint	not null
);
							--so geht das !!!
create table income_delivery
(	supplierid		int			not null		references suppliers
,	productid		int			not null		references products
,	deliverydate	datetime	not null  
,	quantity		smallint	not null		check(quantity>0)
,	primary key(supplierid, productid, deliverydate)
);










