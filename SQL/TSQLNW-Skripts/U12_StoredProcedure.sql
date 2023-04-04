create procedure usp_jahr_lfland
(@jahr	smallint)
as
begin
	select 	shipcountry,
			year(orderdate) as jahr,
			datepart(q, orderdate) as quartal,
			sum(UnitPrice*Quantity*(1-Discount)) as umsatzsumme, 
			count(distinct od.orderid)		as anzahl_bestellungen
	from 	[order details] od
	join 	orders o
	on 		o.orderid=od.orderid

	where 	year(orderdate)=@jahr

	group by	shipcountry,
				year(orderdate), 
				datepart(q, orderdate)
	
end;



execute usp_jahr_lfland 2020;

exec usp_jahr_lfland @jahr=2020;

exec usp_jahr_lfland @jahr=2020;

exec usp_jahr_lfland;

exec usp_jahr_lfland default;





create procedure usp_jahr_lfland_if
@jahr	smallint=null
as
begin
	if not exists(	select * from orders
					where year(orderdate)=@jahr) 
		and @jahr is not null
	begin
		raiserror('Sie haben ein Jahr angegeben, in dem nichts bestellt wurde', 10, 1);
		return;
	end;

	if @jahr is null
		select 	shipcountry,
				year(orderdate) as jahr,
				datepart(q, orderdate) as quartal,
				sum(UnitPrice*Quantity*(1-Discount)) as umsatzsumme, 
				count(od.orderid)		as anzahl_bestellposten
		from 	[order details] od
		join 	orders o
		on 		o.orderid=od.orderid
									--WHERE-Klausel weggelassen
		group by	shipcountry,
					year(orderdate), 
					datepart(q, orderdate);
	else
		select 	shipcountry,
				year(orderdate) as jahr,
				datepart(q, orderdate) as quartal,
				sum(UnitPrice*Quantity*(1-Discount)) as umsatzsumme, 
				count(od.orderid)		as anzahl_bestellposten
		from 	[order details] od
		join 	orders o
		on		o.orderid=od.orderid

		where 	year(orderdate)=@jahr

		group by	shipcountry,
					year(orderdate), 
					datepart(q, orderdate);
end;

exec usp_jahr_lfland_if 2020;

exec usp_jahr_lfland_if @jahr=2021;

exec usp_jahr_lfland_if @jahr=1968;

exec usp_jahr_lfland_if;


/******************	Übergabe von Textfragmenten
							in varchar-Parametern
*************************************************************************/							
create procedure usp_show_shippers
@comp		varchar(50)='%'
as
select * from shippers
where companyname like '%'+@comp+'%';





exec usp_show_shippers;

exec usp_show_shippers 'pack';


/**********	Microsoft empfiehlt jedoch selbst,
			Prozeduren, die einen einzelnen Wert
			oder eine tabellarische Ergebnismenge
			erzeugen,
			in eine benutzerdefinierte Skalarfunktion
			oder Funktion mit Tabellenrückgabe
			umzuschreiben
****************************************************/


/**********	Das wichtigste Einsatzgebiet 
			für Stored Procedures ist 
			(in allen relationalen DBMS)
			das Ausführen von DML-Operationen			
****************************************************/

							--UPDATE ganz ohne Fehlerüberprüfung

create procedure usp_upd_listenpreis
@productid	int,
@preisneu	money
as
begin
	update	products
	set		unitprice=@preisneu
	where	productid=@productid;
end;	



					select	productid, productname, unitprice
					from	products
					where	productid>70;

exec usp_upd_listenpreis 71, 22;

exec usp_upd_listenpreis	@productid=72,
							@preisneu=35;

exec usp_upd_listenpreis 73;


begin tran
	exec usp_upd_listenpreis 74, 50;
	
	select productid, productname, unitprice
	from products
	where productid>70;
rollback tran




								--Überprüfen auf zwei Standardfehler:
								--zu wenig Parameter
								--keine gültige ProduktID

alter procedure usp_upd_listenpreis
@productid	int		=null,
@preisneu	money	=null
as
begin
	declare @meldung varchar(100);

	if	@productid is null or @preisneu is null
		begin
			set @meldung='Sie müssen sowohl eine gültige ProduktID als auch einen neuen Preis angeben';
			raiserror(@meldung, 15, 1);
			return;
		end;
		
	if not exists(	select * from products
					where productid=@productid)
		begin
			set @meldung='	Es gibt kein Produkt mit dieser ID. Versuchen Sie es noch einmal.';
			raiserror(@meldung, 15, 1);
			return;	
	
		end;							

	update	products
	set		unitprice=@preisneu
	where	productid=@productid;
end;

						select	productid, productname, unitprice
						from	products
						where	productid>70;
						
exec usp_upd_listenpreis 73;										

exec usp_upd_listenpreis 93, 22;

exec usp_upd_listenpreis	@productid=72,
							@preisneu=34.50;
							
							


						--Abfangen einer zu drastischen Preiserhöhung
						--(in einem Schritt)

alter procedure usp_upd_listenpreis
@productid	int		=null,
@preisneu	money	=null
as
begin
	set nocount on;
	declare @meldung varchar(400);
	declare @preisalt money;

					
	if	@productid is null or @preisneu is null
		begin
			set @meldung='	Sie müssen sowohl eine gültige ProduktID als auch einen neuen Preis angeben';
			raiserror(@meldung, 15, 1);
			return;
		end;
		
	if not exists(	select * from products
			where productid=@productid)
		begin
			set @meldung='	Es gibt kein Produkt mit dieser ID. Versuchen Sie es noch einmal.';
			raiserror(@meldung, 15, 1);
			return;	
	
		end;
	
	set @preisalt=(	select unitprice from products
					where productid=@productid);
					
	if (@preisneu>=@preisalt*2)
	begin
			set @meldung='	Der neue Preis den Sie angegeben haben ist mindestens doppelt so hoch wie der alte. Laut Firmenrichtlinie XY ist das sittenwidrig. 	Die Aktion wurde abgebrochen.';
			raiserror(@meldung, 15, 1);
			return;	
	
	end;													

							--eigentliche Transaktion
	update products
	set unitprice=@preisneu
	where productid=@productid;
end;



						select productid, productname, unitprice
						from products
						where productid>70;
										
exec usp_upd_listenpreis 74, 50;

exec usp_upd_listenpreis	@productid=72,
							@preisneu=34.80;
							



						--falls die ProduktID nicht bekannt ist
						--kann auch das Anfangsfragment des Produktnamens
						--eingegeben werden

alter procedure usp_upd_listenpreis
@productid	int		=null,
@prodname	varchar(50)	=null,
@preisneu	money		=null
as
begin
	declare @meldung varchar(400);
	declare @preisalt money;

					
	if	not(	(@productid is not null and @preisneu is not null) or 
				(@prodname is not null and @preisneu is not null)
			)
		begin
			set @meldung='	Sie müssen sowohl eine gültiges Produkt	als auch einen neuen Preis angeben';
			raiserror(@meldung, 15, 1);
			return;
		end;
		
	if not exists(	select * from products
					where productid=@productid) and @prodname is null
	begin
			set @meldung='	Es gibt kein Produkt mit dieser ID. Versuchen Sie es noch einmal.';
			raiserror(@meldung, 15, 1);
			return;	
	
	end;

	if @productid is  not null and @prodname is not null
		begin
			set @meldung='	Bitte übergeben Sie entweder ProductID oder Productname';
			raiserror(@meldung, 15, 1);
			return;	
	end;
		
	
	set @preisalt=(	select unitprice from products
					where productid=@productid
					or productname like '%'+@prodname+'%')
	
					
	if (@preisneu>=@preisalt*2)
	begin
			set @meldung='	Der neue Preis den Sie angegeben haben ist mindestens doppelt so hoch wie der alte. Laut Firmenrichtlinie XY ist das sittenwidrig. 	Die Aktion wurde abgebrochen.';
			raiserror(@meldung, 15, 1);
			return;	
	
	end;													

							--eigentliche Transaktion
	if @productid is not null
		update products
		set unitprice=@preisneu
		where productid=@productid;
	else
		update products
		set unitprice=@preisneu
		where productname like '%'+@prodname+'%';
	
end;


						select productid, productname, unitprice
						from products
						where productid>70;
							
exec usp_upd_listenpreis	@prodname='Lakka',
							@preisneu=18.70;
							
exec usp_upd_listenpreis	@productid=72,
							@preisneu=35.99;		
							
exec usp_upd_listenpreis	@productid=72;

exec usp_upd_listenpreis	@preisneu=35;

exec usp_upd_listenpreis	@productid=72,
							@preisneu=35,
							@prodname='Lakka';





						--Prozedur mit DELETE
						--und Überprüfen der beiden Standardfehler
						--Überprüfen auf zwei Standardfehler:
						--zu wenig Parameter
						--keine gültige ProduktID
create procedure usp_del_odetails
@orderid	int		=null,
@productid	int		=null
as
begin
	declare @meldung varchar(300);

	if	@productid is null or @orderid is null
		begin
			set @meldung='	Sie müssen sowohl eine gültige OrderID als auch eine gültige ProduktID angeben';
			raiserror(@meldung, 15, 1);
			return;
		end;
		
	if not exists(	select * from [order details]
					where orderid=@orderid
					and	productid=@productid)
		begin
			set @meldung='	Es gibt keine Bestellposition mit diesen ID. Versuchen Sie es noch einmal.';
			raiserror(@meldung, 15, 1);
			return;	
		end;							

	delete from [order details]
	where orderid=@orderid
	and productid=@productid;
end;


							select *
							from [order details]
							where orderid=11000;
							
exec usp_del_odetails 11000;										

exec usp_del_odetails 11000, 22;

exec usp_del_odetails @productid=72;

begin tran
	exec usp_del_odetails 11000, 24;
	
	select *	from [order details]	
	where orderid=11000;

rollback tran;	




						--Prozedur mit INSERT
						--mit Auslassung der Spalte ProductID
						--weil sie eine IDENTITY-Spalte ist
						--und geeigneter Vorbelegung
						--für bestimmte Spalten
create procedure usp_ins_products
@prodname		nvarchar(40)	=null,
@supplierid		int				=null,
@categoryid		int				=null,
@qperunit		nvarchar(20)	=null,
@unitprice		money			=null,
@unitsinstock	smallint		=0,
@unitsonorder	smallint		=0,
@reorderlevel	smallint		=null,
@discontinued	bit				=0
as
begin
	if	@prodname is null
		begin
			raiserror('Sie müssen mindestens eine Produktbezeichnung angeben', 15, 1);
			return;
		end;
		
	insert into products
	(	productname, supplierid, categoryid,
		quantityperunit, unitprice,
		unitsinstock, unitsonorder, reorderlevel,
		discontinued	)
	values(	@prodname, @supplierid, @categoryid,
			@qperunit, @unitprice,
			@unitsinstock, @unitsonorder, @reorderlevel,
			@discontinued	); 
end;

						select *
						from products
						where productid>=70;
										
exec usp_ins_products;										

exec usp_ins_products 'Bördeländer Grünkohl';

exec usp_ins_products 'Griesson Hagebuttenplätzchen', 19, 4, '500g Pack.', 8.99;

exec usp_ins_products	@prodname='Altenburger Klarsichttöter', 
						@categoryid=1, 
						@unitprice=1.99,
						@unitsinstock=200;
																																				--geht
exec usp_ins_products 'Griesson Kürbiskuchen', 19, 4, '500g Pack.', 8.99, @reorderlevel=5;
																																				--geht nicht
exec usp_ins_products @prodname='Bierbowle', 21, 1, '500l Kessel.', 99.99, @reorderlevel=5;
						
						





						--Prozedur mit Transaktion
						--mit Auslassung der Spalte ProductID
						--weil sie eine IDENTITY-Spalte ist
						--und geeigneter Vorbelegung
						--für bestimmte Spalten

create procedure usp_ins_odetails
@orderid	int		=null,
@productid	int		=null,
@quantity	smallint	=1,
@discount	real		=0
as
begin
	declare @meldung varchar(300);
					
	if	@productid is null or @orderid is null
		begin
			set @meldung='	Sie müssen sowohl eine gültige OrderID als auch eine gültige ProduktID angeben';
			raiserror(@meldung, 15, 1);
			return;
		end;
		
		
	begin transaction
		insert into [order details]
		values(		@orderid, 
						@productid, 
						(select unitprice from products where productid=@productid), 
						@quantity, 
						@discount);
		
		update products
		set unitsonorder=unitsonorder+@quantity
		where productid=@productid;
	commit transaction;
end;	

						select *
						from [order details]
						where orderid=11076;
						
						select	productid, productname, unitprice, unitsonorder
						from products
						where productid=3;
						
exec usp_ins_odetails	11076, 3;	


create procedure usp_ins_odetails
@orderid	int		=null,
@productid	int		=null,
@quantity	smallint	=1,
@discount	real		=0
as
begin
	declare @meldung varchar(300);
					
	if	@productid is null or @orderid is null
		begin
			set @meldung='	Sie müssen sowohl eine gültige OrderID als auch eine gültige ProduktID angeben';
			raiserror(@meldung, 15, 1);
			return;
		end;
		
	begin try		
	begin transaction
		insert into [order details]
		values(		@orderid, 
						@productid, 
						(select unitprice from products where productid=@productid), 
						@quantity, 
						@discount);
		
		update products
		set unitsonorder=unitsonorder+@quantity
		where productid=@productid;
	commit transaction;
	end try
	begin catch

		if xact_state()=-1
			rollback transaction;

		print error_message();

	end catch;

end;




create procedure usp_andere_lieferadresse  
@orderid		int		=null,
@shipname		varchar(40)	=null,
@shipaddress	varchar(60)	=null,
@shipcity		varchar(15	)=null,
@shipregion		varchar(15	)=null,
@shippostalcode	varchar(10)	=null,
@shipcountry	varchar(15)	=null
as
begin
		if @orderid is null
			begin
				raiserror('Geben Sie eine Bestellnummer an', 15, 1);
				return;
			end;
		
		update	orders
		set		shipname=@shipname,
				shipaddress=@shipaddress,
				shipcity=@shipcity,
				shipregion=@shipregion,
				shippostalcode=@shippostalcode,
				shipcountry=@shipcountry	
		where	orderid=@orderid	
end




begin tran

select * from orders where orderid=11000

execute usp_andere_lieferadresse	@orderid=11000,
									@shipaddress='23 Santa Clara Ave SE'
									

select * from orders where orderid=11000

rollback tran


alter procedure usp_andere_lieferadresse
@orderid		int		=null,
@shipname		varchar(40)	=null,
@shipaddress		varchar(60)	=null,
@shipcity		varchar(15	)=null,
@shipregion		varchar(15	)=null,
@shippostalcode	varchar(10)	=null,
@shipcountry		varchar(15)	=null
as
begin
		if @orderid is null
			begin
				raiserror('Geben Sie eine Bestellnummer an', 15, 1);
				return;
			end;
		
		update	orders
		set		shipname=		case when @shipname is null then shipname
								else @shipname end,
				shipaddress=	case when @shipaddress is null then shipaddress
								else @shipaddress end,
				shipcity=		case when @shipcity is null then shipcity
								else @shipcity end,
				shipregion=		case when @shipregion is null then shipregion
								else @shipregion end,
				shippostalcode=	case when @shippostalcode is null then shippostalcode
								else @shippostalcode end,
				shipcountry=	case when @shipcountry is null then shipcountry
								else @shipcountry 
				end
		where	orderid=@orderid	
end


alter procedure usp_andere_lieferadresse
@orderid		int		=null,
@shipname		varchar(40)	=null,
@shipaddress	varchar(60)	=null,
@shipcity		varchar(15	)=null,
@shipregion		varchar(15	)=null,
@shippostalcode	varchar(10)	=null,
@shipcountry		varchar(15)	=null
as
begin
		if @orderid is null
			begin
				raiserror('Geben Sie eine Bestellnummer an', 15, 1);
				return;
			end;
		
		update	orders
		set		shipname=		coalesce(@shipname, shipname),
				shipaddress=	coalesce(@shipaddress, shipaddress),
				shipcity=		coalesce(@shipcity, shipcity),
				shipregion=		coalesce(@shipregion, shipregion),
				shippostalcode=	coalesce(@shippostalcode, shippostalcode),
				shipcountry=	coalesce(@shipcountry, shipcountry)	
		where	orderid=@orderid	
end
															

execute usp_andere_lieferadresse	@orderid=11000,
									@shipaddress='23 Santa Clara Ave SE'

select * from orders where orderid=11000;