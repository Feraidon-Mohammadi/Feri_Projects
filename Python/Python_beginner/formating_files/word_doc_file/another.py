content = {
    "company_info": [
        "NTT DATA Deutschland GmbH",
        "Europaplatz 1",
        "99091 Erfurt"
    ],
    "date_and_position": "Erfurt, den 06.06.2023\nBewerbung um eine Praktikum Stelle als Penetrationstester/Cybersecurity.",
    "salutation": "Sehr geehrte Damen und Herren,",
    "application_info": [
        "Hiermit bewerbe ich mich bei Ihnen um eine Praktikum Stelle im Bereich IT-Sicherheit, welches ich am 25.09.2023 beginnen möchte.",
        "Durch Ihre Webseite habe ich mich über Ihre Firma informiert.",
        "Falls es bei Ihnen die Möglichkeit für Praktikumsstellen im Bereich Sicherheit gibt, möchte ich meine Chance mit dieser Bewerbung bei Ihrem Unternehmen prüfen.",
        "Mein langfristiges Ziel liegt jedoch im Bereich IT-Sicherheit, insbesondere im Bereich Penetrationstests und -prüfung.",
        "Während meiner Umschulung bei IAD habe ich bereits erste Erfahrungen in der Sicherheit und Anwendungsentwicklung gesammelt und grundlegende Kenntnisse in Sicherheit erworben: Security Plus CompTIA und Network Plus CompTIA, Ethical Hacking und verschiedenen Programmiersprachen wie Python, SQL, C#, Java. Weitere Informationen stehen in meinem Lebenslauf zur Verfügung.",
        "Diese Kenntnisse dienen mir als solide Grundlage für meine weitere Entwicklung.",
        "Besonders Linux und Python haben mein Interesse geweckt, und ich habe mir zum Ziel gesetzt, diese beiden Bereiche intensiv zu erlernen und zu beherrschen.",
        "Obwohl ich noch keine umfassenden Grundlagen in Linux besitze, arbeite ich kontinuierlich daran, meine Kenntnisse in diesem Bereich zu erweitern.",
        "Ich freue mich darauf, meine Fähigkeiten unter Beweis zu stellen und würde mich über eine Einladung zu einem persönlichen Gespräch sehr freuen, um weitere Einzelheiten zu besprechen."
    ],
    "closing": "Mit freundlichen Grüßen,\nFeraidon Mohammadi"
}

# Output the content
for section, text in content.items():
    if isinstance(text, str):
        print(text)
    else:
        for t in text:
            print(t)