# ==============================================================================
# Modul 1.3: Listen (Lists) - Teil 4: Sortieren & Reihenfolge (.sort & .reverse)
# Datei: C:\Lernen_Python\01_grundlagen\listen\04_sort_reverse.py
# ==============================================================================

# [THEORIE: REIHENFOLGE UND SORTIERUNG VON LISTEN]
# Oft liegen Daten unsortiert vor. Python bietet zwei sehr einfache Methoden:
#
# KONZEPT 1: Aufsteigend sortieren mit '.sort()'
#   - Text/Strings: Werden alphabetisch von A bis Z sortiert.
#   - Zahlen:       Werden aufsteigend von klein nach gross sortiert.
#   Wichtig: .sort() veraendert die Liste direkt an Ort und Stelle ("in-place")!
#   Beispiel: meine_liste.sort()
#
# KONZEPT 2: Reihenfolge umkehren mit '.reverse()'
#   Dreht die aktuelle Reihenfolge der Elemente einfach komplett um (letztes wird erstes usw.).
#   Beispiel: meine_liste.reverse()
# ==============================================================================


# ==============================================================================
# [MUSTERBEISPIELE]
# ==============================================================================

# --- DEMO 1: AUFSTEIGEND SORTIEREN MIT .sort() ---
node_names = ["web-03", "api-01", "db-02", "auth-01"]
print(f"[DEMO 1 vor sort]   {node_names}")

node_names.sort()
print(f"[DEMO 1 nach sort]  {node_names}")

ping_times = [45, 12, 89, 23]
ping_times.sort()
print(f"[DEMO 1 Zahlen sort] {ping_times}")

print("-" * 40)

# --- DEMO 2: REIHENFOLGE UMKEHREN MIT .reverse() ---
priority_queue = ["niedrig", "mittel", "hoch", "kritisch"]
print(f"[DEMO 2 vor reverse]  {priority_queue}")

priority_queue.reverse()
print(f"[DEMO 2 nach reverse] {priority_queue}")

print("=" * 60)


# ==============================================================================
# [DEINE UEBUNGSAUFGABEN]
# ==============================================================================

# ------------------------------------------------------------------------------
# AUFGABE 1 (zu Konzept 1: .sort() mit Text):
# Szenario:
# Ein Server hat unstrukturierte Log-Dateien empfangen:
# log_files = ["syslog", "auth.log", "kern.log", "daemon.log"]
# Zur besseren Uebersicht sollen die Dateinamen alphabetisch sortiert werden.
#
# Deine Aufgabe:
# 1. Erstelle die Liste: log_files = ["syslog", "auth.log", "kern.log", "daemon.log"]
# 2. Sortiere die Liste mit log_files.sort().
# 3. Gib die sortierte Liste mit print() aus.
# ------------------------------------------------------------------------------

log_files = ["syslog", "auth.log", "kern.log", "daemon.log"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2 (zu Konzept 1: .sort() mit Zahlen):
# Szenario:
# CPU-Messungen in Prozent liegen unsortiert vor:
# cpu_loads = [78, 12, 95, 34, 55]
# Du moechtest die Auslastungen von der kleinsten zur groessten sortieren.
#
# Deine Aufgabe:
# 1. Erstelle die Liste: cpu_loads = [78, 12, 95, 34, 55]
# 2. Sortiere die Liste aufsteigend mit cpu_loads.sort().
# 3. Gib die sortierten Werte mit print() aus.
# 4. Gib mit einem f-String das kleinste Element (Index 0) und das groesste (Index -1) aus!
# ------------------------------------------------------------------------------

cpu_loads = [78, 12, 95, 34, 55]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3 (zu Konzept 2: .reverse()):
# Szenario:
# Schritte eines Deployment-Prozesses in normaler Reihenfolge:
# steps = ["build", "test", "package", "deploy"]
# Fuer ein Rollback (Rueckabwicklung) muss die Reihenfolge umgedreht werden.
#
# Deine Aufgabe:
# 1. Erstelle die Liste: steps = ["build", "test", "package", "deploy"]
# 2. Kehre die Reihenfolge mit steps.reverse() um.
# 3. Gib die umgekehrte Liste mit print() aus.
# ------------------------------------------------------------------------------

steps = ["build", "test", "package", "deploy"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 4 (zu Konzept 1 & 2 kombiniert):
# Szenario:
# Punktzahlen (Scores) von Benutzern:
# scores = [150, 420, 90, 310, 280]
# Eine Bestenliste (Leaderboard) soll vom HOECHSTEN zum NIEDRIGSTEN Score sortiert sein.
#
# Tipp: Sortiere erst mit .sort() (klein nach gross) und drehe danach mit .reverse() um!
#
# Deine Aufgabe:
# 1. Erstelle die Liste: scores = [150, 420, 90, 310, 280]
# 2. Sortiere die Liste erst mit scores.sort().
# 3. Drehe sie danach mit scores.reverse() um.
# 4. Gib das fertige Leaderboard (absteigend) mit print() aus.
# ------------------------------------------------------------------------------

scores = [150, 420, 90, 310, 280]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 5 (Praxis-Check: Text sortieren):
# Szenario:
# Du hast fuenf Staedtenamen: Hamburg, Berlin, Muenchen, Koeln, Frankfurt.
#
# Deine Aufgabe:
# 1. Lege eine Liste namens 'staedte' mit diesen fuenf Namen an.
# 2. Sortiere die Staedte alphabetisch (A bis Z).
# 3. Gib das Ergebnis auf der Konsole aus.
# ------------------------------------------------------------------------------

staedte = ["Hamburg", "Berlin", "Muenchen", "Koeln", "Frankfurt"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 6 (Praxis-Check: Zahlen sortieren):
# Szenario:
# Folgende Testergebnisse einer Pruefung liegen vor: 88, 42, 95, 73, 61, 100, 54.
#
# Deine Aufgabe:
# 1. Speichere die Zahlen in einer Liste namens 'punkte'.
# 2. Sortiere die Punktzahlen aufsteigend (von klein nach gross).
# 3. Gib die sortierte Liste auf der Konsole aus.
# ------------------------------------------------------------------------------

punkte = [88, 42, 95, 73, 61, 100, 54]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 7 (Praxis-Check: Reihenfolge umkehren):
# Szenario:
# Die Projektschritte "Start", "Check 1", "Check 2", "Ziel" sollen
# fuer einen Rueckblick in umgekehrter Reihenfolge dargestellt werden.
#
# Deine Aufgabe:
# 1. Speichere die Schritte in einer Liste namens 'timeline'.
# 2. Drehe die Reihenfolge der Elemente komplett um.
# 3. Gib die Liste aus.
# ------------------------------------------------------------------------------

timeline = ["Start", "Check 1", "Check 2", "Ziel"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 8 (Praxis-Check: Absteigend sortieren):
# Szenario:
# Verschiedene Preisangebote in Euro: 19.99, 4.50, 49.90, 12.00, 89.00.
# Fuer eine Rangliste soll der hoechste Preis ganz vorne stehen und der niedrigste ganz hinten.
#
# Deine Aufgabe:
# 1. Lege eine Liste 'preise' mit den Betraegen an.
# 2. Sortiere die Liste absteigend (vom teuersten zum billigsten).
# 3. Gib das Ergebnis aus.
# ------------------------------------------------------------------------------

preise = [19.99, 4.50, 49.90, 12.00, 89.00]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 9 (zu Konzept 1: .sort()):
# Szenario:
# CPU-Auslastungsmessungen von 5 Kernen (in Prozent):
# cpu_loads = [78, 12, 95, 34, 60]
#
# Deine Aufgabe:
# 1. Lege die Liste 'cpu_loads' mit den 5 Zahlen an.
# 2. Sortiere die Liste mit .sort() aufsteigend (vom schwaechsten zum staerksten belasteten Kern).
# 3. Gib mit einem f-String den geringsten Wert (Index 0) und den hoechsten Wert (Index -1) aus:
#    "Minimale Last: {cpu_loads[0]}% | Maximale Last: {cpu_loads[-1]}%"
# 4. Gib die sortierte Gesamtliste aus.
# ------------------------------------------------------------------------------

cpu_loads = [78, 12, 95, 34, 60]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 10 (zu Konzept 2: .reverse()):
# Szenario:
# Ein Sysadmin ruft die Chronologie eingegebener Befehle ab:
# command_history = ["ls -la", "cd /etc/nginx", "nano nginx.conf", "systemctl reload nginx"]
# Fuer eine Rueckschau soll die Reihenfolge umgedreht werden (neuester Befehl zuerst).
#
# Deine Aufgabe:
# 1. Lege die Liste 'command_history' mit den 4 Befehlen an.
# 2. Kehre die Reihenfolge mit .reverse() komplett um.
# 3. Gib die Liste mit print() aus.
# ------------------------------------------------------------------------------

command_history = ["ls -la", "cd /etc/nginx", "nano nginx.conf", "systemctl reload nginx"]

# Hier deinen Code schreiben:



print("=" * 60)

