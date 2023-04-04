--Index:	belegen Speicherbereiche auf Festspeicher(wie Tabellen auch)
--			speichern darin sortiert die Werte einer Tabellenspalte
--			oder -spaltenmenge(Indexschlüssel)
--			dazu wird für jeden Indexschlüsselwert noch ein Verweis
--			auf den Tabellendatensatz gespeichert;
--			Indexschlüsselwert und Verweis bilden einen Indexdatensatz;


--Zweck:	Performanceverbesserung bei		Filter-			(WHERE), 
--											Verknüpfungs-	(JOIN) und 
--											Gruppierungs-	(GROUP BY)
--											operationen

--Kandidaten für Indexspalten sollten eine

--			hohe Selektivität
--			niedrige Dichte				(relativ wenig Wiederholungswerte) haben

--Aktualisierung der Tabellendaten(INSERT, UPDATE, DELETE)

--			Datenbankindizes werden mit der Tabelle(jeder Index ist genau
--			einer Tabelle zugeordnet) absolut synchron gehalten

--			Jede Transaktion ist erst abgeschlossen(COMMITet), wenn alle 
--			Indizes der Tabelle aktualisiert sind

--Den sortierten Indexschlüsselwerten ist ein Binärbaum übergeordnet

--Je größer die Menge der gespeicherten Tabellendaten, desto effektiver ein Index

--Syntax:			CREATE INDEX <indexname>
--					ON <tabellenname>(<spaltenname>);

--					CREATE INDEX <indexname>
--					ON <tabellenname>(<spaltenname1>, <spaltenname2>,...);

--Heap					8K-Seiten, die einer Tabelle zugeordnet sind und nur durch
--						eine Index Allocation Map(IAM) logisch verbunden sind
--						es existiert keine Sortiervorschrift für die Speicherung 
--						der Datensätze im Heap

--NonClustered Index	Index bildet eine separate Speicherstruktur
--(Standard)			speichert die Werte der Indexschlüssel sortiert und 
--						zu jedem Schlüssel einen Verweis auf den dazugehörigen
--						Datensatz
--						kann jederzeit gelöscht werden, ohne dass die Tabelle
--						dadurch beeinflusst wird
--						999 pro Tabelle möglich

--Clustered Index		Tabelle ist im Index integriert
--						auf Blattebene sind die kompletten Datensätze der Tabelle
--						sortiert nach dem Indexschlüssel gespeichert
--						kann ebenfalls gelöscht werden, dabei wird nur der 
--						Indexbaum und die Zeiger entfernt, 
--						die Blattseiten bleiben erhalten
--						max. 1 pro Tabelle
--						zu einer Zeit kann eine Tabelle entweder als Heap
--						oder als clustered Index existieren
