 select * from [order details]
where orderid=11077;

select unitprice, productname from products
where productid in(20, 8, 64, 2);

/************	DML-Anweisungen	***************/

INSERT INTO [order details]
VALUES(	11077, 25, 14, 50, .05); 


UPDATE	[order details]
SET			quantity=65
WHERE	orderid=11077
AND			productid=25;


DELETE FROM	[order details]
WHERE		orderid=11077
AND			productid=25;




select * from [order details]
where orderid=11077;

