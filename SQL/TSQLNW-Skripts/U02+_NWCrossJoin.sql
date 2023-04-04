select * from customers			--91
select * from orders			--830
select * from [order details]	--2155
select * from products			--77

select * from customers, orders, [order details], products;

--1min: 3152814

select	convert(bigint,91)*830*2155*77 as Zeilen,
		round((8*1024/77+24*1024/91+160*1024/830+72*1024/2155)*12533070550/1024/1024/1024, 0) as GigaByte,
		12533070550/3152814/60/24 as Tage

-------------------------------------------------------Erzeugung von Testdaten

select		orders.orderid, orderdate, customerid, shipcity,
			productid, unitprice, quantity 
into		orders_cross_test
from		orders cross join [order details]


select * from orders_cross_test where customerid='ALFKI';


drop table orders_cross_test;

--------------------------------------------Ermitteln verdächtiger Sitzungen

select	session_id,
			reads,
			row_count,
			start_time,
			command,
			status,
			suser_name(user_id),
			db_name(database_id)
from sys.dm_exec_requests
where status<>'background'

