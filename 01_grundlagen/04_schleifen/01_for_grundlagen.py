# ==============================================================================
# Modul 1.4: Schleifen (Loops) - for-Schleife Grundlagen
# Datei: C:\Lernen_Python\01_grundlagen\schleifen\01_for_grundlagen.py
# ==============================================================================

# [THEORIE & GRUNDLAGEN: WAS IST EINE FOR-SCHLEIFE?]
# Stell dir vor, du hast eine Liste mit 100 Servern oder 1000 E-Mail-Adressen.
# Ohne Schleife muesstest du 100-mal print() schreiben:
#   print(servers[0])
#   print(servers[1])
#   print(servers[2]) ... das waere extrem muehsam und unmoeglich bei grossen Datenmengen!
#
# Eine 'for'-Schleife nimmt dir diese Arbeit ab:
# Sie nimmt sich ein Element nach dem anderen aus einer Liste und fuehrt den eingerueckten
# Codeblock fuer JEDES einzelne Element genau einmal aus.
#
# ------------------------------------------------------------------------------
# DIE SYNTAX DER FOR-SCHLEIFE:
#
#   for element in liste:
#       # Was hier eingrueckt ist, wird fuer jedes Element wiederholt!
#
# DIE REGELN:
# 1. Das Schluesselwort 'for': Leitet die Schleife ein.
# 2. Die Schleifenvariable (z. B. 'server', 'item', 'tool'):
#    Diesen Namen denkst DU dir frei aus! In jedem Durchlauf packt Python automatisch
#    das naechste Element aus der Liste in diese Variable.
#    Tipp: Liste im Plural benennen ('servers'), Variable im Singular ('server').
# 3. Das Schluesselwort 'in': Verbindet die Variable mit der Liste.
# 4. Der Doppelpunkt (:): MUSS am Ende der for-Zeile stehen!
# 5. Die Einrueckung (4 Leerzeichen): Alles was eingerueckt ist, gehoert ZUR Schleife.
#    Sobald du wieder ganz links schreibst, bist du AUSSERHALB der Schleife!
# ==============================================================================


# ==============================================================================
# [DAS MUSTERBEISPIEL]
# ==============================================================================
servers = ["web-01", "database-01", "backup-01", "auth-01"]

print(f"[DEMO] Starte Ueberpruefung von {len(servers)} Servern...")

# Die for-Schleife beginnt:
for server in servers:
    # Dieser eingerueckte Code laeuft 4-mal (einmal fuer jeden Server):
    print(f"[DEMO] -> Pruefe Verbindung zu: {server} ... OK")

# Dieser Code ist NICHT mehr eingerueckt - er laeuft erst, wenn die Schleife komplett FERTIG ist:
print("[DEMO] Ueberpruefung aller Systeme abgeschlossen!")

print("=" * 60)


# ==============================================================================
# [DEINE UEBUNGSAUFGABEN]
# Hier gelten weiterhin unsere Regeln:
# - Aufgabenstellung auf Deutsch
# - Variablennamen auf Englisch (mit Erklaerung im Kommentar)
# ==============================================================================

# ------------------------------------------------------------------------------
# AUFGABE 1: Liste von Werkzeugen durchlaufen
# Szenario:
# Du hast eine Liste deiner wichtigsten IT-Tools: "python", "terminal", "git".
#
# Deine Aufgabe:
# 1. Erstelle eine Liste 'tools' mit den 3 Strings: "python", "terminal", "git".
# 2. Schreibe eine for-Schleife ('for tool in tools:').
# 3. Gib in jedem Schleifendurchlauf mit einem f-String Folgendes aus:
#    "Installiertes Tool: <tool>"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 1 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 2: Temperatur-Sensoren auslesen & Abschlussmeldung
# Szenario:
# Drei Sensoren haben folgende Temperaturen gemessen: 19.5, 22.0, 24.5.
#
# Deine Aufgabe:
# 1. Erstelle eine Liste 'temperatures' mit den 3 Float-Zahlen: [19.5, 22.0, 24.5]
# 2. Schreibe eine for-Schleife, die jeden Wert als 'temp' durchlaeuft.
# 3. Gib in der Schleife fuer jeden Wert aus:
#    "Sensor meldet: <temp> Grad Celsius"
# 4. Schreibe AUSSERHALB der Schleife (also nicht mehr eingerueckt) einen print-Befehl:
#    "Alle Sensoren wurden erfolgreich abgefragt."
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 2 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 3: Benutzer-Accounts verarbeiten
# Szenario:
# Drei neue Teammitglieder sollen im System angelegt werden: "alice", "bob", "charlie".
#
# Deine Aufgabe:
# 1. Erstelle eine Liste 'users' mit den 3 Namen als Strings: ["alice", "bob", "charlie"]
# 2. Schreibe eine for-Schleife, die jeden Namen als 'user' durchlaeuft.
# 3. Gib in der Schleife fuer jeden Benutzer mit einem f-String aus:
#    "Benutzerkonto angelegt fuer: <user>"
# 4. Schreibe AUSSERHALB der Schleife (nicht mehr eingerueckt) einen print-Befehl:
#    "Alle Benutzerkonten wurden eingerichtet."
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 3 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 4: Backup-Dateien ueberpruefen (Start- & Abschlussmeldung)
# Szenario:
# Eine Reihe von Backup-Dateien soll ueberprueft werden:
# "config.json", "database.sql", "media.zip", "logs.txt".
#
# Deine Aufgabe:
# 1. Erstelle eine Liste 'files' mit den 4 Dateinamen als Strings.
# 2. Schreibe VOR der Schleife einen print-Befehl:
#    "Starte Pruefung von Backup-Dateien..."
# 3. Schreibe eine for-Schleife, die jeden Eintrag als 'filename' durchlaeuft.
# 4. Gib in der Schleife fuer jede Datei aus:
#    "[CHECK] Datei geprueft: <filename>"
# 5. Schreibe NACH der Schleife (wieder ganz links eingerueckt):
#    "Pruefung aller 4 Dateien erfolgreich beendet."
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 4 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 5: Netzwerk-Ports scannen
# Szenario:
# Eine Reihe von Netzwerk-Ports soll geprueft werden: 80, 443, 8080, 22.
#
# Deine Aufgabe:
# 1. Erstelle eine Liste 'ports' mit den 4 Ports als Integer-Zahlen.
# 2. Schreibe eine for-Schleife, die jeden Port als 'port' durchlaeuft.
# 3. Gib in der Schleife fuer jeden Port aus:
#    "Scanne Netzwerk-Port: <port>"
# 4. Gib ausserhalb der Schleife aus:
#    "Port-Scan abgeschlossen."
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 5 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 6: Status von Systemdiensten ausgeben
# Szenario:
# Verschiedene Dienste auf einem Server sollen bestaetigt werden:
# "nginx", "postgresql", "redis", "docker".
#
# Deine Aufgabe:
# 1. Erstelle eine Liste 'services' mit den 4 Strings.
# 2. Gib VOR der Schleife aus:
#    "Starte Statusabfrage der Dienste..."
# 3. Schreibe eine for-Schleife, die jeden Eintrag als 'service' durchlaeuft.
# 4. Gib in der Schleife fuer jeden Dienst aus:
#    "Dienst [<service>] laeuft stabil."
# 5. Gib NACH der Schleife aus:
#    "Statusabfrage beendet: Alle Dienste sind online."
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 6 schreiben:



print("=" * 60)


