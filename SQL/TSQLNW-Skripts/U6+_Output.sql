use nwmewes

begin tran;

set nocount on

UPDATE TOP (10) products
SET unitprice = unitprice * 1.025 ;

rollback tran;




begin tran;

UPDATE TOP (10) products
SET unitprice = unitprice * 1.025 
OUTPUT		INSERTED.productid,
			INSERTED.productname,
			DELETED.unitprice as Preis_alt,
			INSERTED.unitprice as Preis_neu

rollback tran;



create table preishistory
(	prodid			int,
	prodname		varchar(50),
	priceold		money,
	pricenew		money,
	upddate			datetime,
	username		varchar(50));



begin tran

UPDATE TOP (10) products
SET unitprice = unitprice * 1.025 
OUTPUT	INSERTED.productid,
		INSERTED.productname,
		DELETED.unitprice,
		INSERTED.unitprice,
		getdate(),
		original_login()

INTO preishistory;



select * from preishistory;

rollback tran




insert into orders(customerid, orderdate)
output inserted.orderid
values('HUNGO', getdate())
;
