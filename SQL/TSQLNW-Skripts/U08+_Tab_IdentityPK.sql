use northwind;
go

drop table income_delivery;

create table income_delivery
(	inc_del_id		int				identity	
,	supplierid		int				not null
,	productid		int				not null
,	suppdate		datetime		not null
,	quantity		smallint		not null
,	primary key( inc_del_id)
);

exec sp_help income_delivery;

											--5mal
insert into income_delivery
values( 7, 18, '10.10.2020', 50);

select * from income_delivery;

truncate table income_delivery;

								--wenn das unbedingt(...) so gewollt ist
								--dann sollte mindestens
								--ein Unique-Constraint auf den
								--eigentlichen(zusammengesetzten)
								--Primary Key erstellt werden
alter table income_delivery
add unique(supplierid, productid, suppdate);