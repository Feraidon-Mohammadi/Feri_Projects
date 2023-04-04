/**************	Verschachtelte Transaktionen 
					durch gegenseitigen Prozeduraufruf

create procedure p1
(...)
as
begin
	begin tran
		exec p2(...)
		exec p3(...)
		exec p4(...)
	commit tran

end;

create procedure p4
(...)
as
begin
	begin tran
		update..;
		update..;
	commit tran

end;
***********************************************************/


select @@trancount

begin tran	t1

select @@trancount

--exec proc_t2

	begin tran t2
	
	select @@trancount
	
	commit tran

--return	
	
select @@trancount	
	
commit tran	

select @@trancount
