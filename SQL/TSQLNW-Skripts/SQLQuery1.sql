/*####################################################################################################*/
CREATE TABLE kunde (
    kundennr		int			 NOT NULL		PRIMARY KEY,
    vorname         varchar(50)  NOT NULL	,
    kundenname      varchar(50)  NOT NULL	,
    plz				char(5) NOT  NULL,
    ort				varchar(100) NULL,
    bundesland      varchar(250) NULL
);
/*####################################################################################################*/

create table artikel (
	artnr		int				not null		    primary key,
	artbez		varchar(50)		not null,
	listenpris	money			null	
);
/*####################################################################################################*/

create table rechnung (
	rechnungnr		int			not null		primary key, 
	rechnungdatum	datetime	default			getdate(),
	kundennr		int			not null		unique
	foreign key (kundennr) references kunde
);
/*####################################################################################################*/

create table rechngpos (
	rechnungnr		int			not null			references rechnung,
	artnr			int			not null			references artikel,
	posmenge		tinyint			null,
	discount		tinyint		default 0           check(discount between 0 and 20),				
	Primary key(rechnungnr,artnr)
	);

	select * from rechngpos



















    
/*######################################################################################################
############################################ dozent ####################################################*/
create table kunde
(kundennr		char(7)|int	not null		primary key
,kname		varchar(30)	not null
,kvorname		varchar(50)	null
,plz			char(5)		null		check(plz like ‘[0-9][0-9][0-9][0-9][0-9]’)
,ort			varchar(50)	not null
,bundesland		varchar(30)	null
)
/*####################################################################################################*/
create table rechnung
(rechnungnr		char(7)|int	not null
,rechnungdatum	datetime	null	default getdate()
,kundennr		char(7)|int	not null	
,primary key(rechnungnr)
,foreign key(kundennr) references kunde
)

/*####################################################################################################*/
create table rechngpos
(rechnungnr		char(7)|int	not null
,artnr			char(4)|int	not null
,posmenge		smallint	not null		default (1)check(posmenge>0)
,discount		tinyint|decimal(3,2)	null	default (0)
check(discount between 0 and 20|0.2)
,primary key(artnr, rechnungnr)
,foreign key(artnr) references artikel
,foreign key(rechnungnr) references rechnung
)
/*####################################################################################################*/
create table artikel
(artnr			char(4)|int	not null		primary key
,artbez			varchar(50)	not null
,listenpreis		smallmoney	null		check(listenpreis>0)
)
/*####################################################################################################*/

select kname, kvorname from kunde where ort=’Saalfeld’

	select kundennr, plz from kunde
	where	bundesland like ‘Ba%’
|bundesland=’Bayern’ or bundesland=’Baden-Würtemberg’
	order by plz | 2

	select artikel.artnr, artbez 	
from artikel, rechngpos, rechnung
	where artikel.artnr=rechngpos.artnr
	and rechngpos.rechnungnr=rechnung.rechngnr
	and	rechnungdatum between ‘1.1.97’ and ‘31.1.97 23:59’
|	year(rechnungsdatum)=1997 and month(rechnungsdatum)=1
and discount=0

	select artnr, artbez from artikel
	where artnr in
		(select artnr from rechngpos	where discount=0
And rechngnr in
			(select rechngnr from rechnung
			where rechnungdatum between ‘1.1.97’ and ‘31.1.97 23:59’))

	select count(*) from rechnung
	where kundennr='4711' and rechnungdatum between ‘1.1.96’ and ’31.12.96 23:59’

	select ort, count(*)	from kunde k, rechung r, rechngpos p, artikel a
				where k.kundennr=r.kundennr
				and r.rechnungnr=p.rechnungnr
				and a.artnr=p.artnr
				and artbez=’Damenrad Diamant 2000’
	group by ort

	select ort, count(*)	from kunden where kundennr in
				(select kundennr from rechnung where rechnungnr in
				(select rechnungnr from rechngpos where artnr =|in
				(select artnr from artikel 
 where artbez=’Damenrad Diamant 2000’)))
	group by ort

	select * from artikel
	where artnr not in	(select artnr from rechngpos)

	select artikel.*		from artikel left join rechngpos
				on artikel.artnr=rechngpos.artnr
	where rechngpos.rechngnr is null







