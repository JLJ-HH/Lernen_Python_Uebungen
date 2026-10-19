# ==============================================================================
# Modul 1.3: Listen (Lists) - Teil 2: Werte aendern & Vorhandensein pruefen
# Datei: C:\Lernen_Python\01_grundlagen\listen\02_update_in.py
# ==============================================================================

# [THEORIE: ZWEI WICHTIGE LISTEN-KONZEPTE]
# Listen sind veraenderbar (mutable) und erlauben einfache Abfragen.
# In dieser Datei ueben wir genau zwei Dinge:
#
# KONZEPT 1: Element an einer Position ueberschreiben (Updaten)
#   Genau wie Variablen koennen wir eine Stelle in der Liste neu zuweisen:
#   meine_liste[0] = "neuer_wert"   # Ersetzt das erste Element
#   meine_liste[1] = "anderer_wert" # Ersetzt das zweite Element
#
# KONZEPT 2: Pruefen mit 'in' (und 'not in')
#   Prueft, ob ein Wert in der Liste enthalten ist (gibt True oder False):
#   if "gesuchter_wert" in meine_liste:
#       print("Gefunden!")
#   else:
#       print("Nicht vorhanden!")
# ==============================================================================


# ==============================================================================
# [MUSTERBEISPIELE]
# ==============================================================================

# --- DEMO 1: WERT UEBERSCHREIBEN ---
cluster = ["web-01", "db-alt", "cache-01"]
print(f"[DEMO 1 vor Update]  Cluster: {cluster}")

# Wir tauschen 'db-alt' (Index 1) gegen 'db-neu' aus:
cluster[1] = "db-neu"
print(f"[DEMO 1 nach Update] Cluster: {cluster}")

print("-" * 40)

# --- DEMO 2: VORHANDENSEIN MIT 'in' PRUEFEN ---
server_names = ["web-01", "api-01", "db-01"]
search_node = "web-01"

if search_node in server_names:
    print(f"[DEMO 2] Server '{search_node}' ist in der Liste vorhanden.")
else:
    print(f"[DEMO 2] Server '{search_node}' existiert nicht in der Liste.")

print("=" * 60)


# ==============================================================================
# [DEINE UEBUNGSAUFGABEN]
# ==============================================================================

# ------------------------------------------------------------------------------
# AUFGABE 1 (zu Konzept 1): Einzelnen Port austauschen
# Szenario:
# Ein System hat 3 Standard-Ports konfiguriert: [80, 8080, 443].
# Der unverschluesselte Web-Port 80 (Index 0) soll durch Port 8000 ersetzt werden.
#
# Deine Aufgabe:
# 1. Erstelle die Liste: network_ports = [80, 8080, 443]
# 2. Ueberschreibe das ERSTE Element (Index 0) mit der Zahl 8000:
#    network_ports[0] = 8000
# 3. Gib die gesamte Liste mit print() aus.
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2 (zu Konzept 1): Status in einer Status-Liste aktualisieren
# Szenario:
# Du ueberwachst 3 Container mit ihren Zustaenden: ["running", "starting", "stopped"].
# Der Container an Index 1 ist jetzt fertig gestartet und soll auf "running" gesetzt werden.
#
# Deine Aufgabe:
# 1. Erstelle die Liste: container_status = ["running", "starting", "stopped"]
# 2. Ueberschreibe den Zustand an Index 1 mit dem Wert "running":
#    container_status[1] = "running"
# 3. Gib die aktualisierte Liste mit print() aus.
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3 (zu Konzept 2): Benutzerrolle pruefen mit 'in'
# Szenario:
# Eine Liste definiert Administrator-Rollen: ["admin", "superadmin", "owner"].
# Ein angemeldeter Nutzer hat die Rolle: current_role = "admin"
#
# Deine Aufgabe:
# 1. Erstelle die Liste: admin_roles = ["admin", "superadmin", "owner"]
# 2. Erstelle die Variable: current_role = "admin"
# 3. Pruefe mit if/else und 'in':
#    - Wenn current_role in admin_roles ist: gib aus "Zugriff gewaehrt: Admin-Bereich"
#    - Sonst: gib aus "Zugriff verweigert"
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 4 (zu Konzept 2): Domain-Sperrliste (Blacklist) pruefen
# Szenario:
# Ein Webfilter blockiert verbotene Domains: ["malware.com", "spam.net", "phishing.org"]
# Eine angefragte Adresse lautet: requested_domain = "google.com"
#
# Deine Aufgabe:
# 1. Erstelle die Liste: blocked_domains = ["malware.com", "spam.net", "phishing.org"]
# 2. Erstelle die Variable: requested_domain = "google.com"
# 3. Pruefe mit if/else:
#    - Wenn requested_domain in blocked_domains ist:
#        gib aus: "Warnung: Domain ist blockiert!"
#    - Sonst:
#        gib aus: "Domain ist sicher und erreichbar."
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 5 (zu Konzept 1: Wert ueberschreiben):
# Szenario:
# In einer Datenbank-Konfiguration steht der Hostname aktuell noch auf der lokalen Test-Adresse:
# db_endpoints = ["127.0.0.1", "localhost", "port-5432"]
# Fuer den Produktivbetrieb muss der zweite Eintrag (Index 1) auf "db-prod.internal" aktualisiert werden.
#
# Deine Aufgabe:
# 1. Lege die Liste 'db_endpoints' mit den 3 Werten an.
# 2. Ueberschreibe das Element an Index 1 mit dem neuen String "db-prod.internal".
# 3. Gib mit print() die aktualisierte Liste aus.
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 6 (zu Konzept 2: Pruefen mit 'in'):
# Szenario:
# Auf einem Server sind verschiedene Sicherheitszertifikate hinterlegt:
# installed_certs = ["wildcard-ssl", "internal-ca", "vpn-client"]
# Das System prueft vor dem Start, ob das erforderliche Zertifikat 'api-gateway' vorhanden ist.
#
# Deine Aufgabe:
# 1. Lege die Liste 'installed_certs' an.
# 2. Definiere die Variable: check_cert = "api-gateway"
# 3. Pruefe mit if / else und 'in':
#    - Wenn 'check_cert' in 'installed_certs' ist:
#      Gib aus: "[OK] Zertifikat {check_cert} ist installiert."
#    - Sonst:
#      Gib aus: "[FEHLER] Zertifikat {check_cert} fehlt! Bitte neu ausstellen."
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("=" * 60)

