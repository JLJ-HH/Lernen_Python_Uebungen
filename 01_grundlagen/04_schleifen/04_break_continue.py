# ==============================================================================
# Modul 1.4: Schleifen (Loops) - break & continue
# Datei: C:\Lernen_Python\01_grundlagen\schleifen\04_break_continue.py
# ==============================================================================

# [THEORIE & GRUNDLAGEN: SCHLEIFEN STEUERN]
# Manchmal moechtest du eine Schleife nicht stur bis zum allerletzten Element durchlaufen
# lassen, sondern vorzeitig eingreifen.
# Dafuer gibt es in Python zwei maechtige Steuerbefehle:
#
# ------------------------------------------------------------------------------
# 1. 'break' (Die Notbremse):
# - Bricht die Schleife SOFORT und komplett ab!
# - Keine weiteren Durchlaeufe mehr. Python springt direkt zur ersten Zeile NACH der Schleife.
# - Typischer Einsatz: "Sobald ich das gesuchte Element gefunden habe, hoere sofort auf zu suchen!"
#
# ------------------------------------------------------------------------------
# 2. 'continue' (Der Ueberspringer):
# - Bricht NUR den AKTUELLEN Durchlauf ab.
# - Ignoriert alle Zeilen darunter und springt sofort zum NAECHSTEN Element der Liste!
# - Typischer Einsatz: "Ueberspringe ungueltige Werte oder Server, die im Wartungsmodus sind."
# ==============================================================================


# ==============================================================================
# [MUSTERBEISPIEL 1: break (Vorzeitiger Abbruch bei Fund)]
# ==============================================================================
logs = ["INFO: Start", "INFO: Lade Daten", "CRITICAL: Festplatte voll!", "INFO: Bereit"]

print("[DEMO 1] Durchsuche Log-Eintraege nach Notfaellen...")

for log in logs:
    if "CRITICAL" in log:
        print(f"[DEMO 1] -> Notfall gefunden: '{log}' -> Breche Analyse sofort ab!")
        break  # Sofortiger Ausstieg aus der Schleife!
    print(f"[DEMO 1] Normaler Log: {log}")

print("[DEMO 1] Schleife beendet.")

print("-" * 60)


# ==============================================================================
# [MUSTERBEISPIEL 2: continue (Elemente gezielt ueberspringen)]
# ==============================================================================
server_status_list = ["active", "maintenance", "active", "offline", "active"]

print("[DEMO 2] Sende Benachrichtigungen nur an aktive Systeme...")

for status in server_status_list:
    if status == "maintenance":
        print("[DEMO 2] -> Status 'maintenance' uebersprungen (Wartung laeuft).")
        continue  # Springt direkt zum naechsten Durchlauf, der Code darunter laeuft NICHT!
    
    print(f"[DEMO 2] Sende Ping an System mit Status: {status}")

print("=" * 60)


# ==============================================================================
# [DEINE UEBUNGSAUFGABEN]
# ==============================================================================

# ------------------------------------------------------------------------------
# AUFGABE 1: break (Sicherheitsstopp bei Fehlerwert)
# Szenario:
# Du pruefst eine Liste von Sensor-Werten: [12, 18, -99, 25, 30].
# Der Wert -99 ist ein Fehlercode eines defekten Sensors.
#
# Deine Aufgabe:
# 1. Erstelle die Liste 'sensor_readings = [12, 18, -99, 25, 30]'.
# 2. Schreibe eine for-Schleife ('for reading in sensor_readings:').
# 3. Pruefe mit if: WENN 'reading == -99':
#    - Gib aus: "Defekter Sensor (-99) entdeckt! Notstopp aktiv."
#    - Fuehre 'break' aus.
# 4. Gib unter dem if (aber in der Schleife) aus: "Sensor-Wert OK: <reading>".
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 1 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 2: continue (Gesperrte Benutzer ignorieren)
# Szenario:
# Du hast eine Benutzerliste: ["alice", "banned_user", "charlie"].
# Der Name "banned_user" soll ignoriert werden.
#
# Deine Aufgabe:
# 1. Erstelle die Liste 'users = ["alice", "banned_user", "charlie"]'.
# 2. Schreibe eine for-Schleife ('for user in users:').
# 3. Pruefe mit if: WENN 'user == "banned_user"':
#    - Gib aus: "Gesperrter Benutzer wird uebersprungen."
#    - Fuehre 'continue' aus.
# 4. Gib fuer alle anderen aus:
#    "Willkommen im System, <user>!"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 2 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 3: break mit 'in' (Teiltext finden und stoppen)
# Szenario:
# Du pruefst Chat-Nachrichten auf Spam.
#
# Deine Aufgabe:
# 1. Erstelle die Liste:
#    chat_nachrichten = ["Hallo wie gehts?", "Klick hier fuer GRATIS Gewinne!", "Bis spaeter!"]
# 2. Schreibe eine for-Schleife ('for nachricht in chat_nachrichten:').
# 3. Pruefe mit if und 'in': WENN '"GRATIS" in nachricht':
#    - Gib aus: "Spam erkannt! Chat sofort sperren."
#    - Fuehre 'break' aus.
# 4. Gib unter dem if (in der Schleife) aus:
#    f"Nachricht freigegeben: {nachricht}"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 3 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 4: continue mit 'in' (Teiltext finden und ueberspringen)
# Szenario:
# Du verarbeitest Dokumente, moechtest aber Entwuerfe ueberspringen.
#
# Deine Aufgabe:
# 1. Erstelle die Liste:
#    dateien = ["rechnung.pdf", "entwurf_bericht.docx", "praesentation.pptx", "entwurf_notiz.txt"]
# 2. Schreibe eine for-Schleife ('for datei in dateien:').
# 3. Pruefe mit if und 'in': WENN '"entwurf" in datei':
#    - Gib aus: f"Entwurf uebersprungen: {datei}"
#    - Fuehre 'continue' aus.
# 4. Gib unter dem if (in der Schleife) aus:
#    f"Verarbeite Datei: {datei}"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 4 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 5: break mit '==' (Exakter Notstopp)
# Szenario:
# Du ueberwachst ein System und pruefst eine Liste von HTTP-Statuscodes:
# 200, 200, 404, 500, 200.
# Der Statuscode 500 signalisiert einen schweren Serverabsturz.
# Sobald dieser exakte Fehlerwert auftaucht, soll der Pruefprozess sofort
# gestoppt werden, ohne weitere Codes zu pruefen.
#
# Deine Aufgabe:
# - Erstelle die Liste 'status_codes' mit den 5 Integer-Zahlen.
# - Schreibe eine for-Schleife, die jeden Code durchlaeuft.
# - Pruefe mit '==': Wenn ein Code exakt dem Wert 500 entspricht:
#   - Gib eine Notfall-Warnung aus, dass ein Serverfehler aufgetreten ist und abgebrochen wird.
#   - Beende die Schleife sofort mit 'break'.
# - Gib fuer alle regulaeren Codes in der Schleife aus, dass der Statuscode verarbeitet wurde.
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 5 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 6: continue mit '==' (Exaktes Element ueberspringen)
# Szenario:
# Ein Berechtigungssystem weist Benutzerrollen Zugriffsrechte zu.
# Folgende Rollen sollen der Reihe nach geprueft werden:
# "admin", "gast", "entwickler", "gast", "manager".
# Konten mit der exakten Rolle "gast" duerfen keine Zugriffsrechte erhalten
# und sollen im Prozess einfach uebersprungen werden.
#
# Deine Aufgabe:
# - Erstelle die Liste 'rollen' mit den 5 Strings.
# - Schreibe eine for-Schleife, die alle Rollen durchlaeuft.
# - Pruefe mit '==': Wenn die Rolle exakt "gast" ist:
#   - Gib aus, dass Gast-Konten uebersprungen werden.
#   - Ueberspringe diesen Durchlauf mit 'continue'.
# - Gib fuer alle anderen Rollen aus, dass Zugriffsrechte erfolgreich vergeben wurden.
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 6 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 7: break mit 'in' (Teiltext-Fund mit sofortigem Abbruch)
# Szenario:
# Ein Virenscanner prueft eingehende Downloads:
# "bericht.docx", "urlaubsfoto.jpg", "setup_trojaner.exe", "tabelle.xlsx".
# Befindet sich das Teilwort "trojaner" in einem Dateinamen, liegt eine akute
# Bedrohung vor und der Scan muss auf der Stelle abgebrochen werden!
#
# Deine Aufgabe:
# - Erstelle die Liste 'downloads' mit den 4 Dateinamen.
# - Schreibe eine for-Schleife, die jeden Dateinamen durchlaeuft.
# - Pruefe mit 'in': Wenn "trojaner" im Namen vorkommt:
#   - Gib eine Warnmeldung aus (Bedrohung entdeckt / Notstopp).
#   - Brich die gesamte Schleife sofort mit 'break' ab.
# - Gib fuer alle sicheren Dateien in der Schleife aus, dass die Datei geprueft und in Ordnung ist.
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 7 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 8: continue mit 'in' (Teiltext-Fund ueberspringen)
# Szenario:
# Ein Auswertungsskript verarbeitet Log-Meldungen:
# "System gestartet", "WARNUNG: Speicher voll", "Verbindung aufgebaut", "WARNUNG: Hohe CPU-Last", "Backup erfolgreich".
# Alle Meldungen, die das Wort "WARNUNG" als Teiltext enthalten, sollen
# fuer diese Auswertung ignoriert und uebersprungen werden.
#
# Deine Aufgabe:
# - Erstelle die Liste 'logs' mit den 5 Nachrichten.
# - Schreibe eine for-Schleife, die jede Log-Nachricht durchlaeuft.
# - Pruefe mit 'in': Wenn "WARNUNG" in der Meldung enthalten ist:
#   - Gib aus, dass diese Warnmeldung uebersprungen wird.
#   - Ueberspringe den Durchlauf mit 'continue'.
# - Gib fuer alle normalen Meldungen aus, dass der Log-Eintrag erfolgreich archiviert wurde.
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 8 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 9: Job-Warteschlange stoppen (break mit '==')
# Szenario:
# Ein Rechenzentrum fuehrt eine Liste geplanter Server-Aufgaben aus:
# ["datenbank_backup", "cache_leeren", "notabschaltung", "system_update"]
# Der Befehl "notabschaltung" signalisiert einen Notfall.
# Sobald dieser exakte Befehl auftaucht, darf kein weiterer Job mehr ausgefuehrt
# werden – die Warteschlange muss sofort stoppen!
#
# Deine Aufgabe:
# - Erstelle die Liste 'aufgaben' mit den 4 Befehlen.
# - Schreibe eine for-Schleife, die jede Aufgabe durchlaeuft.
# - Pruefe mit '==': Wenn eine Aufgabe exakt dem String "notabschaltung" entspricht:
#   - Gib eine Notfall-Warnung inklusive des Aufgabennamens aus.
#   - Beende die Schleife sofort mit 'break'.
# - Gib fuer alle regulaeren Aufgaben in der Schleife aus, dass der Befehl abgearbeitet wurde.
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 9 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 10: Web-Crawler URL-Filter (continue mit 'in')
# Szenario:
# Ein Suchmaschinen-Crawler durchsucht eine Liste von Internet-Adressen (URLs):
# ["https://shop.de/produkte", "https://shop.de/intern/admin", "https://shop.de/kontakt", "https://shop.de/intern/kasse", "https://shop.de/ueber-uns"]
# Alle Adressen, die das Teilwort "intern" enthalten, sind geschuetzte Bereiche
# und duerfen nicht erfasst werden – sie sollen uebersprungen werden!
#
# Deine Aufgabe:
# - Erstelle die Liste 'webseiten' mit den 5 URLs.
# - Schreibe eine for-Schleife, die jede URL durchlaeuft.
# - Pruefe mit 'in': Wenn "intern" in der URL vorkommt:
#   - Gib einen Hinweis aus, dass dieser geschuetzte Pfad uebersprungen wird.
#   - Ueberspringe die weitere Verarbeitung mit 'continue'.
# - Gib fuer alle oeffentlichen Webseiten aus, dass die URL erfolgreich indexiert wurde.
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 10 schreiben:



print("=" * 60)

