# ==============================================================================
# Modul 1.3: Listen (Lists) - Grundlagen & Indizierung
# Datei: C:\Lernen_Python\01_grundlagen\listen\01_grundlagen_index.py
# ==============================================================================

# [THEORIE: WAS IST EINE LISTE?]
# Bisher konnte eine Variable immer nur EINEN Wert speichern (z. B. server = "web-01").
# Eine Liste (list) ist wie ein Notizblock oder Einkaufszettel: Sie kann BELIEBIG
# VIELE Werte in einer einzigen Variablen speichern.
#
# Kennzeichen einer Liste:
# 1. Eckige Klammern: [ ... ]
# 2. Kommas trennen die einzelnen Elemente: ["web", "db", "cache"]
#
# ------------------------------------------------------------------------------
# DIE GOLDENE REGEL DER INDIZIERUNG (Zero-based Indexing):
# Computer fangen IMMER bei 0 an zu zaehlen!
#
# Position im Alltag:     1. Element      2. Element      3. Element
# Index im Code:              [0]             [1]             [2]
#
# Negativer Index (vom Ende her zaehlen):
# Der Index [-1] greift immer auf das ALLERLETZTE Element zu!
# Der Index [-2] greift auf das VORLETZTE Element zu!
# ==============================================================================


# ==============================================================================
# [DAS MUSTERBEISPIEL]
# ==============================================================================
servers = ["web-01", "database-01", "auth-01", "cache-01"]

# 1. Von vorne zaehlen (positive Indizes):
first_server = servers[0]    # Das 1. Element (Index 0)
second_server = servers[1]   # Das 2. Element (Index 1)

# 2. Von hinten zaehlen (negative Indizes):
last_server = servers[-1]    # Das allerletzte Element (Index -1)
second_last = servers[-2]    # Das vorletzte Element (Index -2)

print(f"[DEMO] Gesamte Liste: {servers}")
print(f"[DEMO] Erstes Element [0]: {first_server}")
print(f"[DEMO] Zweites Element [1]: {second_server}")
print(f"[DEMO] Vorletztes Element [-2]: {second_last}")
print(f"[DEMO] Letztes Element [-1]: {last_server}")

print("=" * 60)


# ==============================================================================
# [DEINE UEBUNGSAUFGABEN]
# Ab hier gelten unsere neuen Regeln:
# - Aufgabenstellung auf Deutsch
# - Variablennamen auf Englisch (mit deutscher Erklaerung im Kommentar)
# ==============================================================================


# ------------------------------------------------------------------------------
# AUFGABE 1: Liste erstellen & Elemente ansprechen
# Szenario:
# Du verwaltest eine Liste von 3 Cloud-Diensten: "storage", "compute" und "network".
#
# Deine Aufgabe:
# 1. Erstelle die Variable 'services' mit diesen 3 Text-Werten (als Liste mit []).
# 2. Gib mit einem f-String das ERSTE Element (Index 0) aus.
# 3. Gib mit einem f-String das LETZTE Element (Index -1) aus.
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2: Zahlen-Liste anlegen & mittleres Element ansprechen
# 1. Erstelle eine Liste 'ports' mit drei Zahlen: [80, 443, 22]
# 2. Gib mit print() das mittlere Element an Index 1 aus.
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3: Namen-Liste & Erstes/Letztes Element
# 1. Erstelle eine Liste 'names' mit drei Namen: ["Alex", "Sam", "Chris"]
# 2. Gib mit print() das erste Element (Index 0) aus.
# 3. Gib mit print() das letzte Element (Index -1) aus.
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 4: Vorletztes Element abrufen (Index -2)
# 1. Erstelle eine Liste 'users' mit vier Konten: ["admin", "anna", "ben", "clara"]
# 2. Gib mit Index -2 das VORLETZTE Element aus.
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 5: Listen-Element in einer Variablen speichern
# 1. Erstelle eine Liste 'servers' mit: ["web-01", "web-02", "db-01"]
# 2. Speichere das erste Element in einer neuen Variable: first_server = servers[0]
# 3. Gib 'first_server' mit print() aus.
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 6: Alles auf einen Blick (Erstellen, Gesamtliste & Zugriff)
# 1. Erstelle eine Liste 'tools' mit drei Begriffen: ["terminal", "python", "editor"]
# 2. Gib zuerst die gesamte Liste mit print(tools) aus.
# 3. Gib danach das Element an Index 1 und das Element an Index -1 aus.
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("=" * 60)

