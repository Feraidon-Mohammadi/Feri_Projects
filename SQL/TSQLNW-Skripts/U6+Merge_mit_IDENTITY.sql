insert into shippers
values('CompX', null), ('CompY', null);

merge shippers2 as target
using shippers as source
on(target.shipperid=source.shipperid)
when not matched then
insert values(source.companyname, source.phone);






select productid, productname, supplierid, categoryid, quantityperunit,
		unitprice as listprice, unitsinstock, unitsonorder, reorderlevel,
		discontinued
into products2
from products;

insert into products(productname, quantityperunit, unitprice, discontinued)
values('Saufbier', '0.5ltr bottle', 1.11, 0);

merge products2
using products
on products2.productid=products.productid
when not matched then
insert (productname,
		quantityperunit,
		listprice,
		discontinued)
values(	products.productname, 
		products.quantityperunit,
		products.unitprice,
		products.discontinued);