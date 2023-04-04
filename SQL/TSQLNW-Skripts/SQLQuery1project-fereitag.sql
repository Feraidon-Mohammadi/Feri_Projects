create database Feriproject;
use FeriProject
go

create table obst (
	obsttableid		int				not null	primary key,
	obstpreis		decimal(5, 2)	not null,
	color			varchar(50)			null,
	obstnr			int				not null,
	foreign key (obstnr)  references gemuese
)
select * from obst 
update 

;

--drop table obst;
--delete from obst


create table gemmuese (
	gemueseid		int			not null	primary key,
	gemueseprice	money		not null,
	gemuesename		varchar(50)		null,
	rezept			int			not null,	
	foreign key(rezept)			references zutate
);
--drop table gemmuese;



create table zutate (
	zutatenid			int			not null	primary key,
	gemueseid			int			not null,
	veranestalltung		varchar(70)		null,
	obsttableid			int			not null,
	
	foreign key (obsttableid)	references  obst,
);

--drop table zutate;




select * from obst




select * from gemmuese


select * from zutate




















--#########################################################################
CREATE TABLE table1 (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  table2_id INT,
  FOREIGN KEY (table2_id) REFERENCES table2(id)
);

CREATE TABLE table2 (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  table3_id INT,
  FOREIGN KEY (table3_id) REFERENCES table3(id)
);

CREATE TABLE table3 (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  table1_id INT,
  FOREIGN KEY (table1_id) REFERENCES table1(id)
);








--#########################################################################################
CREATE TABLE TableA (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    TableB_id INT,
    FOREIGN KEY (TableB_id) REFERENCES TableB(id)
);

CREATE TABLE TableB (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    TableC_id INT,
    FOREIGN KEY (TableC_id) REFERENCES TableC(id)
);

CREATE TABLE TableC (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    TableA_id INT,
    FOREIGN KEY (TableA_id) REFERENCES TableA(id)
);