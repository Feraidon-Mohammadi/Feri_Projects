use nwmewes;

select	orderid,
		customerid,
		orderdate,
		ShippedDate
into	#orders_OLAP		
from Orders		
where YEAR(OrderDate)=2022;


select * from #orders_OLAP;


select	orderid,
		customerid,
		orderdate,
		ShippedDate
into	#orders_OLTP		
from Orders		
where YEAR(OrderDate)=2022;


select * from #orders_OLTP;

select * from #orders_OLTP
where orderid<11070;


update #orders_OLTP
set shippeddate=orderdate+10
where orderid<11070
and shippeddate is null;




insert into #orders_OLTP
values('ANTON', GETDATE(), null);

insert into #orders_OLTP
values('FOLKO', GETDATE(), null);

insert into #orders_OLTP
values('QUICK', GETDATE(), null);

insert into #orders_OLTP
values('PICCO', GETDATE(), null);


select * from #orders_OLTP;

select * from #orders_OLAP;


MERGE #orders_OLAP AS target

USING  #orders_OLTP AS source

ON (target.orderid = source.orderid)
WHEN MATCHED						--and shippeddate is null
THEN 
    UPDATE SET shippeddate=source.shippeddate
WHEN NOT MATCHED 
THEN	
	INSERT 
	VALUES (source.customerid, source.orderdate, source.shippeddate)
;
--when not matched by source
--then delete;
	

select * from #orders_OLAP;	

