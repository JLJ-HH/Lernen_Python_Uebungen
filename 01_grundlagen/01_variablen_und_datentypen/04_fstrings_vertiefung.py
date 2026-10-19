# ==============================================================================
# Modul 1.1 - Vertiefung Runde 3: Type-Casting & f-Strings
# Datei: 04_fstrings_vertiefung.py
# ==============================================================================

# ==============================================================================
# [DAS MUSTERBEISPIEL]
# Achte besonders auf die geschweiften Klammern {} und die runden Klammern ():
# ==============================================================================

# Zeile 1: Der String-Eingangswert
download_str = "85.5"

# Zeile 2: Umwandlung (Type Casting) in float
download_zahl = float(download_str)

# Zeile 3: Berechnung (14.5 MB kommen dazu) -> NEUE VARIABLE ENTSTEHT HIER:
neuer_download = download_zahl + 14.5

# Zeile 4: Ausgabe der neuen Variable im f-String:
#          In den geschweiften Klammern {} steht exakt der Name aus Zeile 3!
print(f"Gesamter Download: {neuer_download} Megabyte")

# Zeile 5: Datentyp mit type() im f-String pruefen:
#          Aussen geschweift {}, innen runde Klammern () fuer type(...):
print(f"Datentyp des Ergebnisses: {type(neuer_download)}")
print("=" * 60)


# ==============================================================================
# [DEINE 6 TRAININGS-AUFGABEN]
# Versuche sie diesmal zu loesen, ohne nach oben zum Beispiel zu schauen!
# Merkregel:
# - In {} kommt immer dein Variablenname aus der Berechnung.
# - Bei type() heisst es immer: {type(deine_berechnete_variable)}
# ==============================================================================

# ------------------------------------------------------------------------------
# AUFGABE 1: CPU-Auslastung eines Agenten-Servers
# Die aktuelle CPU-Last liegt bei 68.4 Prozent (als String).
# 1. Wandle 'cpu_str' in eine Kommazahl (float) um.
# 2. Durch einen intensiven Task steigt die Last um 11.2 Prozent. Berechne den neuen Wert.
# 3. Gib das Ergebnis mit einem f-String aus:
#    "Neue CPU-Auslastung: X Prozent"
# 4. Gib den Datentyp des neuen Werts mit {type(...)} aus.
# ------------------------------------------------------------------------------

cpu_str = "68.4"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2: Bot-Nachrichten Zaehler
# Ein Chatbot hat heute bereits 230 Nachrichten verschickt (als String).
# 1. Wandle 'nachrichten_str' in eine Ganzzahl (int) um.
# 2. Eine neue User-Gruppe generiert weitere 70 Nachrichten. Berechne die Gesamtzahl.
# 3. Gib das Ergebnis mit einem f-String aus:
#    "Gesendete Nachrichten heute: X Nachrichten"
# 4. Gib den Datentyp des Gesamtwerts mit {type(...)} aus.
# ------------------------------------------------------------------------------

nachrichten_str = "230"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3: Akkulaufzeit / Akkuprozent
# Ein autonomes Geraet meldet einen Akkustand von 95.0 Prozent (als String).
# 1. Wandle 'akku_str' in eine Kommazahl (float) um.
# 2. Nach einem langen Einsatz sinkt der Akku um 18.5 Prozent. Berechne den Reststand.
# 3. Gib das Ergebnis mit einem f-String aus:
#    "Verbleibende Akkukapazitaet: X Prozent"
# 4. Gib den Datentyp des Reststands mit {type(...)} aus.
# ------------------------------------------------------------------------------

akku_str = "95.0"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 4: API-Kosten berechnen (Multiplikation & float)
# Ein Cloud-Dienst verlangt pro Abfrage 0.05 Euro (als String).
# 1. Wandle 'preis_pro_abfrage_str' in float um.
# 2. Ein Script fuehrt 100 Abfragen durch. Berechne die Gesamtkosten (preis * 100).
# 3. Gib das Ergebnis mit einem f-String aus:
#    "Gesamtkosten fuer 100 Abfragen: X Euro"
# 4. Gib den Datentyp der Gesamtkosten mit {type(...)} aus.
# ------------------------------------------------------------------------------

preis_str = "0.05"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 5: Systemstatus / Sensor-Flag (Zahl zu bool im f-String)
# Ein IoT-Sensor liefert seinen Zustand als Zahl: 1 bedeutet 'online', 0 'offline'.
# 1. Wandle 'sensor_code' mit bool() in einen Wahrheitswert um.
# 2. Gib den Zustand mit einem f-String aus:
#    "Sensor online: X"
# 3. Gib den Datentyp des Zustands mit {type(...)} aus.
# ------------------------------------------------------------------------------

sensor_flag = 1

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 6: Server-Speicher aufteilen (Division & float)
# Es stehen 120.0 GB freier Speicher zur Verfuegung (als String).
# Dieser Speicher soll gleichmaessig auf 4 Agenten verteilt werden (/ 4).
# 1. Wandle 'speicher_gesamt_str' in float um.
# 2. Berechne den Speicher pro Agent (speicher / 4).
# 3. Gib das Ergebnis mit einem f-String aus:
#    "Speicherplatz pro Agent: X GB"
# 4. Gib den Datentyp des Ergebnisses mit {type(...)} aus.
# ------------------------------------------------------------------------------

gesamt_speicher_str = "100.0"

# Hier deinen Code schreiben:



print("=" * 60)

