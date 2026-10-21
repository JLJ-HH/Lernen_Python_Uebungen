# ==============================================================================
# Modul 1.4: Schleifen (Loops) - range() & Zaehlen
# Datei: C:\Lernen_Python\01_grundlagen\schleifen\02_range_und_zaehlen.py
# ==============================================================================

# [THEORIE & GRUNDLAGEN]
# Oft moechtest du eine Aktion genau X-mal ausfuehren (z. B. "Wiederhole den Download-
# Versuch 5-mal"), hast dafuer aber gar keine fertige Liste angelegt.
# Dafuer gibt es in Python die eingebaute Funktion range()!
#
# ------------------------------------------------------------------------------
# 1. WIE FUNKTIONIERT range()?
# range() erzeugt eine Reihe von ganzen Zahlen nach festen Regeln:
#
#   range(5)          -> Erzeugt die Zahlen: 0, 1, 2, 3, 4
#                        ACHTUNG: Python faengt bei 0 an und STOPPT VOR dem Endwert!
#
#   range(1, 6)       -> Start bei 1, Stopp vor 6: 1, 2, 3, 4, 5
#
#   range(10, 50, 10) -> Start bei 10, Stopp vor 50, Schrittweite 10: 10, 20, 30, 40
#
# ------------------------------------------------------------------------------
# 2. DAS ZAEHLER-MUSTER (Akkumulator):
# Wenn du in einer Schleife etwas zusammenzaehlen oder aufsummieren willst, gilt:
# - VOR der Schleife legst du die Start-Variable an (z. B. total = 0).
# - IN der Schleife addierst du den neuen Wert hinzu (total = total + wert oder kurz total += wert).
# - NACH der Schleife gibst du das Endergebnis aus!
# ==============================================================================


# ==============================================================================
# [MUSTERBEISPIEL 1: range() fuer feste Wiederholungen]
# ==============================================================================
print("[DEMO 1] Sende 3 Ping-Versuche an Router...")

for attempt in range(1, 4):  # Zahlen: 1, 2, 3 (stoppt vor 4)
    print(f"[DEMO 1] Ping-Versuch Nr. {attempt} gesendet.")

print("[DEMO 1] Alle Ping-Versuche abgeschlossen.")

print("-" * 60)


# ==============================================================================
# [MUSTERBEISPIEL 2: Werte aufsummieren mit total += wert]
# ==============================================================================
file_sizes_mb = [12, 45, 18, 25]  # Dateigroessen in Megabyte

# Schritt 1: Startwert vor der Schleife auf 0 setzen
total_mb = 0

print(f"[DEMO 2] Berechne Gesamtspeicher fuer: {file_sizes_mb}")

# Schritt 2: Liste durchlaufen und aufaddieren
for size in file_sizes_mb:
    total_mb += size  # Das ist die elegante Kurzform fuer: total_mb = total_mb + size
    print(f"[DEMO 2] + {size} MB hinzugefuegt -> Zwischenstand: {total_mb} MB")

# Schritt 3: Gesamtergebnis nach der Schleife ausgeben
print(f"[DEMO 2] Gesamter Speicherbedarf: {total_mb} MB")

print("=" * 60)


# ==============================================================================
# [DEINE UEBUNGSAUFGABEN]
# ==============================================================================

# ------------------------------------------------------------------------------
# AUFGABE 1: Wiederholen mit range()
# Szenario:
# Du simulierst einen 5-stufigen Countdown fuer einen Raketenstart oder Server-Neustart.
#
# Deine Aufgabe:
# 1. Schreibe eine for-Schleife mit range(1, 6) und nenne die Variable 'step'.
# 2. Gib in jedem Durchlauf aus:
#    "System-Check Stufe <step> von 5 aktiv."
# 3. Gib nach der Schleife aus:
#    "Check abgeschlossen. Alle Systeme bereit!"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 1 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 2: Cloud-Kosten aufsummieren (Der Zaehler)
# Szenario:
# Auf deinem Cloud-Konto fallen 3 Posten an: 15, 30 und 45 Euro.
#
# Deine Aufgabe:
# 1. Erstelle eine Variable 'total_cost = 0' (dein Start-Zaehler).
# 2. Erstelle eine Liste 'costs = [15, 30, 45]'.
# 3. Durchlaufe die Liste mit einer for-Schleife ('for cost in costs:').
# 4. Addiere in jedem Schritt den Betrag auf 'total_cost' hinzu ('total_cost += cost').
# 5. Gib AUSSERHALB der Schleife das Endergebnis mit einem f-String aus:
#    "Gesamte monatliche Kosten: <total_cost> Euro"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 2 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 3: Wiederholung mit range() (Praxis-Transfer)
# Szenario:
# Du simulierst eine Datensicherung (Backup). Es sollen nacheinander die 
# Backup-Runden 1 bis 4 durchgefuehrt werden.
#
# Deine Aufgabe:
# - Schreibe eine for-Schleife mit range(), die die Runden von 1 bis inklusive 4 durchlaeuft.
# - Gib in jedem Durchlauf aus:
#   "Backup-Runde <runde> von 4 erfolgreich abgeschlossen."
# - Gib nach Abschluss der gesamten Schleife einmal aus:
#   "Alle Backups wurden erfolgreich erstellt!"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 3 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 4: Werte aufsummieren (Praxis-Transfer Zaehler)
# Szenario:
# In einer Arbeitswoche wurden von Montag bis Freitag folgende Anzahlen
# an IT-Support-Tickets bearbeitet: 12, 8, 15, 7 und 10.
#
# Deine Aufgabe:
# - Lege eine Liste mit diesen fuenf Ticket-Zahlen an.
# - Erstelle eine passende Zaehlervariable mit dem Startwert 0.
# - Durchlaufe die Liste mit einer Schleife und summiere alle Tickets auf.
# - Gib nach der Schleife das Gesamtergebnis mit einem f-String aus:
#   "Gesamtzahl der bearbeiteten Tickets diese Woche: <variable> Tickets"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 4 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 5: Wiederholung mit range() (Verbindungsversuche)
# Szenario:
# Du schreibst ein Skript, das die Verbindung zu einem Server prüft.
# Es sollen nacheinander die Verbindungsversuche 1 bis 5 simuliert werden.
#
# Deine Aufgabe:
# - Schreibe eine for-Schleife mit range(), die von 1 bis inklusive 5 zählt.
# - Gib in jedem Durchlauf aus:
#   "Verbindungsversuch <versuch> von 5 wird ausgefuehrt..."
# - Gib nach der Schleife einmal aus:
#   "Verbindung zum Server erfolgreich aufgebaut!"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 5 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 6: Werte aufsummieren (Download-Groessen addieren)
# Szenario:
# Du hast fuenf Dateien heruntergeladen mit folgenden Groessen in Megabyte (MB):
# 120, 45, 300, 85 und 250.
#
# Deine Aufgabe:
# - Lege eine Liste mit diesen fuenf Zahlen an.
# - Erstelle eine Zaehlervariable (z.B. 'gesamt_mb' oder 'total_size') mit Startwert 0.
# - Durchlaufe die Liste mit einer for-Schleife und summiere alle Werte auf.
# - Gib nach der Schleife das Gesamtergebnis mit einem f-String aus:
#   "Gesamter Speicherbedarf aller Downloads: <variable> MB"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 6 schreiben:



print("=" * 60)

