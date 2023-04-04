/***	Erstellen einer Kopie der Northwind-Datenbank
		ohne Constraints
		für die Unterrichtseinheit	SQL-Routinen	***/
		
create database NWMewes;
go

use NWMewes;

select *
into customers
from northwind.dbo.customers;		

select *
into orders
from northwind.dbo.orders;

select *
into [order details]
from northwind.dbo.[order details];

select *
into products
from northwind.dbo.products;

select *
into categories
from northwind.dbo.categories;

select *
into suppliers
from northwind.dbo.suppliers;

select *
into shippers
from northwind.dbo.shippers;

select *
into employees
from northwind.dbo.employees;