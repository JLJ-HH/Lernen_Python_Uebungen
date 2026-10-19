# ==============================================================================
# Modul 1.2: Bedingungen & Verzweigungen (if, elif, else)
# Datei: C:\Lernen_Python\01_grundlagen\bedingungen\01_grundlagen_if_else.py
# ==============================================================================

# [THEORIE & GRUNDLAGEN]
# Bisher lief dein Code immer stur von oben nach unten durch.
# Mit Bedingungen (if / elif / else) kann dein Programm Entscheidungen treffen!
# Es prueft einen Wahrheitswert (Boolean: True oder False) und biegt entsprechend ab.

# ------------------------------------------------------------------------------
# DIE 2 GOLDENEN REGELN VON PYTHON:
# 1. Der Doppelpunkt (:): Nach 'if', 'elif' und 'else' MUSS immer ein Doppelpunkt stehen!
# 2. Die Einrueckung (4 Leerzeichen / Tab):
#    Alles, was eingerueckt unter dem 'if' steht, gehoert zu diesem Block und
#    wird NUR ausgefuehrt, wenn die Bedingung wahr (True) ist!
# ------------------------------------------------------------------------------


# ==============================================================================
# [DAS MUSTERBEISPIEL 1: Einfaches if / else]
# ==============================================================================
akku_stand = 15.0

print(f"[STATUS] Akku-Stand: {akku_stand}%")

if akku_stand >= 20.0:
    # Dieser Block laeuft NUR, wenn akku_stand >= 20.0 wahr ist:
    print("-> Status: Agent ist startklar!")
else:
    # Dieser Block laeuft in allen anderen Faellen (wenn es False ist):
    print("-> Status: Akku zu schwach! Bitte aufladen.")

print("-" * 60)


# ==============================================================================
# [DAS MUSTERBEISPIEL 2: Mehrere Faelle mit if / elif / else]
# 'elif' ist die Abkuerzung fuer 'else if' (also: "oder wenn stattdessen...")
# Python prueft von oben nach unten. Der erste Treffer gewinnt!
# ==============================================================================
latenz_ms = 350

print(f"[STATUS] Gemessene Latenz: {latenz_ms} ms")

if latenz_ms < 200:
    print("-> Bewertung: Hervorragend (Blitzschnell)")
elif latenz_ms < 500:
    print("-> Bewertung: Gut (Voellig im Rahmen)")
else:
    print("-> Bewertung: Kritisch (Antwortzeit zu langsam!)")

print("=" * 60)


# ==============================================================================
# [DEINE UEBUNGSAUFGABEN]
# Loese die folgenden 3 Aufgaben direkt hier im Skript:
# ==============================================================================

# ------------------------------------------------------------------------------
# AUFGABE 1: API-Guthaben pruefen (if / else)
# Szenario: Ein API-Aufruf kostet 0.05 Euro.
# 1. Du hast das Startguthaben 'guthaben = 0.12'.
# 2. Schreibe ein if/else:
#    - WENN 'guthaben' groesser oder gleich 0.05 ist:
#      Gib aus: "API-Aufruf genehmigt. Guthaben reicht aus."
#    - SONST (else):
#      Gib aus: "API-Aufruf abgelehnt. Bitte Guthaben aufladen."
# ------------------------------------------------------------------------------

guthaben = 0.12

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2: Server-Temperatur Alarmstufe (if / elif / else)
# Szenario: Ein Server meldet seine aktuelle Temperatur 'temp = 82.5'.
# 1. Schreibe ein if / elif / else mit folgenden 3 Stufen:
#    - WENN 'temp' groesser als 80.0 ist:
#      Gib aus: "ALARM: Server ist ueberhitzt!"
#    - ODER WENN (elif) 'temp' groesser oder gleich 60.0 ist:
#      Gib aus: "WARNUNG: Server laeuft warm."
#    - SONST (else):
#      Gib aus: "NORMAL: Temperatur im optimalen Bereich."
# ------------------------------------------------------------------------------

temp = 82.5

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3: Benutzer-Rolle und Zugriffsrechte (Text-Vergleich mit ==)
# Szenario: Ein Agent empfaengt die Rolle eines Benutzers als Text 'rolle = "admin"'.
# In Python vergleicht man Text mit doppeltem Gleichheitszeichen: rolle == "admin"
#
# 1. Schreibe ein if / elif / else:
#    - WENN 'rolle == "admin"':
#      Gib aus: "Vollzugriff: Administrator-Modus aktiv."
#    - ODER WENN 'rolle == "editor"':
#      Gib aus: "Eingeschraenkter Zugriff: Bearbeiten erlaubt."
#    - SONST (else):
#      Gib aus: "Zugriff verweigert: Unbekannte Rolle."
# ------------------------------------------------------------------------------

rolle = "admin"

# Hier deinen Code schreiben:



print("=" * 60)

