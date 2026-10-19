# ==============================================================================
# Modul 1.2 - Profi-Muster: Logik umkehren (Fehler zuerst) & Verschachteln
# Datei: C:\Lernen_Python\01_grundlagen\bedingungen\05_logik_umkehren_und_schachteln.py
# ==============================================================================
# Bisher haben wir oft gefragt: "Wenn alles perfekt ist, mach weiter!"
# In der echten Software-Entwicklung macht man es sehr oft genau ANDERSRUM:
# Man fängt zuerst alle Fehler und Ausschlusskriterien ab.
#
# Hier lernst du zwei mächtige Denkweisen:
#
# 1. DER "ANDERSRUM-WEG" (Guard Clause / Fehler zuerst abfangen):
#    Statt zu prüfen, ob alles stimmt, prüfen wir, was FEHLT:
#    if eingeloggt == False:
#        print("Abgebrochen: Nicht eingeloggt!")
#    elif volumen_mb < 50:
#        print("Abgebrochen: Zu wenig Datenvolumen!")
#    else:
#        print("Erfolg: Download startet!")
#
# 2. VERSCHACHTELTE BEDINGUNGEN (Nested if):
#    Ein 'if' innerhalb eines anderen 'if':
#    if eingeloggt == True:
#        if volumen_mb >= 50:
#            print("Download gestartet.")
#        else:
#            print("Zu wenig Volumen.")
#    else:
#        print("Nicht eingeloggt.")
# ==============================================================================


# ------------------------------------------------------------------------------
# AUFGABE 1: Der "Andersrum-Weg" (Musterbeispiel zum Verstehen)
# Szenario:
# Ein Bot soll einen Trade an einer Krypto-Börse platzieren.
# Voraussetzungen: API-Key vorhanden und Kontostand mindestens 100 Euro.
# Wir prüfen zuerst die Fehlergründe!
# ------------------------------------------------------------------------------
has_api_key = True
kontostand = 45.0

if has_api_key == False:
    print("Trade abgelehnt: Kein API-Key hinterlegt.")
elif kontostand < 100.0:
    print(f"Trade abgelehnt: Nur {kontostand} Euro Guthaben (mind. 100 Euro noetig).")
else:
    print("Trade erfolgreich ausgefuehrt!")

print("-" * 60)

# ------------------------------------------------------------------------------

# AUFGABE 2: Verschachtelung (Musterbeispiel zum Verstehen)
# Szenario:
# Ein Benutzer will eine Premium-Funktion nutzen.
# Erst prüfen wir, ob er registriert ist. Nur wenn ja, prüfen wir das Abo.
# ------------------------------------------------------------------------------
ist_registriert = True
ist_premium = False

if ist_registriert == True:
    if ist_premium == True:
        print("Zugriff auf alle Premium-Inhalte erlaubt.")
    else:
        print("Zugriff beschraenkt: Bitte auf Premium upgraden.")
else:
    print("Zugriff verweigert: Bitte zuerst registrieren.")

print("-" * 60)

# ------------------------------------------------------------------------------

# AUFGABE 3: Der Andersrum-Weg (Selbst umsetzen)
# Szenario:
# Ein Datei-Upload auf einen Cloud-Server darf nur stattfinden, wenn:
# - Die Datei kleiner oder gleich 20 MB ist (dateigroesse_mb <= 20)
# - Der Dateityp "pdf" ist (dateityp == "pdf")
#
# Deine Aufgabe:
# Fange zuerst die Fehler einzeln ab (z. B. mit if / elif)!
# 1. Lege 'dateigroesse_mb' (Zahl, z. B. 25) und 'dateityp' (String, z. B. "png") an.
# 2. Wenn der Typ nicht "pdf" ist: Gib eine Fehlermeldung aus (z. B. "Falscher Dateityp: nur PDF erlaubt").
# 3. Wenn die Datei zu gross ist: Gib eine Fehlermeldung aus (z. B. "Datei zu gross: max. 20 MB erlaubt").
# 4. Wenn alles passt (else): Gib eine Erfolgsmeldung aus (z. B. "Upload erfolgreich gestartet.").
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 4: Verschachteltes System (Selbst umsetzen)
# Szenario:
# Ein Sicherheitsterminal gewährt Zutritt zu einem Rechenzentrum.
# - Stufe 1: Der Transponder muss gültig sein ('transponder_ok' ist True).
# - Stufe 2 (nur wenn Stufe 1 bestanden): Der PIN-Code muss 1234 lauten ('pin == 1234').
#
# Deine Aufgabe:
# Baue eine verschachtelte if-Struktur:
# 1. Lege 'transponder_ok' (Boolean) und 'pin' (Ganzzahl) an.
# 2. Wenn der Transponder gültig ist:
#    -> Prüfe im inneren if die PIN:
#       - PIN korrekt: Zutritt gewähren (z. B. "pin").
#       - PIN falsch: Fehler melden (z. B. "Falsche PIN: Alarm ausgeloest!").
# 3. Wenn der Transponder ungültig ist (äusseres else):
#    -> Zutritt verweigern (z. B. "Transponder ungueltig: Zutritt verwehrt.").
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("=" * 60)

