----------------------------------JOIN-Wiederholung


						--für die Rechnung der Bestellung
						--Nr. 10999
select	o.orderid,	orderdate, 
		o.customerid,
		od.productid, 
		od.unitprice, quantity, discount,
		convert(money, od.unitprice*quantity*(1-discount)) as linetotal
from	[order details] od
join	orders o
on		o.orderid=od.orderid
where	o.orderid=10999;	



						--SQL89
select	o.orderid,	orderdate, 
		o.customerid,
		od.productid, 
		od.unitprice, quantity, discount,
		convert(money, od.unitprice*quantity*(1-discount)) as linetotal

from	[order details] od, orders o
where	o.orderid=od.orderid

and		o.orderid=10999	
;


						--für die Rechnung der Bestellung
						--Nr. 10999
select	o.orderid,	orderdate, 
		c.customerid,
		companyname, 
		address, postalcode, city,
		p.productid, 
		productname, quantityperunit,
		od.unitprice, quantity, discount,
		convert(money, od.unitprice*quantity*(1-discount)) as linetotal
from	products p 
join	[order details] od
on		p.productid=od.productid
join	orders o
on		o.orderid=od.orderid
join	customers c
on		c.customerid=o.customerid
where	o.orderid=10999	



						--SQL89
select	o.orderid,	orderdate, 
		c.customerid,
		companyname, 
		address, postalcode, city,
		p.productid, 
		productname, quantityperunit,
		od.unitprice, quantity, discount,
		convert(money, od.unitprice*quantity*(1-discount)) as linetotal

from	products p, [order details] od, orders o, customers c
where	o.orderid=10999
and		p.productid=od.productid
and		o.orderid=od.orderid
and		c.customerid=o.customerid	



						--SQL92
						--wie es nicht funktioniert
select	o.orderid,	orderdate, 
		c.customerid,
		companyname, 
		address, postalcode, city,
		p.productid, 
		productname, quantityperunit,
		od.unitprice, quantity, discount,
		convert(money, od.unitprice*quantity*(1-discount)) as linetotal

from	products p join ([order details] od join (orders o join customers c
on		p.productid=od.productid)
on		o.orderid=od.orderid)
on		c.customerid=o.customerid

where	o.orderid=10999
order by o.orderid;


						--SQL92
						--wie mans machen kann
select	o.orderid,	orderdate, 
		c.customerid,
		companyname, 
		address, postalcode, city,
		p.productid, 
		productname, quantityperunit,
		od.unitprice, quantity, discount,
		convert(money, od.unitprice*quantity*(1-discount)) as linetotal

from	products p join [order details] od join orders o join customers c
on		c.customerid=o.customerid
on		o.orderid=od.orderid
on		p.productid=od.productid

where	o.orderid=10999
;


						--die Outer Joins
							--left
							--right
							--full


						--Inner					
select	employeeid
		, lastname
		, e.city
		, customerid
		, companyname
		, c.city
from	employees e inner join customers c 
on		e.city=c.city


						--Left
select	employeeid
		, lastname
		, e.city
		, customerid
		, companyname
		, c.city
from	employees e left outer join customers c 
on		e.city=c.city

						--Left
						--mit WHERE-Klausel
select	employeeid
		, lastname
		, e.city
		, customerid
		, companyname
		, c.city
from	employees e left outer join customers c 
on		e.city=c.city
where	c.city is null


						--Right
select	employeeid
		, lastname
		, e.city
		, customerid
		, companyname
		, c.city
from	employees e right join customers c 
on		e.city=c.city


						--Full
select	employeeid
		, lastname
		, e.city
		, customerid
		, companyname
		, c.city
from	employees e full join customers c 
on		e.city=c.city


									--SelfJoin
select	mgr.employeeid,
		mgr.title,
		concat(mgr.lastname,', ',mgr.firstname) as manager,
		emp.employeeid,
		emp.title,
		concat(emp.lastname,', ',emp.firstname) as agent
from	employees as mgr
join	employees as emp
on		emp.reportsto=mgr.employeeid
order by mgr.employeeid;


select * from employees;

select	concat(e2.lastname,', ',e2.firstname) as agent,
		e2.hiredate
from	employees e1
join	employees e2
on		year(e1.hiredate)=year(e2.hiredate)
--and		e1.employeeid<e2.employeeid
where	e1.lastname='King'
and		e2.lastname<>'King';

select	concat(e2.lastname,', ',e2.firstname) as agent,
		e2.hiredate
from	employees e1
join	employees e2
on		year(e1.hiredate)=year(e2.hiredate)
and		e1.employeeid<>e2.employeeid
where	e1.lastname='King'
--and		e2.lastname<>'King';

		