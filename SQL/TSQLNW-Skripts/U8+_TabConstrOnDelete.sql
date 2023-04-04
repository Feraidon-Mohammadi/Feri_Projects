create database personalabteilung;
go

use personalabteilung;

drop table personal, abteilung;

create table abteilung
(	abtid			char(4)	not null		primary key
,	abtname	varchar(30)		not null		unique);

go

create table personal
(	persid	char(5)			not null		primary key
,	fname	varchar(30)		not null	
,	vname	varchar(30)		not null
,	abtid	char(4)			null
,	chefid	char(5)			null			references personal);


insert into abteilung values('A1', 'Vertrieb');
insert into abteilung values('B1', 'Betrieb');
insert into abteilung values('C1', 'Trieb');


alter table personal
add constraint fk_pers_abt 
foreign key(abtid) references abteilung;

insert into personal values('P1', 'Raabe', 'Gislinde', null, null);
insert into personal values('P2', 'Nökel', 'Norma', 'A1', 'P1');
insert into personal values('P3', 'Seifert', 'Gertrud', 'B1', 'P1');
insert into personal values('P4', 'Werner', 'Günther', 'C1', 'P1');
insert into personal values('P5', 'Günther', 'Werner', 'C1', 'P4');
insert into personal values('P6', 'Engel', 'Gustav', 'B1', 'P3');
insert into personal values('P7', 'Ruppert', 'Rudolph', 'A1', 'P2');


insert into personal values('P8', 'Meier', 'Peter', 'A11', 'P2');


delete from abteilung where abtid='A1';

exec sp_helpconstraint personal


alter table personal
drop constraint fk_pers_abt;


alter table personal
add constraint fk_pers_abt 
foreign key(abtid) references abteilung
on delete cascade;

exec sp_helpconstraint personal

select * from abteilung;

select * from personal;

delete from abteilung where abtid='A1';

select * from abteilung;

select * from personal;

/*****************************************************************/

alter table personal
drop constraint fk_pers_abt;

alter table personal
add constraint fk_pers_abt 
foreign key(abtid) references abteilung
on delete set null;

select * from abteilung;

select * from personal;

delete from abteilung where abtid='B1';

select * from abteilung;

select * from personal;

/******************************************************************/

insert into abteilung values('D1', 'Dummy');

alter table personal
add default 'D1' for abtid;

alter table personal
drop constraint fk_pers_abt;

alter table personal
add constraint fk_pers_abt 
foreign key(abtid) references abteilung
on delete set default;

select * from abteilung;

select * from personal;

delete from abteilung where abtid='C1';

select * from abteilung;

select * from personal;

use master;

go

drop database personalabteilung;