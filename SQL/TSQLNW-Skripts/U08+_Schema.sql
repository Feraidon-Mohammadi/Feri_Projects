use northwind;
go
create schema contact;
go
create table contact.adresses
(	id			int,
	street		varchar(70),
	postalcode	char(6),
	city		varchar(50),
	region		varchar(50)
);

exec sp_help 'contact.adresses';

select * from adresses;

select * from contact.adresses;

create table contact
(	id			int,
	phone		varchar(25),
	mobile		varchar(25),
	email		varchar(50));

exec sp_help 'contact';

select * from contact;

alter schema contact
transfer dbo.contact;

select * from contact;

select * from contact.contact;

create synonym adresses for contact.adresses;

create synonym contact for contact.contact;

select * from dbo.adresses;

select * from adresses;

select * from contact.adresses;


create table dbo.adresses
(	id		int,
	city	varchar(50),
	country	varchar(50)
);

drop synonym adresses;

create role persondata_role;

grant select, insert
on	  schema::contact
to persondata_role;

