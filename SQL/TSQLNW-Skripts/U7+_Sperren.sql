--disable trigger all on products;


									--Sperrgranularität
									--Zeilensperren statt Tabellensperre
									--obwohl ohne WHERE-Klausel
begin tran

	update products
	set unitprice=unitprice+1;
	
	select * from products;
	
	exec sp_lock;

	select * from sys.dm_tran_locks
	where request_mode='X';
	
rollback tran	





--Sitzung 1

begin tran

	select * from products with(tablock, holdlock)
	
--commit tran;	


--Sitzung 2

select * from products;

select * from products  with(readuncommitted);		--Dirty Read


--Sitzung 3  

begin tran

	update Products
	set UnitsInStock=UnitsInStock+10
	where SupplierID=10
	
	select * from Products
	where SupplierID=10
	
--	commit tran


--Sitzung 4  

begin tran

	update Products
	set UnitsInStock=UnitsInStock+10
	where SupplierID=10
	
	select * from Products
	where SupplierID=10
	
--	commit tran


--Sitzung 5

exec sp_lock

select * from sys.dm_tran_locks;

select	session_id,
			start_time,
			command,
			blocking_session_id,
			wait_type,
			wait_time
from	sys.dm_exec_requests
where blocking_session_id<>0;	





	

