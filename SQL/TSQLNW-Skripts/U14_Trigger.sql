 /***	In der Tabelle VERKAEUFER ist für die Spalte ORT 
		NULL erlaubt. Ein NULL im Wohnort macht aber keinen Sinn.
		Der Trigger gibt für diesen Fall eine Fehlermeldung aus
		und beendet die Transaktion
***/

create table nworderaudit
(	wer		nvarchar(128)
,	wann	datetime);


create trigger trg_orders_arbeitszeit
on orders
after update, insert, delete
as
begin

if (	datepart(hh, getdate())>19	or
		datepart(hh, getdate())<7	or
		datepart(dw, getdate()) in(6,7))
	begin
		
		raiserror('	Um die Zeit wird nicht gearbeitet', 17, 1);
		rollback transaction;
		
		insert into dbo.nworderaudit 
		values( original_login(), getdate() );
		return;
	end;
end;

------------------------------------------------------Zeitzone ändern

insert into orders(customerid, orderdate)
values('XXXXX', getdate());


update orders
set freight=50
where orderid=11000;


select * from dbo.nworderaudit;

select * from orders
where orderid>=11077;

select * from orders
where orderid=11000;

disable trigger trg_orders_arbeitszeit on orders;
				--all
-----------------------------------------------------Zeitzone wieder zurücksetzen



								--Trigger für Folgeoperation
								--auf Lagerbestand nach neuem Datensatz
								--in [order details]
								
create trigger trg_od_ins_unitsonorder
on [order details]
after insert, update
as
if update(quantity)
begin
	--set nocount on
								--funktioniert auch nur
								--wenn nur eine Zeile
								--in [order details] betroffen ist
	update	products
	set		unitsonorder=unitsonorder+(	select quantity
										from inserted)
	where	productid=(	select productid
						from inserted);						
end;								


select * from [order details]
where orderid=11000;

select productname, unitsonorder
from products
where productid=20;

insert into [order details]
values(11000, 20, (select unitprice from products where productid=20), 12, 0);


								--Überprüfung auf unverhältnismäßig 
								--starke Preiserhöhung
								--wird aus der Prozedur genommen...

alter procedure usp_upd_listenpreis
@productid	int		=null,
@preisneu	money	=null
as
begin
	declare @meldung varchar(400);
	declare @preisalt money;

					
	if	@productid is null or @preisneu is null
		begin
			set @meldung='	Sie müssen sowohl eine gültige ProduktID
							als auch einen neuen Preis angeben';
			raiserror(@meldung, 15, 1);
			return;
		end;
		
	if not exists(	select * from products
					where productid=@productid)
	begin
			set @meldung='	Es gibt kein Produkt mit dieser ID.
							Versuchen Sie es noch einmal.';
			raiserror(@meldung, 15, 1);
			return;	
	
	end;
	
	set @preisalt=(	select unitprice from products
					where productid=@productid);
					
	if (@preisneu>=@preisalt*2)
	begin
			set @meldung='	Der neue Preis den Sie angegeben haben 
							ist mindestens doppelt so hoch wie der alte.
							Laut Firmenrichtlinie XY ist das sittenwidrig. 
							Die Aktion wurde abgebrochen.';
			raiserror(@meldung, 15, 1);

			
			return;	
	
	end;													

	disable trigger trg_orders_updlistenpreis on products;

							--eigentliche Transaktion
	update products
	set unitprice=@preisneu
	where productid=@productid;

	enable trigger trg_orders_updlistenpreis on products;
end;




								--...und in einen Trigger eingebaut
								
create trigger trg_orders_updlistenpreis
on products
after update
as
if update(unitprice)
begin
								--funktioniert nur, wenn genau in einer Zeile
								--der Preis verändert wird
								
	declare		@preisalt	money, 
				@preisneu	money,
				@meldung	varchar(300);
	set @preisneu=(	select unitprice from inserted);
	set @preisalt=(	select unitprice from deleted);
					
	if (@preisneu>=@preisalt*2)
	begin
			set @meldung='	Der neue Preis den Sie angegeben haben 
							ist mindestens doppelt so hoch wie der alte.
							Laut Firmenrichtlinie XY ist das sittenwidrig. 
							Die Aktion wurde abgebrochen.';
			raiserror(@meldung, 15, 1);
			rollback transaction;
			return;	
	
	end;		
	
end;


select productid, productname, unitprice
from products
where productid=50;

----------------------------------Prozedur verhindert
begin transaction;
	exec usp_upd_listenpreis	@productid=50, 
								@preisneu=40;
	
	select productid, productname, unitprice
	from products
	where productid=50;
rollback transaction;	

--------------------------------------Trigger verhindert
update products
set unitprice=200
where productid=50;


exec usp_upd_listenpreis	@productid=50, 
								@preisneu=17;








	
							--Archivtabelle für orders und [order details]
create table odarchiv
(	orderid				int,
	productid			int,
	unitprice			money,
	quantity			smallint,
	discount			real,
	benutzer			varchar(50),
	datumuhrzeit		datetime)	

											
create trigger trg_odetails_archiv
on [order details]
after delete, update
as 
begin
					--DELETE löscht nur eine Zeile
	
	begin
		print 'Daten wurden archiviert'
											--archiviert jetzt auch alle Zeilen
											--wenn das DELETE mehrere
											--Zeilen löscht!!!!
		insert into odarchiv
		select	deleted.orderid,
				deleted.productid,
				deleted.unitprice,
				deleted.quantity,
				deleted.discount,
				original_login(),
				getdate()
		from deleted
	end;
end;

select * from [order details]
where orderid=11000;

delete from [order details]
where orderid=11000
and productid=20;

select * from odarchiv;

delete from [order details]		--geht auch ohne Cursor
where orderid=11000
and discount=0.25;









----------------------------------------	Problem, wenn die DML-Anweisung
--											tausende Zeilen bearbeitet
--											kann Sitzungs-Cache überlasten


alter trigger trg_odetails_archiv
on [order details]
after delete, update
as 
begin
					--DELETE löscht nur eine Zeile
	if (select count(*) from deleted)	=1
	begin
		print 'Daten wurden archiviert'

		insert into odarchiv
		select	deleted.orderid,
				deleted.productid,
				deleted.unitprice,
				deleted.quantity,
				deleted.discount,
				original_login(),
				getdate()
		from deleted
	end
						--Behandlung mehrerer Zeilen
						--mit Cursor
						
					--DELETE löscht mehr als eine Zeile
	if (select count(*) from deleted)	>1
	begin
					--Cursor-Deklaration
					--SELECT erfasst alle Zeilen
								--aus DELETED
		declare c_deleted cursor for 	select * 
										from deleted

					--Deklaration von Variablen
					--zur Aufnahme der Werte
					--aus den Cursorzeilen
		declare	@oid	int, 
				@pid	int, 
				@up	money, 
				@qu int, 
				@d real

					--Öffnen des Cursors
					--(Ausführen des Select
					--+Laden der Treffermenge)
		open c_deleted

					--Zeiger bewegen in der Treffermenge
					--Auslesen der ersten Zeile in die 						--Variablen

		fetch next from c_deleted into @oid,@pid,@up,@qu,@d

					--Eintragen in die Archivtabelle
					--und zeilenweise Wiederholung
					--bis die Treffermenge durch ist
		while @@fetch_status=0
		begin
			insert into odarchiv
			values(@oid,@pid,@up,@qu,@d,suser_sname(),getdate())

			fetch next from c_deleted into @oid,@pid,@up,@qu,@d
		end

		close c_deleted
					--Speicherbereich freigeben
		deallocate c_deleted
	end

end

select * from [order details]
where orderid=	(	select max(orderid)
					from [order details])
	
select * from [order details]
where orderid=11077;


					--Test1: eine Zeile

delete from [order details] 
where orderid=11077 and productid=2

select * from odarchiv
					--Test2: mehrere Zeilen

delete from [order details] where orderid=11077

select * from odarchiv


select * from [order details]
where orderid=	(	select max(orderid)
					from [order details])

					--Test3: UPDATE
update [order details]
set unitprice=155
where orderid=11076
and productid=14

select * from odarchiv


