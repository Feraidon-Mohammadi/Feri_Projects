
exec sp_helpconstraint departments;

exec sp_help supplyconditions;

alter table department
add	check(budget between 0 and 2000000),
	check(deptlocationid in(1,2,3,4,7,12));

alter table supplyconditions
add	constraint ck_supplcond_days check(days between 0 and 14),
	constraint ck_supplcond_price check(price>=0);
		
		


alter table customers
add primary key(customerid);

create table orders2
(	orderid			int			not null	identity		primary key,
	customerid		nchar(5)	not null	references customers,
	orderdate		datetime	not null	default getdate(),
	shipdate		datetime	null,	
	check(shipdate>=orderdate)
	/* or shipdate is null)*/
);		









--Prüfbedingung

--Vergleichsoperatoren <, >, >=, <=, <>, =} Theta

ALTER TABLE dbo.t_lager
ADD CHECK(flaeche>0)

ALTER TABLE dbo.t_auftrag
ADD CHECK(lieferdatum>=auftragsdatum OR lieferdatum IS NULL)

--Logische Operatoren AND, OR, NOT

ALTER TABLE dbo.t_lager
ADD CHECK(flaeche>=1000 AND flaeche<=200000)

ALTER TABLE dbo.t_weinsorten
ADD CHECK	(	herkunft='Italien' OR 
				herkunft='Frankreich' OR 
				herkunft='Spanien')

--Prädikate

--Geschlossene Intervalle mit BETWEEN

ALTER TABLE dbo.t_lager
ADD CHECK(flaeche BETWEEN 1000 AND 200000)

ALTER TABLE dbo.bestellungen2000
ADD CHECK(bestelldatum BETWEEN '1.1.2000' AND '31.12.2000 23:59')

ALTER TABLE dbo.bestellungen_seit_2000
ADD CHECK(bestelldatum BETWEEN '1.1.2000' AND GETDATE())


--Aufzählungen mit IN

ALTER TABLE dbo.t_weinsorten
ADD CHECK(herkunft IN('Italien', 'Frankreich', 'Spanien'))

ALTER TABLE dbo.t_weinsorten
ADD CHECK(fuellmenge IN(0.25, 0.75, 0.5, 1, 1.5, 2, 5, 0.375))

--Textmuster mit LIKE
--anwendbar NUR auf die Datentypen 	CHAR, VARCHAR, TEXT
--					NCHAR, NVARCHAR, NTEXT
--erlaubt die Verwendung von Platzhaltern
--		%	für beliebig viele Zeichen
--		_	genau ein Zeichen
--		[]	kann eine Aufzählung oder einen Bereich
--			zulässiger Zeichen für eine Stelle maskieren


ALTER TABLE lexikon_A
ADD CHECK(stichwort LIKE 'A%')

ALTER TABLE lexikon_A_bis_F
ADD CHECK(stichwort LIKE '[A-F]%')

ALTER TABLE lexikon_A_oder_F
ADD CHECK(stichwort LIKE '[AF]%')

ALTER TABLE lexikon_A_oder_F
ADD CHECK(stichwort LIKE 'AF%')



ALTER TABLE personen
ADD CHECK(PLZ LIKE '[0-9][0-9][0-9][0-9][0-9]')




ALTER TABLE personen
ADD CHECK(	PLZ LIKE 'D-[0-9][0-9][0-9][0-9][0-9]' OR
			PLZ LIKE 'A-[0-9][0-9][0-9][0-9]' OR
			PLZ LIKE 'CH-[0-9][0-9][0-9][0-9]')


ALTER TABLE kennwortmerker
ADD CHECK(kennwort LIKE '________%')





ALTER TABLE buchausgabe
ADD CHECK(		isbn LIKE '[0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9]-[0-9A-Z]' OR
				isbn LIKE '[0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]-[0-9A-Z]'	





/***	UDT = Userdefined Data Type
		Benutzerdefinierter Datentyp
		Quasi:	eine CHECK-Klausel wird nicht an eine Spalte in einer Tabelle
		gebunden, sondern
		an einen Datentypen, und steht damit über die gesamte 
		Datenbank hinweg zur Verfügung
***/

-- nach SQL Standard

CREATE DOMAIN typ_PLZ char(5)
CHECK(typ_PLZ LIKE '[0-9][0-9][0-9][0-9][0-9]')

-- nach Microsoft Transact-SQL

exec sp_addtype typ_PLZ, 'char(5)'

--seit SQLServer2005:

CREATE TYPE typ_PLZ FROM char(5)
go
CREATE RULE regel_PLZ AS @regel_PLZ like '[0-9][0-9][0-9][0-9][0-9]'
go
exec sp_bindrule regel_PLZ, typ_PLZ

create table adressen
(ID			int				not null identity
,PLZ		typ_PLZ			null
,Ort		varchar(50)		not null
,strasse	varchar(70)		null
)	

exec sp_help adressen

exec sp_helptype		--gibts nicht mehr

insert into adressen values('07749', 'Jena', 'Löbstedter Str.')

insert into adressen values('077', 'Jena', 'Löbstedter Str.')

select * from adressen


--Ändern eines UDT

exec sp_unbindrule typ_PLZ;

drop rule regel_PLZ;

CREATE RULE regel_PLZ AS @regel_PLZ like '[0-9][0-9][0-9][0-9][0-9]' or 
						 @regel_PLZ like '[0-9][0-9][0-9][0-9]';
														
exec sp_bindrule regel_PLZ, typ_PLZ;														


















 
drop table dbo.projekt

select * from projekt

exec sp_help projekt