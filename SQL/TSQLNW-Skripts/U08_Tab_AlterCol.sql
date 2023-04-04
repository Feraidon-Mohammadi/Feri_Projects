exec sp_help suppliers;

select * from Suppliers;

alter table suppliers
add email varchar(50) null ;			--column

select contactname, city, email, phone
from suppliers;


								--funktioniert nur,
								--wenn die Spalte noch nicht existiert
alter table suppliers
add email varchar(50) not null default '@' check(email like '%@%');

								--so gehts
								--wenn die Spalte schon existiert
alter table suppliers
add default '@' for email, check(email like '%@%');

alter table suppliers
alter column email varchar(100);


								--geht erst, 
								--wenn alle Constraints weg sind
alter table suppliers
drop column email;



exec sp_helpconstraint suppliers;

alter table suppliers
drop constraint	DF__suppliers__email__7B5B524B, constraint CK__suppliers__email__7C4F7684;