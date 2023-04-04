select	employeeid
		, firstname
		, lastname
		, reportsto
from	employees;

alter table employees
add foreign key(reportsto) references employees;

