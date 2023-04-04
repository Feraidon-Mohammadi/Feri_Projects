/*******	Erstellen eines benutzerdefinierten Datentyps vom Typ TABLE(Array)
			und Verwendung als Parameterdatentyp in einer Inline-Funktion
******************************************************************************/

create type catlist as table
(
	catid	int
);


CREATE FUNCTION UDF_Suppliers_Products
(@cat catlist readonly)
RETURNS table
AS
RETURN(
SELECT
  Products.ProductID
  ,Products.ProductName
  ,Products.CategoryID
  ,Products.QuantityPerUnit
  ,Products.UnitPrice
  ,Categories.CategoryName
  ,Suppliers.SupplierID
  ,Suppliers.CompanyName
  ,Suppliers.Address
  ,Suppliers.City
  ,Suppliers.PostalCode
  ,Suppliers.Country
  ,Suppliers.Phone
FROM
  Products
  INNER JOIN Categories
    ON Products.CategoryID = Categories.CategoryID
  INNER JOIN Suppliers
    ON Products.SupplierID = Suppliers.SupplierID
WHERE products.CategoryID IN(select catid from @cat)	);


declare @category catlist

insert into @category values(1), (2), (4)

select * from UDF_Suppliers_Products(@category);