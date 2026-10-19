# ==============================================================================
# Modul 1.3: Listen (Lists) - Teil 5: Laenge messen (len) & Erweitern (.append)
# Datei: C:\Lernen_Python\01_grundlagen\listen\05_len_append.py
# ==============================================================================

# [THEORIE: ZWEI ELEMENTARE LISTEN-WERKZEUGE]
# Listen wachsen und schrumpfen dynamisch. Um die Kontrolle darueber zu behalten,
# brauchst du zwei fundamentale Werkzeuge:
#
# KONZEPT 1: Die Laenge einer Liste messen mit 'len()'
#   - 'len(meine_liste)' zaehlt, wie viele Elemente sich in der Liste befinden.
#   - Das Ergebnis ist immer eine ganze Zahl (Datentyp 'int').
#   - Wichtig: 'len()' zaehlt die reale Anzahl an Elementen (1, 2, 3...),
#     nicht den Index (der bei 0 beginnt)!
#     Beispiel: len(["a", "b", "c"]) ergibt 3.
#
# KONZEPT 2: Neue Elemente hinten anhaengen mit '.append()'
#   - 'meine_liste.append(neuer_wert)' packt einen neuen Wert ans Ende der Liste.
#   - Die Liste wird direkt veraendert ("in-place").
#   - Merke: Man schreibt nur 'meine_liste.append("x")', kein 'liste = ...'!
# ==============================================================================


# ==============================================================================
# [MUSTERBEISPIELE]
# ==============================================================================

# --- DEMO 1: LAENGE EINER LISTE MESSEN MIT len() ---
active_nodes = ["web-01", "web-02", "db-01"]
node_count = len(active_nodes)

print(f"[DEMO 1] Liste: {active_nodes}")
print(f"[DEMO 1] Anzahl der Server: {node_count}")

print("-" * 40)

# --- DEMO 2: ELEMENT HINTEN ANHAENGEN MIT .append() ---
queue = ["job_01", "job_02"]
print(f"[DEMO 2 vor append]  Warteschlange: {queue}")

# Neuen Job anhaengen:
queue.append("job_03")
print(f"[DEMO 2 nach append] Warteschlange: {queue}")
print(f"[DEMO 2 neue Laenge] Jetzt sind {len(queue)} Jobs enthalten.")

print("=" * 60)


# ==============================================================================
# [DEINE UEBUNGSAUFGABEN]
# ==============================================================================

# ------------------------------------------------------------------------------
# AUFGABE 1 (zu Konzept 1: len()):
# Szenario:
# Du pruefst den Bestand an Server-Knoten in einem Rechenzentrum.
#
# Deine Aufgabe:
# 1. Erstelle eine Liste 'cluster_nodes' mit 4 beliebigen Server-Namen (z. B. "node-a", "node-b", ...).
# 2. Ermittle mit 'len(cluster_nodes)' die Laenge der Liste.
# 3. Gib auf der Konsole folgenden Satz mit f-String aus:
#    "Im Cluster sind aktuell <anzahl> Knoten aktiv."
# ------------------------------------------------------------------------------

cluster_nodes = ["node-a", "node-b", "node-c", "node-d"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2 (zu Konzept 1: len()):
# Szenario:
# Vor einem System-Backup liegen ausstehende Backup-Dateien vor.
#
# Deine Aufgabe:
# 1. Erstelle eine Liste 'backup_files' mit 3 Dateinamen: ["daten.sql", "config.tar", "bilder.zip"].
# 2. Speichere die Laenge der Liste in einer Variablen 'total_files'.
# 3. Gib mit einem f-String aus:
#    "Gefundene Backup-Dateien: <total_files>"
# ------------------------------------------------------------------------------

backup_files = ["daten.sql", "config.tar", "bilder.zip"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3 (zu Konzept 2: .append()):
# Szenario:
# Eine Firewall-Konfiguration enthaelt eine Liste freigegebener Ports: [22, 80, 443].
# Der verschluesselte DNS-Port 853 soll neu zur Liste hinzugefuegt werden.
#
# Deine Aufgabe:
# 1. Lege die Liste 'allowed_ports' mit den drei Zahlen [22, 80, 443] an.
# 2. Fuege die Zahl 853 mit '.append()' hinten an die Liste an.
# 3. Gib die gesamte Liste 'allowed_ports' mit print() aus.
# ------------------------------------------------------------------------------

allowed_ports = [22, 80, 443]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 4 (zu Konzept 2: .append()):
# Szenario:
# Ein Systemlog protokolliert neue Ereignisse fortlaufend.
#
# Deine Aufgabe:
# 1. Lege eine Liste 'audit_log' an mit einem Start-Eintrag: ["System gestartet"].
# 2. Fuege mit einem ersten '.append()'-Aufruf "Benutzer angemeldet" hinzu.
# 3. Fuege mit einem zweiten '.append()'-Aufruf "Backup erfolgreich" hinzu.
# 4. Gib mit einem f-String die finale Liste und die Gesamtzahl der Eintraege aus:
#    "Audit-Log (<anzahl> Eintraege): <audit_log>"
# ------------------------------------------------------------------------------

audit_log = ["System gestartet"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 5 (zu Konzept 1: len()):
# Szenario:
# Ein Mailserver ueberwacht eine ausgehende E-Mail-Warteschlange:
# mail_spool = ["mail_01.eml", "mail_02.eml", "mail_03.eml", "mail_04.eml", "mail_05.eml"]
#
# Deine Aufgabe:
# 1. Lege die Liste 'mail_spool' mit den 5 Eintraegen an.
# 2. Ermittle mit len(mail_spool) die Anzahl der wartenden Mails und speichere
#    sie in 'pending_mails'.
# 3. Gib mit einem f-String aus:
#    "Ausgehende Warteschlange: {pending_mails} E-Mails stehen zum Versand bereit."
# ------------------------------------------------------------------------------

mail_spool = ["mail_01.eml", "mail_02.eml", "mail_03.eml", "mail_04.eml", "mail_05.eml"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 6 (zu Konzept 2: .append()):
# Szenario:
# Auf einem Server laufen Docker-Container:
# running_containers = ["web_app", "redis_cache"]
# Ein neuer Container namens "postgres_db" wird gestartet.
#
# Deine Aufgabe:
# 1. Lege die Liste 'running_containers' mit den beiden Containern an.
# 2. Fuege den Container "postgres_db" mit '.append()' hinten an die Liste an.
# 3. Gib mit einem f-String die neue Liste und deren Gesamtzahl aus:
#    "Aktive Container ({len(running_containers)}): {running_containers}"
# ------------------------------------------------------------------------------

running_containers = ["web_app", "redis_cache"]

# Hier deinen Code schreiben:



print("=" * 60)

