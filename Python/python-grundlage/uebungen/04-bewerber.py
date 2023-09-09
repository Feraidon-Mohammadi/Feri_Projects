def ist_kandidat(alter, erfahrung, geschlecht, gehalt):
    if erfahrung >= 35 or gehalt < 20_000:
        return True
    if erfahrung >= 20 and gehalt > 60_000:
        return True
    if (geschlecht == "w" or geschlecht == "d") and (25 <= alter <= 35) and gehalt <= 30_000:
        return True
    if geschlecht == "m" and alter >= 25:
        if erfahrung >= 5:
            return True
        elif gehalt < 40_000:
            return True
        else:
            # erfahrung < 5 and gehalt >= 40_000
            return False

    # In allen sonstigen Fällen, lehnen wir den Bewerber ab.
    return False
    
print(ist_kandidat(20, 40, "m", 30_000))    # true
print(ist_kandidat(50, 2, "w", 10_000))     # true    
print(ist_kandidat(50, 20, "w", 65_000))    # true    
print(ist_kandidat(50, 2, "w", 65_000))     # false    
print(ist_kandidat(50, 2, "m", 35_000))     # true    
print(ist_kandidat(50, 2, "w", 35_000))     # false    
print(ist_kandidat(50, 2, "m", 35_000))     # true    
print(ist_kandidat(30, 2, "d", 25_000))     # true    
print(ist_kandidat(30, 2, "d", 35_000))     # false    

