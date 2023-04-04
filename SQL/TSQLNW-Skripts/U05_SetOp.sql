 --Mengenoperatoren

use northwind;
go

							--UNION

					--alle Adressdaten in einer
					--Adresstabelle konsolidieren

select	city, address, postalcode, 'Kundenadresse' as herkunft
--into adresstabelle
from	customers

union all

select	city, address, postalcode, 'Mitarbeiteradresse' as addresstyp
from	employees

union all

select  city, address,  postalcode, 'Lieferantenadresse'
from	suppliers

;


select * from adresstabelle;

exec sp_spaceused 'adresstabelle';

if exists(select * from sys.tables where name='adresstabelle')

	drop table adresstabelle;




					--Aggregate nach verschiedenen Gruppierungen
select	year(orderdate) as jahr,
		shipcountry,
		customerid,
		sum(unitprice*quantity*(1-discount)) as umsatz
from	orders
join	[order details] od
on 		orders.orderid=od.orderid
group by	year(orderdate),
			shipcountry,
			customerid

union

select	year(orderdate),
		null,
		customerid, 
		sum(unitprice*quantity*(1-discount)) as umsatz
from	orders
join	[order details] od
on 		orders.orderid=od.orderid
group by	year(orderdate),
			customerid

union

select	null,
		shipcountry,
		null,
		sum(unitprice*quantity*(1-discount)) as umsatz
from	orders
join	[order details] od
on 		orders.orderid=od.orderid
group by	shipcountry;





				--Verhalten von

						--UNION

select postalcode, city, address, customerid
from customers

union									--97

select	shippostalcode,
		shipcity,
		shipaddress,
		customerid
from orders
order by customerid

						--UNION ALL

select postalcode, city, address, customerid
from	customers

union all								--921

select	shippostalcode,
		shipcity,
		shipaddress,
		customerid
from	orders
order by customerid;

						--INTERSECT

select postalcode, city, address, customerid
from	customers

intersect 						--83 

select	shippostalcode,
		shipcity,
		shipaddress,
		customerid
from	orders
order by 4;

						--EXCEPT

select postalcode, city, address, customerid
from	customers

except							--8	

select	shippostalcode,
		shipcity,
		shipaddress,
		customerid
from	orders
order by 4;

						--EXCEPT 	reverse

select shippostalcode,
		shipcity,
		shipaddress,
		customerid
from	orders

except							--6

select postalcode, city, address, customerid
from	customers
order by 4;





--Vereinigung beider Mengendifferenzen(entspr. XOR)
--!!!Klammern müssen sein

--	A and not B		or		B and not A

--	oder

--	A or B		and not		A and B


(select postalcode, city, address, customerid
from	customers

except

select	shippostalcode,
		shipcity,
		shipaddress,
		customerid
from	orders)

union
			
(select shippostalcode,
		shipcity,
		shipaddress,
		customerid
from	orders

except

select postalcode, city, address, customerid
from		customers)
order by 4;


--ODER



(	select postalcode, city, address, customerid
	from customers

	union									--97

	select	shippostalcode,
			shipcity,
			shipaddress,
			customerid
	from orders
)

except


(	select postalcode, city, address, customerid
	from	customers

	intersect						--83 

	select	shippostalcode,
			shipcity,
			shipaddress,
			customerid
	from	orders
)
order by 4
;



--Median

select	top(50) percent
		*
from	products
order by unitprice asc

intersect

select	top(50) percent
		*
from	products
order by unitprice desc;



with cte_unter_median
as(
	select	top(50) percent
			*
	from	products
	order by unitprice asc
),
	cte_ueber_median
as(
	select	top(50) percent
			*
	from	products
	order by unitprice desc
)
select * from cte_unter_median
intersect
select * from cte_ueber_median;


with cte_unter_median
as(
	select	top(50) percent
			*
	from	orders
	order by orderdate asc
),
	cte_ueber_median
as(
	select	top(50) percent
			*
	from	orders
	order by orderdate desc
)
select * from cte_unter_median
intersect
select * from cte_ueber_median;




with cte_unter_median
as(
	select	top(50.1) percent
			*
	from	orders
	order by orderdate asc
),
	cte_ueber_median
as(
	select	top(50.1) percent
			*
	from	orders
	order by orderdate desc
)
select * from cte_unter_median
intersect
select * from cte_ueber_median;