--ANSI-SQL

update orders
set ...
where ...;

commit;



update ....;

update ....;

insert....;

delete....;

if <bedingung ok>
		commit;
else
		rollback;



--Wiederherstellen aus dem Transaktionsprotokoll bei Neustart:

--RECOVERY =	Redo + Undo 


select * from products
where productid=50;
					--AUTOCOMMIT ist Server-Einstellung

update products			--sog. Autocommit Transaktion			
set unitprice=300
where productid=50;

					--ROLLBACK hat keinen Zweck

select * from products
where productid=50;



update products			--sog. Autocommit Transaktion			
set unitprice=16.25
where productid=50;


--set implicit_transactions on	--setzt AUTOCOMMIT bis auf Widerruf auﬂer Kraft	
--						--sog. implizite Transaktion	
--	
--update kunden				
--set kennzahl=200
--where knum=2030;
--
--select * from kunden
--where knum=2030;
--
--rollback;
--
--commit;
--
--set implicit_transactions off	--Widerruf



select * from [order details]
where orderid=11000;


begin transaction			--setzt AUTOCOMMIT bis Transaktionsende 
					--auﬂer Kraft
					--(sog. explizite Transaktion)
update  [order details]
set quantity=quantity+5
where orderid=11000
and productid=4;

update products
set unitsonorder=unitsonorder+5
where productid=4;

select * from [order details]
where orderid=11000;

if <bedingung nicht ok>
rollback transaction;

commit transaction;		--Transaktionsende




select * from departments;

--bei Bedarf

create table departments
(	deptid				char(3)			not null,
	deptname			varchar(20)		not null,
	deptlocationid		tinyint			null		default 1,
	deptchiefempno		tinyint			null,
	budget				money			null		default 100000
);

									--CHECK-CONSTRAINT(Einschr‰nkung)
alter table departments
add check(budget between 0 and 1000000)

exec sp_help departments;

truncate table departments;




begin transaction
	insert into departments values('A12', 'Download', default, default, 200000);
	insert into departments values('A13', 'Upload', default, default, 2000000);
commit transaction

-- es wird trotzdem ein wert eingetragen bei begin  zwischen commit
select * from departments;

truncate table departments;	
  

set xact_abort on;			--auch bei CONSTRAINT-Verletzung
							--wird die Transaction zusammengehalten
--set xact... sorgt daf¸r das es als eine wirkliche transaktion gesehne wird										
										
									
							
							
	--f¸r programmierer
	--try,wenn laufzeitfehler auftritt -> mache im catchblock weiter						
begin try
	begin transaction
	insert into departments values('A12', 'Download', default, default, 200000);
	insert into departments values('A13', 'Upload', default, default, 2000000);
	commit transaction	
end	try
begin catch
	if xact_state()=-1
		rollback transaction;

	print ERROR_MESSAGE();

	raiserror('Budget darf nicht mehr als 1000000 sein', 16,1);
end catch								
										
	




									

