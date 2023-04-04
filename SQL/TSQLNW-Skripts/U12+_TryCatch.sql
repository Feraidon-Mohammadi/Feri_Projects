											--Klassische Fehlerbehandlung

/*********************************************************************
SQL-Anweisung

if @@error<>0
begin
	raiserror..;
	return;
end;
**********************************************************************/



--exec sp_helpconstraint products;

/***	bei Bedarf:

alter table products
add check(unitsonorder>=0); 

********************************************/



--select * from [order details] where orderid=11000

--select * from products where productid=24

			--1x ausführen mit +10
			--2x ausführen mit -10


			
									
declare @fehler int;		--übernimmt error_number()					

begin try
	
	begin transaction;				--setzt AUTOCOMMIT bis Transaktionsende 
									--außer Kraft
									--(sog. explizite Transaktion)
		update  [order details]
		set quantity=quantity-10
		where orderid=11000
		and productid=24;

		update products
		set unitsonorder=unitsonorder-10
		where productid=24;
	
	commit transaction;

end try
begin catch
		
		set @fehler=error_number();
		
		 print 'Fehler Nr. '+convert(varchar, @fehler)+' aufgetreten';

		if xact_state()=-1

			rollback transaction;

end catch;

select @fehler as Fehler_Nr;

--if @fehler is null






select * from [order details] where orderid=11000

select * from products where productid=24