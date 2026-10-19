# ==============================================================================
# Modul 1.2 - Die nächste Stufe: Mehrere Bedingungen verknüpfen (and / or)
# Datei: C:\Lernen_Python\01_grundlagen\bedingungen\04_logische_operatoren_and_or.py
# ==============================================================================

# [DIE NEUE HÜRDE: LOGISCHE OPERATOREN]
# In der echten Praxis reicht oft nicht nur EINE Bedingung.
# Ein Agent darf z. B. nur starten, wenn:
# - Der Akku voll ist UND das System nicht überhitzt ist.
#
# Dafür gibt es in Python zwei einfache englische Wörter:
#
# 1. 'and' (UND):
#    BEIDE Bedingungen müssen True sein, damit der Block ausgeführt wird.
#    Beispiel:
#    if akku >= 20 and temp <= 80.0:
#        print("System startklar!")
#
# 2. 'or' (ODER):
#    MINDESTENS EINE der Bedingungen muss True sein (es reicht, wenn eine stimmt).
#    Beispiel:
#    if rolle == "admin" or rolle == "chef":
#        print("Zugriff erlaubt!")
# ==============================================================================


# ------------------------------------------------------------------------------
# AUFGABE 1: Agenten-Freigabe mit 'and' (UND)
# Szenario: Ein KI-Agent darf einen Auftrag nur ausführen, wenn:
# - Sein Guthaben mindestens 0.10 Euro beträgt (guthaben >= 0.10)
#   UND
# - Er mindestens 5 freie Slots hat (slots >= 5)
#
# Schreibe ein if / else mit 'and':
# - WENN guthaben >= 0.10 and slots >= 5:
#   Gib aus: "Auftrag freigegeben: Guthaben und Slots vorhanden."
# - SONST (else):
#   Gib aus: "Auftrag abgelehnt: Zu wenig Guthaben oder keine Slots."
# ------------------------------------------------------------------------------

guthaben = 0.25
slots = 8

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2: Notfall-Alarm mit 'or' (ODER)
# Szenario: Ein Server schlaegt Alarm, wenn:
# - Die CPU-Last ueber 95.0 Prozent liegt (cpu > 95.0)
#   ODER
# - Die Festplatte zu ueber 98.0 Prozent voll ist (festplatte > 98.0)
# (Es reicht also schon, wenn nur EINES von beiden eintrifft!)
#
# Schreibe ein if / else mit 'or':
# - WENN cpu > 95.0 or festplatte > 98.0:
#   Gib aus: "NOTFALL: Kritischer Server-Zustand gemeldet!"
# - SONST (else):
#   Gib aus: "Systemzustand stabil."
# ------------------------------------------------------------------------------

cpu = 96.2
festplatte = 70.0

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3: Login-Berechtigung (Rollenprüfung)
# Szenario:
# Zugang zum Entwickler-Dashboard haben Benutzer mit der Rolle "admin"
# ODER der Rolle "developer".
#
# Deine Aufgabe:
# 1. Lege eine Variable 'rolle' an (teste z. B. "admin", "developer" oder "hr").
# 2. Pruefe die Berechtigung:
#    - Falls zutreffend: Gib aus, dass der Zugang gewaehrt wird (z. B. mit f-String und Rolle).
#    - Andernfalls: Gib aus, dass der Zugang verweigert wird (z. B. mit f-String und Rolle).
# ------------------------------------------------------------------------------

rolle = "user"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 4: Download-Freigabe (Kriterienprüfung)
# Szenario:
# Ein Benutzer moechte eine Datei herunterladen. Der Download darf nur starten,
# wenn der Nutzer eingeloggt ist (True) UND mindestens 50 MB Datenvolumen uebrig hat.
#
# Deine Aufgabe:
# 1. Lege zwei Variablen an: 'eingeloggt' (Boolean) und 'volumen_mb' (Zahl).
# 2. Pruefe, ob beide Kriterien gleichzeitig erfuellt sind:
#    - Bei Erfolg: Gib eine Bestaetigung aus (z. B. "Download gestartet.").
#    - Andernfalls: Gib eine Meldung aus, dass der Download abgelehnt wird.
# ------------------------------------------------------------------------------

eingeloggt = False
volumen_mb = 60

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 5: Kostenloser Versand (Vorteilsprüfung)
# Szenario:
# Ein Online-Shop schenkt dem Kunden die Versandkosten, wenn der Warenkorb-Wert
# mindestens 50 Euro erreicht ODER der Kunde den Status "premium" besitzt.
#
# Deine Aufgabe:
# 1. Lege zwei Variablen an: 'warenkorb' (Zahl) und 'kundenstatus' (String, z. B. "standard" oder "premium").
# 2. Pruefe, ob mindestens eine der Bedingungen zutrifft:
#    - Wenn ja: Gib aus, dass der Versand kostenlos ist (z. B. "Versandkostenfrei!").
#    - Sonst: Gib aus, dass Versandkosten berechnet werden.
# ------------------------------------------------------------------------------

warenkorb = 45
kundenstatus = "standard"

# Hier deinen Code schreiben:



print("=" * 60)

