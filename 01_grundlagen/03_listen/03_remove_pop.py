# ==============================================================================
# Modul 1.3: Listen (Lists) - Teil 3: Elemente entfernen (.remove & .pop)
# Datei: C:\Lernen_Python\01_grundlagen\listen\03_remove_pop.py
# ==============================================================================

# [THEORIE: WIE ENTFERNT MAN ELEMENTE AUS EINER LISTE?]
# In Python gibt es zwei haeufig genutzte Wege, um etwas aus einer Liste zu loeschen:
#
# KONZEPT 1: Gezielt nach WERT loeschen mit '.remove(wert)'
#   Du weisst, WAS du loeschen willst (z. B. "apache2"), egal an welchem Index es steht.
#   Python sucht das Element von links und entfernt das erste Vorkommen.
#   Beispiel: meine_liste.remove("apache2")
#
# KONZEPT 2: Das LETZTE Element entnehmen mit '.pop()'
#   Du nimmst das letzte Element vom Stapel herunter (wie bei einer Aufgabenliste/Queue).
#   Der Clou an .pop(): Es entfernt das Element UND gibt es zurueck, sodass du es
#   in einer Variablen speichern und weiterverarbeiten kannst!
#   Beispiel: erledigt = meine_liste.pop()
# ==============================================================================


# ==============================================================================
# [MUSTERBEISPIELE]
# ==============================================================================

# --- DEMO 1: GEZIELT ENTFERNEN MIT .remove() ---
packages = ["nginx", "apache2", "docker", "git"]
print(f"[DEMO 1 vor remove]  Pakete: {packages}")

# Wir deinstallieren 'apache2':
packages.remove("apache2")
print(f"[DEMO 1 nach remove] Pakete: {packages}")

print("-" * 40)

# --- DEMO 2: LETZTES ELEMENT ENTNEHMEN MIT .pop() ---
task_stack = ["backup_datenbank", "cache_leeren", "report_senden"]
print(f"[DEMO 2 vor pop]  Warteschlange: {task_stack}")

# Wir holen die letzte Aufgabe ab und speichern sie:
current_task = task_stack.pop()
print(f"[DEMO 2] Gerade bearbeitete Aufgabe: {current_task}")
print(f"[DEMO 2 nach pop] Verbleibende Warteschlange: {task_stack}")

print("=" * 60)


# ==============================================================================
# [DEINE UEBUNGSAUFGABEN]
# ==============================================================================

# ------------------------------------------------------------------------------
# AUFGABE 1 (zu Konzept 1: .remove()):
# Szenario:
# Ein Server hat installierte Dienste: ["ssh", "ftp", "http", "mysql"].
# Das alte, unsichere Protokoll "ftp" soll aus der Liste entfernt werden.
#
# Deine Aufgabe:
# 1. Erstelle die Liste: services = ["ssh", "ftp", "http", "mysql"]
# 2. Entferne "ftp" gezielt mit services.remove("ftp").
# 3. Gib mit print() die aktualisierte Liste aus.
# ------------------------------------------------------------------------------

services = ["ssh", "ftp", "http", "mysql"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2 (zu Konzept 1: .remove()):
# Szenario:
# Aus einer Mitarbeiter-Berechtigungsliste scheidet ein Mitarbeiter aus:
# staff = ["Anna", "Ben", "Clara", "David"]
# "Ben" verlaesst das Team und soll aus der Liste geloescht werden.
#
# Deine Aufgabe:
# 1. Erstelle die Liste: staff = ["Anna", "Ben", "Clara", "David"]
# 2. Entferne "Ben" mit staff.remove("Ben").
# 3. Gib mit print() die bereinigte Liste 'staff' aus.
# ------------------------------------------------------------------------------

staff = ["Anna", "Ben", "Clara", "David"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3 (zu Konzept 2: .pop()):
# Szenario:
# Ein Ticket-System enthaelt offene Support-Tickets:
# tickets = ["ticket-101", "ticket-102", "ticket-103"]
# Das neueste Ticket ("ticket-103") soll abgearbeitet werden.
#
# Deine Aufgabe:
# 1. Erstelle die Liste: tickets = ["ticket-101", "ticket-102", "ticket-103"]
# 2. Nimm mit .pop() das letzte Ticket heraus und speichere es in 'active_ticket':
#    active_ticket = tickets.pop()
# 3. Gib mit einem f-String aus: f"In Bearbeitung: {active_ticket}"
# 4. Gib mit print() die verbleibende Liste 'tickets' aus.
# ------------------------------------------------------------------------------

tickets = ["ticket-101", "ticket-102", "ticket-103"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 4 (zu Konzept 2: .pop()):
# Szenario:
# Ein History-Log speichert Rueckgaengig-Schritte (Undo):
# history = ["edit_title", "add_image", "delete_paragraph"]
# Der letzte Schritt soll rueckgaengig gemacht werden.
#
# Deine Aufgabe:
# 1. Erstelle die Liste: history = ["edit_title", "add_image", "delete_paragraph"]
# 2. Entferne die letzte Aktion mit .pop() in eine Variable:
#    undone_action = history.pop()
# 3. Gib mit f-String aus: f"Rueckgaengig gemacht: {undone_action}"
# 4. Gib die uebrig gebliebene History-Liste mit print() aus.
# ------------------------------------------------------------------------------

history = ["edit_title", "add_image", "delete_paragraph"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 5 (Praxis-Check: Gezielt nach Wert entfernen):
# Szenario:
# In einem Warenkorb liegen Produkte:
# warenkorb = ["Laptop", "Maus", "Tastatur", "Monitor"]
# Der Kunde entscheidet sich gegen die "Tastatur" und entfernt sie.
#
# Deine Aufgabe:
# 1. Erstelle die Liste: warenkorb = ["Laptop", "Maus", "Tastatur", "Monitor"]
# 2. Entferne die "Tastatur" gezielt aus der Liste.
# 3. Gib die verbleibende Liste aus.
# ------------------------------------------------------------------------------

warenkorb = ["Laptop", "Maus", "Tastatur", "Monitor"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 6 (Praxis-Check: Gezielt nach Wert entfernen):
# Szenario:
# Eine Liste enthaelt geblockte IP-Adressen:
# blacklist = ["192.168.1.15", "10.0.0.99", "172.16.0.4"]
# Die IP "10.0.0.99" wurde faelschlicherweise geblockt und soll freigegeben werden.
#
# Deine Aufgabe:
# 1. Erstelle die Liste: blacklist = ["192.168.1.15", "10.0.0.99", "172.16.0.4"]
# 2. Loesche die IP-Adresse "10.0.0.99" gezielt aus der Liste.
# 3. Gib die bereinigte Blacklist mit print() aus.
# ------------------------------------------------------------------------------

blacklist = ["192.168.1.15", "10.0.0.99", "172.16.0.4"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 7 (Praxis-Check: Letztes Element entnehmen):
# Szenario:
# Eine Druckwarteschlange hat drei Druckauftraege:
# drucker_queue = ["rechnung.pdf", "foto.png", "vertrag.docx"]
# Der zuletzt hinzugefuegte Auftrag soll sofort gedruckt und aus der Warteschlange genommen werden.
#
# Deine Aufgabe:
# 1. Erstelle die Liste: drucker_queue = ["rechnung.pdf", "foto.png", "vertrag.docx"]
# 2. Nimm den letzten Auftrag vom Ende der Liste heraus und speichere ihn in 'aktueller_druck'.
# 3. Gib auf der Konsole aus: f"Drucke jetzt: {aktueller_druck}"
# 4. Gib die restliche Warteschlange mit print() aus.
# ------------------------------------------------------------------------------

drucker_queue = ["rechnung.pdf", "foto.png", "vertrag.docx"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 8 (Praxis-Check: Letztes Element entnehmen):
# Szenario:
# Ein Notizstapel mit anstehenden Aufgaben:
# notizen = ["Einkaufen", "Rechnungen zahlen", "Arzt anrufen"]
# Du nimmst die oberste/letzte Notiz vom Stapel herunter, um sie zu bearbeiten.
#
# Deine Aufgabe:
# 1. Erstelle die Liste: notizen = ["Einkaufen", "Rechnungen zahlen", "Arzt anrufen"]
# 2. Hole das letzte Element vom Stapel herunter und speichere es in 'aktuelle_notiz'.
# 3. Gib mit f-String aus: f"Erledige jetzt: {aktuelle_notiz}"
# 4. Gib den verbleibenden Notizstapel mit print() aus.
# ------------------------------------------------------------------------------

notizen = ["Einkaufen", "Rechnungen zahlen", "Arzt anrufen"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 9 (zu Konzept 1: .remove()):
# Szenario:
# Auf einem Server sind Netzwerk-Schnittstellen aktiv:
# network_interfaces = ["eth0", "eth1", "wlan0", "docker0"]
# Das WLAN-Interface "wlan0" wird deaktiviert und soll aus der Liste entfernt werden.
#
# Deine Aufgabe:
# 1. Lege die Liste 'network_interfaces' mit den 4 Eintraegen an.
# 2. Entferne gezielt "wlan0" mit .remove().
# 3. Gib die verbleibende Liste mit print() aus.
# ------------------------------------------------------------------------------

network_interfaces = ["eth0", "eth1", "wlan0", "docker0"]

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 10 (zu Konzept 2: .pop()):
# Szenario:
# Ein Software-Stack soll nacheinander installiert werden:
# install_stack = ["git", "curl", "htop", "tmux"]
# Das oberste (letzte) Tool soll mit .pop() entnommen und installiert werden.
#
# Deine Aufgabe:
# 1. Lege die Liste 'install_stack' mit den 4 Tools an.
# 2. Entnimm das letzte Tool mit .pop() in die Variable 'current_tool'.
# 3. Gib mit einem f-String aus:
#    "Installiere jetzt: {current_tool}"
# 4. Gib mit print() die restliche Liste 'install_stack' aus.
# ------------------------------------------------------------------------------

install_stack = ["git", "curl", "htop", "tmux"]

# Hier deinen Code schreiben:



print("=" * 60)

