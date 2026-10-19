# ==============================================================================
# Modul 1.3: Listen (Lists) - Teil 8: Praxis-Mix (Listen & Logik)
# Datei: C:\Lernen_Python\01_grundlagen\listen\08_praxis_mix.py
# ==============================================================================

# [THEORIE: WIE MAN LISTEN IN DER ECHTEN PRAXIS VERWENDET]
# In der Realitaet (DevOps, Sysadmin, Backend) kombiniert man Listen oft mit:
# - Bedingungen (if / else)
# - Laengenpruefungen (len)
# - Sicherheits-Checks (in / not in)
#
# Hier wenden wir alles an, was wir in den Teilen 1 bis 5 gelernt haben:
# 1. Pruefen, wie viele Elemente vorhanden sind: len(liste)
# 2. Berechnen, wie viele Elemente fehlen: gewuenscht - len(liste)
# 3. Automatisch nachbessern: liste.append(...)
# ==============================================================================


# ==============================================================================
# [DAS MUSTERBEISPIEL: REDUNDANZ-CHECK BEI WEBSERVERN]
# Ein Dienst braucht fuer Hochverfuegbarkeit mindestens 3 Server.
# ==============================================================================
active_nodes = ["web-01", "web-02"]
required_count = 3

print(f"[DEMO START] Aktuelle Server: {active_nodes}")

# Schritt 1: Pruefen mit len()
current_count = len(active_nodes)

if current_count >= required_count:
    print(f"[DEMO OK] System ist sicher ({current_count} von {required_count} Servern aktiv).")
else:
    # Schritt 2: Berechnen, wie viele fehlen
    missing = required_count - current_count
    print(f"[DEMO WARNUNG] Zu wenig Server! Es fehlen noch {missing} Server.")
    
    # Schritt 3: Automatisch einen Notfall-Server hinzufuegen
    active_nodes.append("web-notfall-01")
    print(f"[DEMO FIX] Notfall-Server gestartet: {active_nodes}")

print("=" * 60)


# ==============================================================================
# [DEINE PRAXIS-AUFGABEN]
# ==============================================================================

# ------------------------------------------------------------------------------
# AUFGABE 1: Backup-Speicherorte und Redundanz
# Szenario:
# Ein Backup-Job nutzt aktuell zwei Speicherorte: "cloud-eu" und "nas-local".
# Vorgeschrieben sind jedoch mindestens 3 Speicherorte fuer ausreichende Sicherheit.
#
# Deine Aufgabe:
# 1. Lege eine Liste namens 'backup_locations' mit den zwei Orten an.
# 2. Pruefe, ob bereits mindestens 3 Orte vorhanden sind:
#    - Wenn ja: Gib eine Erfolgsmeldung aus ("Backup-Speicherorte ausreichend.").
#    - Wenn nein: Berechne, wie viele Orte noch fehlen, und gib eine Warnung aus
#                 mit der genauen Anzahl der fehlenden Orte.
# ------------------------------------------------------------------------------

backup_locations = ["cloud-eu", "nas-local"]
required_count = 3

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2: Auto-Recovery (Fehlenden Speicherort automatisch anhaengen)
# Szenario:
# Wir nehmen die Liste aus Aufgabe 1. Falls weniger als 3 Speicherorte vorhanden
# sind, soll das Skript automatisch reagieren und einen Notfall-Ort ("cloud-us")
# an das Ende der Liste anhaengen.
#
# Deine Aufgabe:
# 1. Lege die Liste 'backup_locations' mit "cloud-eu" und "nas-local" an.
# 2. Pruefe, ob die Laenge kleiner als 3 ist:
#    - Falls ja: Fuege "cloud-us" ans Ende der Liste hinzu und gib eine Info-Meldung aus.
# 3. Gib am Ende die gesamte Liste und deren neue Laenge auf der Konsole aus.
# ------------------------------------------------------------------------------

backup_locations = ["cloud-eu", "nas-local"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3: Firewall-Freischaltung mit Sicherheits-Check
# Szenario:
# In einer Firewall-Blacklist stehen die IPs: "10.0.0.99", "192.168.1.5", "172.16.0.4".
# Ein Admin moechte die IP "192.168.1.5" entbannen.
#
# Deine Aufgabe:
# 1. Lege die Liste 'blocklist' mit den drei IPs an.
# 2. Definiere eine Variable 'unban_ip' mit dem Wert "192.168.1.5".
# 3. Pruefe zunaechst, ob sich 'unban_ip' ueberhaupt in der Liste befindet:
#    - Ist sie vorhanden: Entferne sie gezielt und bestaetige die Freischaltung mit print().
#    - Ist sie NICHT vorhanden: Gib eine Meldung aus, dass die IP gar nicht gelistet war.
# 4. Gib die aktuelle 'blocklist' aus.
# ------------------------------------------------------------------------------

blocklist = ["10.0.0.99", "192.168.1.5", "172.16.0.4"]
unban_ip = "192.168.3.5"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 4: Zulassungs-Check mit Kapazitaetsgrenze
# Szenario:
# Ein Konferenzraum hat eine maximale Kapazitaet von 4 Teilnehmern.
# Aktuell sind eingetragen: "Alice", "Bob", "Clara".
# Ein neuer Gast ("David") moechte beitreten.
#
# Deine Aufgabe:
# 1. Lege die Liste 'teilnehmer' mit den drei aktuellen Personen an.
# 2. Pruefe, ob noch Platz im Raum ist (also ob die Anzahl kleiner als 4 ist):
#    - Wenn noch Platz ist: Fuege "David" hinzu und gib eine Willkommensmeldung aus.
#    - Wenn voll: Gib eine Meldung aus, dass der Raum voll ist.
# 3. Gib die finale Teilnehmerliste und die Gesamtzahl der Personen aus.
# ------------------------------------------------------------------------------

teilnehmer = ["Alice", "Bob", "Clara"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 5: Support-Ticket Queue (Warteschlange abarbeiten mit .pop)
# Szenario:
# In einem IT-Helpdesk liegen offene Tickets in einer Warteschlange:
# ticket_queue = ["TICKET-101", "TICKET-102", "TICKET-103"]
# Ein Admin klickt auf "Nächstes Ticket annehmen".
#
# Deine Aufgabe:
# 1. Lege die Liste 'ticket_queue' mit den drei Tickets an.
# 2. Pruefe, ob ueberhaupt Tickets in der Liste vorhanden sind (Laenge > 0):
#    - Wenn ja: Nimm das letzte Ticket mit .pop() heraus, speichere es in
#      einer Variablen 'aktuelles_ticket' und gib aus:
#      "[BEARBEITUNG] Ticket {aktuelles_ticket} wird bearbeitet."
#      Gib zusaetzlich aus, wie viele Tickets jetzt noch warten.
#    - Wenn nein (Liste leer): Gib aus: "Warteschlange ist leer! Keine Tickets."
# 3. Gib die verbleibende Liste 'ticket_queue' aus.
# ------------------------------------------------------------------------------

ticket_queue = ["TICKET-101", "TICKET-102", "TICKET-103"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 6: Monitoring & Alarm-Drosselung (mit .count() und .append())
# Szenario:
# Ein Monitoring-Server registriert Vorfaelle:
# alarms = ["CPU_HIGH", "DISK_FULL", "CPU_HIGH", "RAM_WARN"]
# Ein neuer Vorfall ("CPU_HIGH") tritt auf.
# Um das Team vor Spam zu schuetzen: Wenn ein Alarm schon 2-mal oder oefter
# in der Liste existiert, soll er NICHT mehr hinzugefuegt werden!
#
# Deine Aufgabe:
# 1. Lege die Liste 'alarms' an.
# 2. Definiere die Variable: new_alarm = "CPU_HIGH" (teste spaeter auch andere!)
# 3. Zaehle mit alarms.count(new_alarm), wie oft dieser Alarm schon existiert:
#    - Ist er >= 2: Gib eine Warnung aus:
#      "[ALARM-SPAM] {new_alarm} tritt zu oft auf! Nicht erneut hinzugefuegt."
#    - Ist er < 2: Fuege 'new_alarm' mit .append() hinzu und bestaetige:
#      "[NEUER ALARM] {new_alarm} wurde registriert."
# 4. Gib die finale Liste 'alarms' aus.
# ------------------------------------------------------------------------------

alarms = ["CPU_HIGH", "DISK_FULL", "CPU_HIGH", "RAM_WARN"]
new_alarm = "CPU_HIGH"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 7: Performance-Audit (mit .sort(), Slicing [-3:] und Latenz-Check)
# Szenario:
# Du hast Reaktionszeiten (Latenzen in Millisekunden) eines Webservers gesammelt:
# ping_times = [120, 45, 89, 310, 24, 190, 520, 15]
# Du moechtest herausfinden, was die 3 schlechtesten (hoechsten) Pings waren,
# und pruefen, ob der absolut schlechteste Wert die kritische Marke von 500 ms knackt.
#
# Deine Aufgabe:
# 1. Lege die Liste 'ping_times' mit den Zahlen an.
# 2. Sortiere die Liste aufsteigend mit .sort().
# 3. Schneide mit Slicing die letzten 3 Werte (die 3 hoechsten) heraus und speichere
#    sie in einer neuen Liste namens 'slowest_pings'. (Tipp: ping_times[-3:])
# 4. Pruefe, ob der allerletzte Wert aus 'slowest_pings' (Index -1) groesser als 500 ist:
#    - Wenn ja: Gib aus: "[KRITISCH] Maximale Latenz ueber 500ms: {hoechster_wert}ms!"
#    - Wenn nein: Gib aus: "[OK] Latenz im Rahmen: {hoechster_wert}ms."
# 5. Gib die Liste 'slowest_pings' aus.
# ------------------------------------------------------------------------------

ping_times = [120, 45, 89, 310, 24, 190, 520, 15]

# Hier deinen Code schreiben:



print("=" * 60)

