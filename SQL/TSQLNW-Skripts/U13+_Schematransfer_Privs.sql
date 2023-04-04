create table dbo.tabx(sp1	int);

grant select, insert 
on tabx
to sqluserx;

grant update, delete
on schema::dbo
to sqluserx;

create schema schemax;

alter schema schemax
transfer dbo.tabx;

execute as user='sqluserx';

select * from schemax.tabx;

revert;