create database kundeauftrag;

use kundeauftrag;

CREATE SCHEMA REF;

CREATE TABLE ref.kunde
(KNr			int			NOT NULL
,Firma			varchar(80)	NOT NULL
,status			tinyint		NULL	CHECK(status IN(10,20,30,40,50))
,ort			varchar(50)	NOT NULL
,PRIMARY KEY(KNr)
);



CREATE TABLE ref.auftrag
(ANr			int		NOT NULL	IDENTITY(100,1)
,KNr			int		NOT NULL
,ADatum	smalldatetime	NOT NULL	DEFAULT GETDATE()
,LDatum	smalldatetime	NULL
,PRIMARY KEY(ANr)
,FOREIGN KEY(KNr) REFERENCES ref.kunde(KNr)
,CHECK(ldatum>=adatum)
);


select * from ref.kunde;
select * from ref.auftrag;

insert into ref.auftrag values(1, getdate(), null);


insert into ref.kunde values(1, 'Adelmüller', 20, 'München')
insert into ref.kunde values(4, 'Distel', 10, 'Bonn')
insert into ref.kunde values(5, 'Enrico', 20, 'Berlin')

select * from ref.kunde

insert into ref.auftrag values(1, getdate(), null)
insert into ref.auftrag values(5, getdate(), null)
insert into ref.auftrag values(3, getdate(), null)

select * from ref.kunde
select * from ref.auftrag

delete from ref.kunde where knr=1
delete from ref.kunde where knr=4

delete from ref.auftrag where anr=102


exec sp_helpconstraint 'ref.auftrag'


alter table ref.auftrag
drop constraint FK__auftrag__KNr__1ED998B2




update	ref.auftrag
set		knr=5
where	anr=104

select * from ref.kunde
select * from ref.auftrag

alter table ref.auftrag with nocheck
add constraint fk_auftrag_knr	
foreign key(knr) references ref.kunde



