# ==============================================================================
# Modul 1.1: Grundlagen - Vergleichsoperatoren (True / False)
# Datei: 05_vergleichsoperatoren.py
# ==============================================================================

# [WAS SIND VERGLEICHSOPERATOREN?]
# Mit Vergleichsoperatoren vergleichen wir zwei Werte miteinander.
# Das Ergebnis eines Vergleichs ist NIEMALS eine Zahl, sondern IMMER ein Wahrheitswert (bool):
# Entweder True (wahr) oder False (falsch).
#
# Die 6 wichtigsten Vergleichsoperatoren in Python:
#   >   strikter als 'groesser als'         (z. B. 15 > 10  -> True)
#   <   strikter als 'kleiner als'          (z. B. 5 < 10   -> True)
#   >=  'groesser oder gleich' (Mindestwert)(z. B. 10 >= 10 -> True)
#   <=  'kleiner oder gleich' (Hoechstwert) (z. B. 10 <= 10 -> True)
#   ==  'exakt gleich'                      (z. B. 200 == 200 -> True)
#       -> WICHTIG: Ein einzelnes '=' weist einen Wert zu (x = 5).
#                   Ein doppeltes '==' vergleicht zwei Werte!
#   !=  'ungleich' / 'nicht gleich'         (z. B. 5 != 10  -> True)

# ==============================================================================
# [DAS MUSTERBEISPIEL]
# ==============================================================================

# 1. Ein Wert kommt als String rein (z. B. aus einer Web-Eingabe):
alter_str = "17"

# 2. In eine Zahl umwandeln:
alter = int(alter_str)

# 3. Vergleichen (Pruefen, ob die Person mindestens 18 Jahre alt ist):
#    Python fuehrt den Vergleich 'alter >= 18' aus und speichert True oder False!
ist_volljaehrig = alter >= 18

# 4. Ausgabe mit f-String und Typ-Pruefung:
print(f"Ist die Person volljaehrig? {ist_volljaehrig}")
print(f"Datentyp des Ergebnisses: {type(ist_volljaehrig)}")

print("=" * 60)


# ==============================================================================
# [DEINE 6 PRAXIS-AUFGABEN]
# In jeder Aufgabe lernst du genau einen der 6 Operatoren kennen!
# ==============================================================================

# ------------------------------------------------------------------------------
# AUFGABE 1: Operator '>' (Strikt groesser als)
# Szenario: Ein Server-Monitoring meldet die aktuelle CPU-Temperatur.
# Ein Alarm wird ausgeloest, wenn die Temperatur STRIKT GROESSER als 75.0 Grad ist.
#
# 1. Wandle 'temperatur_str' in float um.
# 2. Pruefe mit '>', ob die Temperatur groesser als 75.0 ist.
# 3. Gib das Ergebnis mit einem f-String aus:
#    "Temperatur-Alarm ausgeloest: X"
# 4. Gib den Datentyp des Ergebnisses mit {type(...)} aus.
# ------------------------------------------------------------------------------

temperatur_str = "82.4"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2: Operator '<' (Strikt kleiner als)
# Szenario: Ein Smartphone prueft den Akkustand.
# Der Energiesparmodus soll aktivieren, wenn der Akku STRIKT KLEINER als 20 Prozent ist.
#
# 1. Wandle 'akku_str' in int um.
# 2. Pruefe mit '<', ob der Akku kleiner als 20 ist.
# 3. Gib das Ergebnis mit einem f-String aus:
#    "Energiesparmodus aktivieren: X"
# 4. Gib den Datentyp des Ergebnisses mit {type(...)} aus.
# ------------------------------------------------------------------------------

akku_str = "15"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3: Operator '>=' (Groesser oder gleich / Mindestwert)
# Szenario: Ein Download erfordert mindestens 10.0 Megabyte freien Speicher.
#
# 1. Wandle 'freier_speicher_str' in float um.
# 2. Pruefe mit '>=', ob der freie Speicher groesser oder gleich 10.0 ist.
# 3. Gib das Ergebnis mit einem f-String aus:
#    "Genug Speicherplatz vorhanden: X"
# 4. Gib den Datentyp des Ergebnisses mit {type(...)} aus.
# ------------------------------------------------------------------------------

freier_speicher_str = "10.0"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 4: Operator '<=' (Kleiner oder gleich / Maximalgrenze)
# Szenario: Ein Paketdienst erlaubt Pakete bis maximal 5.0 kg Gewicht.
#
# 1. Wandle 'paket_gewicht_str' in float um.
# 2. Pruefe mit '<=', ob das Gewicht kleiner oder gleich 5.0 kg ist.
# 3. Gib das Ergebnis mit einem f-String aus:
#    "Paketgewicht im zulaessigen Rahmen: X"
# 4. Gib den Datentyp des Ergebnisses mit {type(...)} aus.
# ------------------------------------------------------------------------------

paket_gewicht_str = "4.2"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 5: Operator '==' (Exakt gleich)
# Szenario: Eine Web-API meldet einen HTTP-Statuscode.
# Ein Aufruf war erfolgreich, wenn der Statuscode EXAKT GLEICH 200 ist.
#
# 1. Wandle 'status_str' in int um.
# 2. Pruefe mit '==', ob der Statuscode genau 200 ist.
# 3. Gib das Ergebnis mit einem f-String aus:
#    "API-Anfrage erfolgreich (Code 200): X"
# 4. Gib den Datentyp des Ergebnisses mit {type(...)} aus.
# ------------------------------------------------------------------------------

status_str = "200"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 6: Operator '!=' (Ungleich / Nicht gleich)
# Szenario: Ein Login-System prueft, ob der eingegebene Fehlercode NICHT 0 ist.
# 0 bedeutet 'kein Fehler'. Jeder andere Code bedeutet 'Es gibt einen Fehler'.
#
# 1. Wandle 'fehlercode_str' in int um.
# 2. Pruefe mit '!=', ob der Fehlercode ungleich 0 ist.
# 3. Gib das Ergebnis mit einem f-String aus:
#    "Fehler aufgetreten: X"
# 4. Gib den Datentyp des Ergebnisses mit {type(...)} aus.
# ------------------------------------------------------------------------------

fehlercode_str = "404"

# Hier deinen Code schreiben:



print("=" * 60)

