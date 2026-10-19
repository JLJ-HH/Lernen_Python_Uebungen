# ==============================================================================
# Modul 1.3: Listen (Lists) - Teil 7: Teillisten herausschneiden (Slicing)
# Datei: C:\Lernen_Python\01_grundlagen\listen\07_slicing.py
# ==============================================================================

# [THEORIE: WAS IST SLICING UND WIE FUNKTIONIERT ES?]
# Manchmal braucht man nicht nur ein einzelnes Element (z. B. liste[0]),
# sondern einen ganzen Ausschnitt (eine "Scheibe" = Slice) einer Liste.
#
# SYNTAX:
#   teilliste = liste[start : stop : schritt]
#
# WICHTIG:
#   - 'start': Der Index, an dem der Ausschnitt BEGINNT (inklusive).
#   - 'stop':  Der Index, an dem der Ausschnitt ENDET (EXKLUSIVE! Bis vor diesen Index).
#   - 'schritt' (optional): In welchen Spruengen gegangen wird (Standard: 1).
#   - Slicing veraendert die Original-Liste NICHT! Es entsteht eine neue Teilliste.
#
# DIE WICHTIGSTEN MUSTER:
# 1. Start bis Stop:
#    liste[1:4]     -> Elemente von Index 1 bis vor Index 4 (also Index 1, 2, 3).
#
# 2. Vom Anfang bis X (Start weglassen):
#    liste[:3]      -> Vom Anfang bis vor Index 3 (die ersten 3 Elemente).
#
# 3. Von X bis zum Ende (Stop weglassen):
#    liste[2:]      -> Ab Index 2 bis ganz zum Ende der Liste.
#
# 4. Negative Indizes (von hinten zaehlen):
#    liste[-3:]     -> Die letzten 3 Elemente bis zum Ende!
#    liste[:-2]     -> Vom Anfang bis vor die letzten 2 Elemente (alles ausser den letzten 2).
#
# 5. Schrittweite & Umkehren:
#    liste[::2]     -> Jedes 2. Element der Liste (Schrittweite 2).
#    liste[::-1]    -> Die gesamte Liste rueckwaerts kopieren (ohne das Original zu aendern!).
# ==============================================================================


# ==============================================================================
# [MUSTERBEISPIELE]
# ==============================================================================

servers = ["web-01", "web-02", "web-03", "db-01", "db-02", "cache-01"]

# --- DEMO 1: TEILLISTEN MIT START UND STOP ---
# Wir wollen nur die ersten 3 Server (die Webserver an Index 0, 1, 2):
web_cluster = servers[:3]

# Wir wollen die mittleren beiden (die Datenbanken an Index 3 und 4):
db_cluster = servers[3:5]

print(f"[DEMO 1] Alle Server:      {servers}")
print(f"[DEMO 1] Web-Cluster:      {web_cluster}")
print(f"[DEMO 1] DB-Cluster:       {db_cluster}")

print("-" * 50)

# --- DEMO 2: NEGATIVE INDIZES UND RUECKWAERTS-SLICING ---
# Die letzten 2 Server (Cache und letzte DB):
trailing_nodes = servers[-2:]

# Die gesamte Liste umgedreht (ohne Original zu mutieren):
reversed_nodes = servers[::-1]

print(f"[DEMO 2] Letzte 2 Knoten:  {trailing_nodes}")
print(f"[DEMO 2] Rueckwaerts-Kopie: {reversed_nodes}")
print(f"[DEMO 2] Original-Liste:   {servers} (bleibt unveraendert!)")

print("=" * 60)


# ==============================================================================
# [DEINE UEBUNGSAUFGABEN]
# Ab hier schreibst du wieder selbst den Code!
# Regeln:
# - Aufgabenstellung auf Deutsch
# - Variablennamen auf Englisch
# ==============================================================================


# ------------------------------------------------------------------------------
# AUFGABE 1 (Gefuehrt: Start und Stop verwenden):
# Szenario:
# Ein Backup-System hat fuer eine Arbeitswoche taeglich Archive angelegt:
# backup_files = ["mon_full.bak", "tue_diff.bak", "wed_diff.bak", "thu_diff.bak", "fri_diff.bak"]
#
# Deine Aufgabe:
# 1. Lege die Liste 'backup_files' mit den 5 Dateinamen an.
# 2. Schneide mit Slicing die ersten 3 Backups heraus (Montag bis Mittwoch).
#    Speichere das Ergebnis in der Variablen 'early_backups'. (Tipp: backup_files[:3])
# 3. Schneide mit Slicing den mittleren Teil heraus: Dienstag bis Donnerstag (Index 1 bis vor 4).
#    Speichere das Ergebnis in 'midweek_backups'. (Tipp: backup_files[1:4])
# 4. Gib beide Teillisten jeweils mit print() aus.
# ------------------------------------------------------------------------------

# DEIN CODE HIER:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 2 (Gefuehrt: Negative Indizes nutzen):
# Szenario:
# Ein Monitoring-Agent hat stuendliche CPU-Auslastungswerte gesammelt:
# cpu_metrics = [15, 22, 19, 45, 68, 85, 91, 94]
#
# Deine Aufgabe:
# 1. Lege die Liste 'cpu_metrics' an.
# 2. Extrahiere mit negativem Slicing die letzten 3 Messwerte (die aktuellsten).
#    Speichere sie in 'recent_metrics'. (Tipp: cpu_metrics[-3:])
# 3. Extrahiere alle Werte ausser den letzten 2 (also die Baseline vom Tagesbeginn).
#    Speichere sie in 'baseline_metrics'. (Tipp: cpu_metrics[:-2])
# 4. Gib 'recent_metrics' und 'baseline_metrics' mit print() aus.
# ------------------------------------------------------------------------------

# DEIN CODE HIER:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 3 (Freier / Mitdenken: Schichtplan-Analyse):
# Szenario:
# Ein Dispatcher erfasst 8 Vorfaelle ueber einen Arbeitstag hinweg:
# incidents = ["LOGIN_FAIL", "OK", "OK", "DISK_FULL", "TIMEOUT", "OK", "TIMEOUT", "CRASH"]
# Die ersten 4 Vorfaelle (Index 0 bis 3) fielen in Schicht A.
# Die restlichen 4 Vorfaelle (ab Index 4 bis zum Ende) fielen in Schicht B.
#
# Deine Aufgabe:
# 1. Lege die Liste 'incidents' an.
# 2. Erstelle zwei Teillisten per Slicing:
#    - 'shift_a_incidents' fuer die Vorfaelle von Schicht A
#    - 'shift_b_incidents' fuer die Vorfaelle von Schicht B
# 3. Pruefe mit einer if/else-Bedingung:
#    - Wenn "CRASH" in 'shift_b_incidents' enthalten ist:
#      Gib aus: "[ALARM] Schwerwiegender Systemabsturz in Schicht B festgestellt!"
#    - Andernfalls:
#      Gib aus: "[OK] Keine Abstuerze in Schicht B."
# 4. Gib zusaetzlich beide Listen aus.
# ------------------------------------------------------------------------------

# DEIN CODE HIER:



print("-" * 60)

# ------------------------------------------------------------------------------
# AUFGABE 4 (Freier / Mitdenken: Revisions-Audit & Rollback-Kette):
# Szenario:
# Ein Deployment-Tool haelt die Historie der letzten Deployments:
# deployments = ["v1.0.0", "v1.0.1", "v1.1.0", "v1.2.0", "v2.0.0", "v2.1.0"]
#
# Deine Aufgabe:
# 1. Lege die Liste 'deployments' an.
# 2. Stichproben-Audit:
#    Fuer eine Routinepruefung soll jedes zweite Deployment ab Beginn ueberprueft werden
#    (also Schrittweite 2: Index 0, 2, 4...).
#    Erstelle diese Teilliste mit Schrittweiten-Slicing und speichere sie in 'audit_sample'.
# 3. Rollback-Kette:
#    Fuer einen eventuellen Notfall-Rollback brauchst du die letzten 3 Deployments,
#    aber in umgekehrter Reihenfolge (das allerneueste zuerst, damit man rueckwaerts abrollen kann).
#    Erstelle diese Teilliste und speichere sie in 'rollback_chain'.
#    (Hinweis: Du kannst z. B. zuerst die letzten 3 mit [-3:] herausschneiden und dann umkehren,
#     oder in einem Schritt mit Slicing arbeiten).
# 4. Gib 'audit_sample' und 'rollback_chain' sauber formatiert auf der Konsole aus.
# ------------------------------------------------------------------------------

# DEIN CODE HIER:



print("=" * 60)
