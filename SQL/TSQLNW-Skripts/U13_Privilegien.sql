/***********************************************************************

		Arbeiten mit Rollen und Berechtigungen

	Die nachfolgenden Beispiele sind teilweise mit fiktiven 
	Prozedurnamen geschrieben und daher in dem Fall nicht aausführbar
**************************************************************************/
use northwind;


create role dbadmin;

create role dbuser;

create role auftragsverwaltung;

create role personalverwaltung;

create role kundenbetreuung;

create role produkteinkauf;



create user student --without login;
for login student;



alter role dbadmin add member student;

alter role db_owner add member dbadmin;

							




/***************	GRANT	****************/


										--Anweisungsprivileg
										--umfassende Kontrolle in dieser Datenbank
grant control to dbadmin;



grant select, insert, update, delete	--alle Berechtigungen
on employees 							--für die Tabelle 
to personalverwaltung					--an diese Datenbankrollen


grant select, insert, update(unitprice, supplierid, discontinued)
on products
to produkteinkauf;


grant select, insert, update
on orders
to auftragsverwaltung, dbuser;


grant select
on v_orders_summ
to public;


/************	Funktionen:	EXECUTE für Skalarfunktionen
							SELECT, INSERT, UPDATE, DELETE
							für Inline-Funktionen
**************************************************************************/	

-------------------------------------InLine-Funktion

grant select
on udf_bestelldaten
to auftragsverwaltung;
								

-------------------------------------Skalarfunktion

grant execute
on udf_listenpreis
to auftragsverwaltung;



-------------------------------------Prozedur
grant execute 
on usp_del_odetails
to auftragsverwaltung;

grant execute
on usp_upd_listenpreis
to produkteinkauf;




/***************	REVOKE	****************/

revoke insert, update 
on orders
to dbuser;


					--das INSERT-Privileg wurde 
					--nie für das Tabelle
					--orders vergeben
					--trotzdem keine Fehlermeldung
revoke select, insert
on orders
to public;

					--wird ausgeführt, obwohl das
					--DELETE-Privileg nie für 
					--orders vergeben wurde
revoke delete
on orders 
to public;

								--dbadmin behält das CONTROL-Privileg
								--durch Mitgliedschaft in der Rolle db_owner
revoke control to dbadmin;


revoke execute
on usp_del_odetails
to auftragsverwaltung;



/***************	DENY	****************/


				--das hat Effekt
				--allerdings durchschlagenden
				--sysadmin ist nicht betroffen
deny delete
on orders 
to public;


				--Rückgängig geht auch mit
				--REVOKE
revoke delete
on orders
to public;


deny delete
on orders
to guest, kundenbetreuung, produkteinkauf, personalverwaltung;

				--gängige Praxis
				
grant select
on orders
to public;

deny select
on orders
to guest;	

							




/***************	GRANT OPTION	****************/

--dbo:
grant select, insert, update
on products 
to produkteinkauf
with grant option;


--ein Mitglied aus produkteinkauf:
grant select, insert, update
on products 
to personalverwaltung
with grant option;


--ein Mitglied aus personalverwaltung:
grant select, insert, update
on products 
to dbuser;


--dbo:									--weitergereichte Berechtigungen
										--werden entzogen


revoke select, insert, update
on products
to produkteinkauf
cascade;


/*****************************		Schema und Privilegien
**********************************************************************/

create schema prozeduren;


							--Übertragen von Objekten
							--aus einem Schema in ein anderes
alter schema prozeduren
transfer dbo.usp_del_odetails;

alter schema prozeduren
transfer dbo.usp_shippers_del;

alter schema prozeduren
transfer dbo.usp_shippers_ins;

alter schema prozeduren
transfer dbo.usp_shippers_upd;

alter schema prozeduren
transfer dbo.usp_upd_listenpreis;


							--Vorteil:
							--Berechtigungen mit einem Schlag
							--auf viele Objekte
grant execute 
on schema::prozeduren
to auftragsverwaltung;


		