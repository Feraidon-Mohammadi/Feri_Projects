USE NWMalz;

-- Primärschlüssel für alle Tabellen vergeben
ALTER TABLE categories
ADD PRIMARY KEY(CategoryID);

ALTER TABLE customers
ADD PRIMARY KEY(CustomerID);

ALTER TABLE employees
ADD PRIMARY KEY(EmployeeID);

ALTER TABLE [order details]
ADD PRIMARY KEY(OrderID, ProductID);

ALTER TABLE orders
ADD PRIMARY KEY(OrderID);

ALTER TABLE products
ADD PRIMARY KEY(ProductID);

ALTER TABLE shippers
ADD PRIMARY KEY(ShipperID);

ALTER TABLE suppliers
ADD PRIMARY KEY(SupplierID);


/*************/
/* Aufgabe 1 */
/*************/
CREATE TABLE SubCategories
(	SubCategoryID	INT				NOT NULL	IDENTITY
,	SubCategoryType	VARCHAR(20)		NOT NULL
,	CategoryID		INT				NOT NULL
,	[Description]	VARCHAR(250)	NULL
);


--          Überprüfung der Anweisungsblöcke    --/
SELECT * FROM SubCategories;                    --/
EXEC sp_helpconstraint SubCategories;           --/
--												--/


ALTER TABLE SubCategories
ADD			PRIMARY KEY(SubCategoryID),
CONSTRAINT	uq_sub_cat_type	UNIQUE(SubCategoryType),
CONSTRAINT	fk_subc_cat		FOREIGN KEY(CategoryID)	REFERENCES	categories;


ALTER TABLE products
ADD	SubCategoryID	INT		NULL;


--          Überprüfung der Anweisungsblöcke    --/
SELECT * FROM products;                    --/
EXEC sp_helpconstraint products;           --/
--												--/


ALTER TABLE products
ADD	FOREIGN KEY(SubCategoryID) REFERENCES categories;


/*************/
/* Aufgabe 2 */
/*************/
CREATE TABLE reclamation
(	ReclID			INT				NOT NULL
,	OrderID			INT				NOT NULL
,	Date_time		DATETIME		NOT NULL
,	[Description]	VARCHAR(250)	NOT NULL
);


--          Überprüfung der Anweisungsblöcke    --/
SELECT * FROM reclamation;                    --/
EXEC sp_helpconstraint reclamation;           --/
--												--/


ALTER TABLE	reclamation
ADD						PRIMARY KEY(ReclID),
CONSTRAINT	fk_recl_ord	FOREIGN KEY(OrderID)	REFERENCES	orders,
DEFAULT					GETDATE()				FOR			Date_time,
CHECK(ReclID LIKE	'%[0-9]-[0-9]');


/*************/
/* Aufgabe 3 */
/*************/
CREATE TABLE deliverycondition
(	SupplierID		INT			NOT NULL
,	ProductID		INT			NOT NULL
,	UnitPrice		MONEY		NULL
,	DaysGuarant		TINYINT		NULL
,	MinQuantity		TINYINT		NULL
);


--          Überprüfung der Anweisungsblöcke    --/
SELECT * FROM deliverycondition;                    --/
EXEC sp_helpconstraint deliverycondition;           --/
--


ALTER TABLE deliverycondition
ADD			PRIMARY KEY(SupplierID, ProductID),
CONSTRAINT	fk_dcon_supp	FOREIGN KEY(SupplierID) REFERENCES suppliers,
CONSTRAINT	fk_dcon_prod	FOREIGN KEY(ProductID) REFERENCES	products,
DEFAULT		1				FOR		MinQuantity,
CHECK(MinQuantity > 0),
CHECK(UnitPrice > 0),
CHECK(DaysGuarant >= 0);