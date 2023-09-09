def zerlege(minuten_gesamt):
    minuten_pro_tag = 24 * 60
    anzahl_tage = minuten_gesamt // minuten_pro_tag
    verbleibende_minuten = minuten_gesamt % minuten_pro_tag
    anzahl_stunden = verbleibende_minuten // 60
    anzahl_minuten = verbleibende_minuten % 60

    print(
        f"{minuten_gesamt} Minuten sind {anzahl_tage} Tage "
        + f"{anzahl_stunden} Stunden und {anzahl_minuten} Minuten.")

zerlege(1580)
zerlege(1440)
zerlege(1000)
zerlege(3000)