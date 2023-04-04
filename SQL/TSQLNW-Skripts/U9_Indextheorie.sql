--Index:	belegen Speicherbereiche auf Festspeicher(wie Tabellen auch)
--			speichern darin sortiert die Werte einer Tabellenspalte
--			oder -spaltenmenge(Indexschl�ssel)
--			dazu wird f�r jeden Indexschl�sselwert noch ein Verweis
--			auf den Tabellendatensatz gespeichert;
--			Indexschl�sselwert und Verweis bilden einen Indexdatensatz;


--Zweck:	Performanceverbesserung bei		Filter-			(WHERE), 
--											Verkn�pfungs-	(JOIN) und 
--											Gruppierungs-	(GROUP BY)
--											operationen

--Kandidaten f�r Indexspalten sollten eine

--			hohe Selektivit�t
--			niedrige Dichte				(relativ wenig Wiederholungswerte) haben

--Aktualisierung der Tabellendaten(INSERT, UPDATE, DELETE)

--			Datenbankindizes werden mit der Tabelle(jeder Index ist genau
--			einer Tabelle zugeordnet) absolut synchron gehalten

--			Jede Transaktion ist erst abgeschlossen(COMMITet), wenn alle 
--			Indizes der Tabelle aktualisiert sind

--Den sortierten Indexschl�sselwerten ist ein Bin�rbaum �bergeordnet

--Je gr��er die Menge der gespeicherten Tabellendaten, desto effektiver ein Index

--Syntax:			CREATE INDEX <indexname>
--					ON <tabellenname>(<spaltenname>);

--					CREATE INDEX <indexname>
--					ON <tabellenname>(<spaltenname1>, <spaltenname2>,...);

--Heap					8K-Seiten, die einer Tabelle zugeordnet sind und nur durch
--						eine Index Allocation Map(IAM) logisch verbunden sind
--						es existiert keine Sortiervorschrift f�r die Speicherung 
--						der Datens�tze im Heap

--NonClustered Index	Index bildet eine separate Speicherstruktur
--(Standard)			speichert die Werte der Indexschl�ssel sortiert und 
--						zu jedem Schl�ssel einen Verweis auf den dazugeh�rigen
--						Datensatz
--						kann jederzeit gel�scht werden, ohne dass die Tabelle
--						dadurch beeinflusst wird
--						999 pro Tabelle m�glich

--Clustered Index		Tabelle ist im Index integriert
--						auf Blattebene sind die kompletten Datens�tze der Tabelle
--						sortiert nach dem Indexschl�ssel gespeichert
--						kann ebenfalls gel�scht werden, dabei wird nur der 
--						Indexbaum und die Zeiger entfernt, 
--						die Blattseiten bleiben erhalten
--						max. 1 pro Tabelle
--						zu einer Zeit kann eine Tabelle entweder als Heap
--						oder als clustered Index existieren
