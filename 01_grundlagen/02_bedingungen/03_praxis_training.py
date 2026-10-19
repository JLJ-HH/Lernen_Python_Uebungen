# ==============================================================================
# Modul 1.2 - Praxisrunde 3: Bedingungen (if, elif, else)
# Datei: C:\Lernen_Python\01_grundlagen\bedingungen\03_praxis_training.py
# ==============================================================================


# ------------------------------------------------------------------------------
# AUFGABE 1: API Rate-Limit (Anfragenzaehler)
# Szenario: Ein Agent sendet Anfragen an eine API. Aktuell wurden in dieser
# Minute bereits 95 Anfragen gezaehlt ('anfragen = 95'). Das Maximum ist 100.
#
# Schreibe ein if / else:
# - WENN 'anfragen > 100' ist:
#   Gib aus, dass das Limit ueberschritten wurde und pausiert werden muss.
# - SONST (else):
#   Gib mit einem f-String aus, wie viele Anfragen bisher gesendet wurden.
# ------------------------------------------------------------------------------

anfragen = 95

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2: Server-Monitoring (RAM-Warnstufen)
#
# Kontext:
# Ein Monitoring-Skript prueft regelmaessig die Speicherauslastung (in Prozent).
# Je nach Lastzustand soll das System eine passende Statusmeldung ausgeben:
# - Ab 90.0%: Eine kritische Warnung (z. B. "Speicher kritisch voll!")
# - Ab 75.0%: Eine Vorwarnung (z. B. "Warnung: Hohe Auslastung")
# - Unter 75.0%: Eine Entwarnung (z. B. "Speicherauslastung normal")
#
# Deine Aufgabe:
# 1. Lege eine Variable 'ram' an (teste verschiedene Werte, z. B. 88.5, 95.0, 42.0).
# 2. Werte den Wert aus und gib die entsprechende Meldung im Terminal aus.
# ------------------------------------------------------------------------------

ram = 93.5

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3: KI-Router (Modellauswahl)
#
# Kontext:
# Ein Dispatcher empfaengt Anfragen und soll sie an das passende Modell weiterleiten.
# Unser System unterstuetzt aktuell zwei Modelle: "gemini" und "claude".
#
# Deine Aufgabe:
# 1. Lege eine Variable 'modell' an (teste verschiedene Eingaben wie "gemini", "claude" oder "gpt-4").
# 2. Wenn "gemini" angefordert wird, gib aus, dass der Task an Gemini weitergeleitet wird.
# 3. Wenn "claude" angefordert wird, gib aus, dass der Task an Claude weitergeleitet wird.
# 4. Falls ein anderes oder unbekanntes Modell uebergeben wird, gib aus,
#    dass das Modell nicht unterstuetzt wird (inklusive des Modellnamens).
# ------------------------------------------------------------------------------

modell = "gpt"

# Hier deinen Code schreiben:



print("=" * 60)

