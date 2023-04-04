--Schutzlose Daten

use nwmewes;


insert into department					--5mal ausführen
values('A04', 'Shopping', default, default, default);

select * from department;

select deptid, count(*)
from department
group by deptid
having count(*)>1

delete from department where deptid='A04'

update department
set deptname='Purchasing'
where deptid='A04'

delete top (4) from department where deptid='A04'	--neu in SQL Server 2005





ALTER TABLE department
ADD CONSTRAINT PK_department PRIMARY KEY(deptid)

ALTER TABLE department
ADD UNIQUE(deptname)

ALTER TABLE department
ADD		CONSTRAINT PK_department PRIMARY KEY(deptid),
		CONSTRAINT UQ_department UNIQUE(deptname)

exec sp_helpconstraint department



ALTER TABLE supplyconditions
ADD PRIMARY KEY(supplierid, productid)


--Tabelle mit Primärschlüssel und Alternativschlüssel

--Bsp. 1:	Personal in einem Fuhrunternehmen

CREATE TABLE personal
(	PersNr			char(7)			NOT NULL 	PRIMARY KEY
,	FName			varchar(30)		NOT NULL
,...
,	FuehrerscheinID	char(20)			NULL	UNIQUE	
,...
)



--Bsp. 2:	Patienten einer Klinik

CREATE TABLE patient
(patientid		int				NOT NULL	IDENTITY
,fname			varchar(30)		NULL
,vname			varchar(40)		NULL
,geburtsdatum	smalldatetime	NULL
,strasse		...
,plz			...
,SVNummer		char(20)		null
,...
,PRIMARY KEY(patientid)
,UNIQUE(fname, vname, geburtsdatum)
,unique(SVNummer)
,...
)


--Bsp. 3	:	Stundenplanung

CREATE TABLE stundenplanung
(dozentid		char(5)		NULL
,raumid			char(3)		NULL
,fachid			char(5)		NOT NULL
,kursid			char(7)		NOT NULL
,wochentag		char(2)		NOT NULL
,uhrzeit		time		NULL
,UNIQUE(raumid, wochentag, uhrzeit)
,UNIQUE(dozentid, wochentag, uhrzeit)
)



