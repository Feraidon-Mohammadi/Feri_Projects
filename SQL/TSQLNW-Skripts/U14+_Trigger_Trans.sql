use nwmewes;

create table tab1
(sp1	int);

create trigger t_tab1
on tab1
after insert
as
begin
	if (select sp1 from inserted)=3
	rollback tran;
end;

begin tran
	insert into tab1 values(1);
	select * from tab1;
	insert into tab1 values(2);
	select * from tab1;
	insert into tab1 values(3);
	select * from tab1;
	insert into tab1 values(4);
	select * from tab1;
commit tran;

	insert into tab1 values(3);
	select * from tab1;


select * from tab1;

drop table tab1;