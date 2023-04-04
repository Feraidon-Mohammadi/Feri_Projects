/****	Übungen Abschnitt 7
		Transaktionen
******************************/

/****	Aufg. 1	****/

alter table categories
add primary key(categoryid);

create table subcategories
(	subcategoryid		int			not null	identity
,	subcategorytype		varchar(20)	not null	unique
,	categoryid			int			not null	references categories
,	description			varchar(250)	null
,	primary key(subcategoryid)
);

alter table products
add		subcategoryid	int		null;

alter table products
add		foreign key(subcategoryid) references subcategories;




/****	Aufg. 2	****/

create table reclamation
(	reclid		char(7)		not null	primary key
										constraint ck_recl_reclid
										check(reclid like '[0-9a-z]%-[0-9]')
,	orderid		int			not null	constraint fk_recl_orderid
										references orders
,	date_time	datetime	not null	default getdate()
,	description	varchar(250) not null
);

exec sp_helpconstraint reclamation;



/****	Aufg. 3	****/

create table deliverycondition
(	supplierid		int		not null	constraint pk_supplierid_productid
										primary key(supplierid, productid)
										constraint fk_supplierid
										foreign key(supplierid) 
										references suppliers
,	productid		int		not null	constraint fk_productid
										foreign key(productid)
										references products
,	unitprice		money	null		constraint ck_unitprice
										check(unitprice>0)
,	daysguarant		tinyint	null		constraint ck_daysguarant
										check(daysguarant>=0)
,	minquantity		tinyint	null		default 1
										constraint ck_minquantity
										check(minquantity>0)
);

exec sp_helpconstraint deliverycondition;


























