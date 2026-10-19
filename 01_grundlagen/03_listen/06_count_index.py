# ==============================================================================
# Modul 1.3: Listen (Lists) - Teil 6: Vorkommen zaehlen (.count) & Position finden (.index)
# Datei: C:\Lernen_Python\01_grundlagen\listen\06_count_index.py
# ==============================================================================

# [THEORIE: ZWEI PRAKTISCHE ANALYSE-METHODEN]
# Wenn Listen laenger werden, moechte man Daten auswerten, ohne jedes Element
# von Hand absuchen zu muessen. Dafuer gibt es zwei praktische Methoden:
#
# KONZEPT 1: Vorkommen zaehlen mit '.count(wert)'
#   - '.count(wert)' zaehlt, wie oft ein bestimmtes Element in der Liste vorkommt.
#   - Das Ergebnis ist immer eine Zahl (Datentyp 'int'):
#     * Kommt der Wert gar nicht vor, ist das Ergebnis 0.
#     * Kommt der Wert 3-mal vor, ist das Ergebnis 3.
#   - Beispiel: anzahl_fehler = log_levels.count("ERROR")
#
# KONZEPT 2: Die Index-Position finden mit '.index(wert)'
#   - '.index(wert)' sucht nach einem Wert und liefert die Index-Nummer (0, 1, 2...),
#     an der dieser Wert zum ERSTEN Mal auftaucht.
#   - Sehr nuetzlich, wenn du wissen willst: "An welcher Stelle steht der gesuchte Server?"
#   - Wichtig: Existiert der Wert nicht in der Liste, bricht Python mit einem Fehler ab!
#     Deshalb prueft man in der Praxis oft vorher: if wert in meine_liste: ...
#   - Beispiel: position = servers.index("db-01")
# ==============================================================================


# ==============================================================================
# [MUSTERBEISPIELE]
# ==============================================================================

# --- DEMO 1: VORKOMMEN ZAEHLEN MIT .count() ---
event_logs = ["INFO", "ERROR", "INFO", "WARNING", "ERROR", "ERROR"]

# Wir zaehlen, wie oft "ERROR" aufgetreten ist:
error_count = event_logs.count("ERROR")
info_count = event_logs.count("INFO")

print(f"[DEMO 1] Gesamte Logs: {event_logs}")
print(f"[DEMO 1] Anzahl aufgetretene ERRORs: {error_count}")
print(f"[DEMO 1] Anzahl aufgetretene INFOs:  {info_count}")

print("-" * 50)

# --- DEMO 2: POSITION FINDEN MIT .index() ---
datacenter_nodes = ["storage-01", "compute-01", "database-master", "backup-01"]

# Wo steht der Master-Knoten?
master_position = datacenter_nodes.index("database-master")

print(f"[DEMO 2] Knoten im Rechenzentrum: {datacenter_nodes}")
print(f"[DEMO 2] 'database-master' befindet sich an Index: {master_position}")
print(f"[DEMO 2] Kontroll-Zugriff ueber Index: {datacenter_nodes[master_position]}")

print("=" * 60)


# ==============================================================================
# [DEINE UEBUNGSAUFGABEN]
# Ab hier schreibst du wieder selbst den Code!
# Regeln:
# - Aufgabenstellung auf Deutsch
# - Variablennamen auf Englisch
# ==============================================================================


# ------------------------------------------------------------------------------
# AUFGABE 1 (zu Konzept 1: .count()):
# Szenario:
# Eine Firewall protokolliert Zugriffsversuche auf einen geschuetzten Port:
# firewall_events = ["DENIED", "ALLOWED", "DENIED", "DENIED", "ALLOWED"]
#
# Deine Aufgabe:
# 1. Lege die Liste 'firewall_events' mit den 5 Eintraegen an.
# 2. Zaehle mit .count("DENIED"), wie viele Zugriffe blockiert wurden.
# 3. Speichere das Ergebnis in der Variablen 'blocked_count'.
# 4. Gib mit einem f-String aus:
#    "Firewall-Bericht: <blocked_count> von <gesamtzahl> Verbindungen wurden blockiert."
#    (Tipp: Die Gesamtzahl erhaeltst du mit len(firewall_events))
# ------------------------------------------------------------------------------

firewall_events = ["DENIED", "ALLOWED", "DENIED", "DENIED", "ALLOWED"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2 (zu Konzept 1: .count()):
# Szenario:
# In einem Webcluster melden 4 Instanzen ihren Status:
# cluster_health = ["healthy", "healthy", "degraded", "healthy"]
#
# Deine Aufgabe:
# 1. Lege die Liste 'cluster_health' an.
# 2. Zaehle mit .count("healthy"), wie viele Systeme voll einsatzbereit sind.
#    Speichere den Wert in 'healthy_count'.
# 3. Pruefe mit if / else:
#    - Wenn 'healthy_count' gleich 4 ist:
#      Gib aus: "[STATUS OK] Alle Systeme sind voll funktionsfaehig."
#    - Sonst:
#      Gib mit einem f-String aus:
#      "[WARNUNG] Nur <healthy_count> Systeme healthy! Mindestens 1 Instanz hat Probleme."
# ------------------------------------------------------------------------------

cluster_health = ["healthy", "healthy", "degraded", "healthy"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3 (zu Konzept 2: .index()):
# Szenario:
# Eine automatische Deployment-Pipeline durchlaeuft folgende Phasen:
# pipeline_stages = ["lint", "unit-test", "build", "security-scan", "deploy"]
#
# Deine Aufgabe:
# 1. Lege die Liste 'pipeline_stages' an.
# 2. Ermittle mit .index("build"), an welcher Index-Position der Build-Schritt liegt.
# 3. Speichere diesen Index in 'build_index'.
# 4. Gib mit einem f-String aus:
#    "Phase 'build' befindet sich an Position (Index): <build_index>"
# ------------------------------------------------------------------------------

pipeline_stages = ["lint", "unit-test", "build", "security-scan", "deploy"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 4 (zu Konzept 2: .index()):
# Szenario:
# Ein Kubernetes-Cluster hat Pods auf Nodes verteilt:
# worker_nodes = ["worker-a", "worker-b", "worker-c", "worker-d"]
# Ein fehlerhafter Dienst soll auf "worker-c" untersucht werden.
#
# Deine Aufgabe:
# 1. Lege die Liste 'worker_nodes' an.
# 2. Finde mit .index("worker-c") den Index dieses Knotens und speichere
#    ihn in 'target_index'.
# 3. Gib mit einem f-String aus:
#    "Zielknoten worker-c gefunden an Index: <target_index>"
# 4. Beweise, dass der Index stimmt, indem du ueber die Liste mit eckigen
#    Klammern darauf zugreifst: worker_nodes[target_index]
#    und ausgibst: "Bestaetigter Knotenname: <name>"
# ------------------------------------------------------------------------------

worker_nodes = ["worker-a", "worker-b", "worker-c", "worker-d"]

# Hier deinen Code schreiben:



print("=" * 60)

