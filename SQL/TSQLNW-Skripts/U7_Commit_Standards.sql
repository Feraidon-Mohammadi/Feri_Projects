
--------------Microsoft Transact-SQL

insert	...	;								--Autocommit

insert	...	;

insert	...	;


begin tran								--Explizite Transaktion Anfang

update	...	;

update	...	;

commit tran								--Explizite Transaktion Ende


update	...	;								--Autocommit








set lock_timeout 30000;






---------------ANSI-SQL

insert	...	;
commit;

insert	...	;
commit;

insert	...	;
commit;


update	...	;

update	...	;

commit;


update	...	;
commit;