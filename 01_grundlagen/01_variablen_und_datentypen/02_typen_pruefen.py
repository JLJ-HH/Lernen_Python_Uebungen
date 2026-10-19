# ==============================================================================
# Modul 1.1: Grundlagen - Datentypen ermitteln mit type()
# Datei: 02_typen_pruefen.py
# ==============================================================================

# [DER DETEKTIV: type()]
# Im letzten Schritt hast du gelernt, Werte in Variablen zu speichern.
# Jetzt wollen wir Python fragen: "Welchen Datentyp hat dieser Wert eigentlich?"
#
# Dafuer gibt es in Python die eingebaute Funktion: type(...)
# Du kannst dir type() wie eine Roentgenbrille oder einen Pruefstempel vorstellen:
# Sie schaut in die Schachtel und ermittelt die Art des Inhalts.
#
# WIE FUNKTIONIERT print(type(variable))? (Von innen nach aussen in 3 Schritten)
# Beispiel:
#   auto = "BMW"
#   print(type(auto))
#
#   Schritt 1: Python nimmt die Schachtel 'auto' und holt den Wert heraus -> "BMW"
#   Schritt 2: type("BMW") ermittelt die Kategorie -> <class 'str'>
#   Schritt 3: print(...) zeigt diesen Pruefstempel auf dem Bildschirm an!
#
# Was bedeutet die Ausgabe <class '...'>?
# - 'class' bedeutet einfach "Kategorie" oder "Bauart".
# - Die 4 wichtigsten Typ-Stempel in Python:
#   - <class 'str'>   fuer String (Text)
#   - <class 'int'>   fuer Integer (Ganze Zahl)
#   - <class 'float'> fuer Float (Kommazahl)
#   - <class 'bool'>  fuer Boolean (Wahrheitswert)
#
# WICHTIG:
# Bei type(auto) KEINE Anfuehrungszeichen um den Variablennamen setzen!
# Sonst wuerde Python das Wort "auto" als Text untersuchen, statt in die Schachtel zu schauen.

# ==============================================================================
# [BEISPIELE]
# ==============================================================================

stadt = "Berlin"
alter = 30
gewicht = 72.5
ist_admin = False

print(type(stadt))       # <class 'str'>
print(type(alter))       # <class 'int'>
print(type(gewicht))     # <class 'float'>
print(type(ist_admin))   # <class 'bool'>

print("=" * 60)

# ==============================================================================
# [DER GROSSE AHA-EFFEKT: TEXT VS. ZAHL]
# Achte genau auf die Anfuehrungszeichen!
# ==============================================================================

wert_text = "100"      # Steht in Anfuehrungszeichen -> Python sieht es als Text!
wert_zahl = 100        # Steht ohne Anfuehrungszeichen -> Python sieht es als ganze Zahl!

print(type(wert_text))   # <class 'str'>
print(type(wert_zahl))   # <class 'int'>

print("=" * 60)


# ==============================================================================
# [DEINE UEBUNGSAUFGABEN]
# ==============================================================================

# Aufgabe 1: String pruefen
# Erstelle eine Variable namens 'auto_marke' mit einer Automarke deiner Wahl als Text (z. B. "Audi" oder "BMW").
# Gib den Datentyp dieser Variable mit print() und type() aus.

# Hier deinen Code schreiben:



print("-" * 60)


# Aufgabe 2: Integer pruefen
# Erstelle eine Variable namens 'postleitzahl' mit einer beliebigen Postleitzahl als ganze Zahl (z. B. 20095).
# Gib den Datentyp dieser Variable mit print() und type() aus.

# Hier deinen Code schreiben:



print("-" * 60)


# Aufgabe 3: Float pruefen
# Erstelle eine Variable namens 'benzin_preis' mit einem beliebigen Literpreis als Kommazahl (z. B. 1.79).
# Gib den Datentyp dieser Variable mit print() und type() aus.

# Hier deinen Code schreiben:



print("-" * 60)


# Aufgabe 4: Boolean pruefen
# Erstelle eine Variable namens 'motor_laeuft' mit einem Wahrheitswert (True oder False).
# Gib den Datentyp dieser Variable mit print() und type() aus.

# Hier deinen Code schreiben:



print("-" * 60)


# Aufgabe 5: Quiz - Welcher Typ entsteht bei der Division?
# Wenn du zwei ganze Zahlen teilst (z. B. 10 geteilt durch 2):
# div_ergebnis = 10 / 2
# Pruefe mit print() und type(), welchen Datentyp Python dem Ergebnis gibt.
# Ist es ein int oder ein float? (Lass dich vom Ergebnis ueberraschen!)

div_ergebnis = 10 / 2

# Hier deinen Code schreiben:



print("=" * 60)

