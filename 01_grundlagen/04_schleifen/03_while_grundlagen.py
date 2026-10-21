# ==============================================================================
# Modul 1.4: Schleifen (Loops) - while-Schleife Grundlagen
# Datei: C:\Lernen_Python\01_grundlagen\schleifen\03_while_grundlagen.py
# ==============================================================================

# [THEORIE & GRUNDLAGEN: WAS IST EINE WHILE-SCHLEIFE?]
# Eine 'for'-Schleife benutzt man, wenn man genau weiss, wie oft man etwas wiederholen
# will (z. B. "fuer jedes Element in einer 4-teiligen Liste").
#
# Eine 'while'-Schleife benutzt man, wenn man etwas wiederholen will,
# SOLANGE eine bestimmte Bedingung wahr (True) ist!
#
# ------------------------------------------------------------------------------
# DIE 3 PFEILER JEDER WHILE-SCHLEIFE:
# 1. Startwert VOR der Schleife definieren:
#    counter = 1
# 2. Die Bedingung beim while-Befehl:
#    while counter <= 3:
# 3. Den Zustand IN der Schleife veraendern (ganz wichtig!):
#    counter += 1
#
# ------------------------------------------------------------------------------
# ACHTUNG: DIE ENDLOSSCHLEIFE (Infinite Loop)!
# Vergisst du Schritt 3 (also den Zaehler zu erhoehen), bleibt die Bedingung FUER IMMER
# True und dein Programm stoppt nie wieder von alleine!
# Falls dir das jemals im Terminal passiert:
# Druecke Tastenkombination: STRG + C (um den Vorgang sofort abzubrechen).
# ==============================================================================


# ==============================================================================
# [DAS MUSTERBEISPIEL: Retry-Mechanismus mit Countdown]
# ==============================================================================
remaining_attempts = 3  # Startwert: 3 Versuche uebrig

print(f"[DEMO] Starte Verbindungsaufbau mit {remaining_attempts} Versuchen...")

# Solange noch Versuche groesser als 0 sind, wird wiederholt:
while remaining_attempts > 0:
    print(f"[DEMO] -> Verbinde... Noch {remaining_attempts} Versuche uebrig.")
    # Sehr wichtig: Zaehler um 1 reduzieren, damit die Schleife irgendwann stoppt!
    remaining_attempts -= 1

print("[DEMO] Keine Versuche mehr uebrig. Verbindung beendet.")

print("=" * 60)


# ==============================================================================
# [DEINE UEBUNGSAUFGABEN]
# ==============================================================================

# ------------------------------------------------------------------------------
# AUFGABE 1: Einfacher Zaehler von 1 bis 4
# Szenario:
# Du moechtest einen einfachen Zaehler mit einer while-Schleife von 1 bis 4 zaehlen lassen.
#
# Deine Aufgabe:
# 1. Erstelle die Variable 'step = 1'.
# 2. Schreibe eine while-Schleife mit der Bedingung: 'while step <= 4:'.
# 3. Gib in der Schleife aus: "Schritt Nummer: <step>".
# 4. Erhoehe 'step' in der Schleife um 1 ('step += 1').
# 5. Gib nach der Schleife aus: "Alle 4 Schritte ausgefuehrt."
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 1 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 2: Akku-Ladung simulieren
# Szenario:
# Ein Agent hat aktuell 'battery_level = 20'. Er soll solange aufladen, bis
# er mindestens 50 Prozent erreicht hat. In jedem Ladezyklus laedt er um 10 Prozent auf.
#
# Deine Aufgabe:
# 1. Erstelle 'battery_level = 20'.
# 2. Schreibe eine while-Schleife mit der Bedingung: 'while battery_level < 50:'.
# 3. Gib in der Schleife aus: "Lade auf... Aktueller Stand: <battery_level>%"
# 4. Erhoehe 'battery_level' um 10 ('battery_level += 10').
# 5. Gib nach der Schleife aus:
#    "Ladevorgang beendet. Stand erreicht: <battery_level>%"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 2 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 3: Countdown (Herunterzaehlen mit while)
# Szenario:
# Ein Server-Neustart steht bevor. Du simulierst einen Sicherheits-Countdown
# von 5 herunter bis 1.
#
# Deine Aufgabe:
# - Erstelle eine Variable fuer den Countdown mit dem Startwert 5.
# - Schreibe eine while-Schleife, die solange laeuft, wie der Countdown groesser als 0 ist.
# - Gib in jedem Durchlauf aus:
#   "Server-Neustart in <sekunden> Sekunden..."
# - Reduziere die Countdown-Variable in jedem Durchlauf um 1.
# - Gib nach der Schleife einmal aus:
#   "Server wird jetzt neu gestartet!"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 3 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 4: Fortschritt / Schwellenwert (Praxis-Transfer)
# Szenario:
# Ein Download-Manager laedt eine Datei in Paketen herunter. Der Fortschritt
# beginnt bei 0 Prozent und in jedem Schritt werden 25 Prozent geladen, bis
# 100 Prozent erreicht sind.
#
# Deine Aufgabe:
# - Erstelle eine Variable fuer den Fortschritt mit dem Startwert 0.
# - Schreibe eine while-Schleife, die solange laeuft, wie der Fortschritt kleiner als 100 ist.
# - Gib in jedem Durchlauf aus:
#   "Download laeuft... Fortschritt: <fortschritt>%"
# - Erhoehe den Fortschritt in jedem Durchlauf um 25.
# - Gib nach der Schleife einmal aus:
#   "Download vollstaendig abgeschlossen (100%)!"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 4 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 5: Kaffeemaschine: Wassertank auffuellen (Hochzaehlen mit Schrittweite)
# Szenario:
# Der Wassertank einer Kaffeemaschine hat aktuell 300 ml Wasser ('wasser_ml = 300').
# Die Maschine benoetigt mindestens 900 ml fuer den Tag.
# In jedem Nachfuellschritt werden 150 ml hinzugefuegt.
#
# Deine Aufgabe:
# - Erstelle die Variable 'wasser_ml = 300'.
# - Schreibe eine while-Schleife, die laeuft, solange 'wasser_ml < 900' ist.
# - Gib in jedem Durchlauf aus:
#   "Fuellstand: {wasser_ml} ml... fuelle 150 ml nach."
# - Erhoehe 'wasser_ml' in jedem Schritt um 150.
# - Gib nach der Schleife einmal aus:
#   "Wassertank bereit ({wasser_ml} ml)! Maschine einsatzbereit."
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 5 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 6: Support-Tickets abarbeiten (Warteschlange abarbeiten)
# Szenario:
# Im IT-Support sind am Morgen 6 Tickets in der Warteschlange.
# Du moechtest simulieren, wie diese Tickets nacheinander abgearbeitet werden,
# bis die Warteschlange vollstaendig leer ist.
#
# Deine Aufgabe:
# - Erstelle eine passende Variable fuer die Anzahl der Tickets mit dem Startwert 6.
# - Schreibe eine while-Schleife, die solange laeuft, wie noch Tickets vorhanden sind.
# - Gib in jedem Durchlauf aus:
#   "Ticket wird bearbeitet... Noch <anzahl> Ticket(s) in der Warteschlange."
# - Reduziere die Ticket-Variable in jedem Durchlauf um 1.
# - Gib nach dem Ende der Schleife einmal aus:
#   "Alle Tickets erledigt! Warteschlange ist leer."
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 6 schreiben:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 7: Sparziel erreichen (Akkumulator mit Zielwert)
# Szenario:
# Du sparst fuer ein neues Technik-Projekt. Dein Startkapital betraegt 50 Euro.
# Jeden Monat kannst du 75 Euro zuruecklegen, bis du dein Ziel von mindestens
# 350 Euro erreicht hast.
#
# Deine Aufgabe:
# - Erstelle eine Variable fuer dein Erspartes mit dem Startwert 50.
# - Schreibe eine while-Schleife, die laeuft, solange das Ersparte unter 350 Euro liegt.
# - Gib in jedem Durchlauf aus:
#   "Sparen laeuft... Aktueller Betrag: <betrag> Euro"
# - Erhoehe das Ersparte in jedem Monat um 75 Euro.
# - Gib nach der Schleife einmal aus:
#   "Sparziel erreicht! Endstand: <betrag> Euro"
# ------------------------------------------------------------------------------

# Hier deinen Code fuer Aufgabe 7 schreiben:



print("=" * 60)


