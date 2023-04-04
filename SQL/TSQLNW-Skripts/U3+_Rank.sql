select 	productname,
	categoryid,
	unitprice 
from products
order by unitprice desc;


select 	productname,
	categoryid,
	unitprice as unitprice1,
	rank() over(order by unitprice desc) as rank_position,
	dense_rank() over(order by unitprice desc) as denserank_position,
	row_number() over(order by unitprice desc) as row_position, 
	ntile(10) over(order by unitprice desc) as ntile_position10,
	unitprice as unitprice2,
	ntile(4) over(order by unitprice desc) as ntile_position4
from products;



select 	productname,
	categoryid,
	unitprice as unitprice1,
	rank() over(partition by categoryid order by unitprice desc) as rank_position,
	dense_rank() over(partition by categoryid order by unitprice desc) as denserank_position,
	row_number() over(partition by categoryid order by unitprice desc) as row_position, 
	ntile(10) over(partition by categoryid order by unitprice desc) as ntile_position10,
	unitprice as unitprice2,
	ntile(4) over(partition by categoryid order by unitprice desc) as ntile_position4
from products;



select	categoryname,
			companyname,
			productid,
			productname,
			unitprice,
			ntile(2) over(	partition by	categoryname
									order by unitprice desc) as preisgruppen
from		products p
join		categories c
on p.categoryid=c.categoryid
join		suppliers s
on p.supplierid=s.supplierid
