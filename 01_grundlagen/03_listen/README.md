# Modul 1.3: Listen (Lists)

## 📌 Zweck dieses Ordners
Dieser Ordner behandelt **Listen (`list`)** – die flexibelste und am häufigsten genutzte Datenstruktur in Python, um Sammlungen von Elementen geordnet zu speichern.

Didaktischer Aufbau: Jede Datei behandelt **maximal zwei zusammengehörige Kernkonzepte** mit jeweils **1 direktem Musterbeispiel + 2 Übungsaufgaben** (insgesamt 4 Aufgaben pro Datei).

---

## 📂 Dateien & Inhalte

### 1. `01_grundlagen_index.py` (Grundlagen & Indizierung)
- **Konzepte:**
  - Listen erstellen mit eckigen Klammern: `["a", "b", "c"]`
  - Zero-based Indexing (Erstes Element: `[0]`, Letztes Element: `[-1]`)
  - Schnelleinstieg & erste Gehversuche

### 2. `02_update_in.py` (Werte ändern & Vorhandensein prüfen)
- **Konzepte:**
  - Konzept 1: Element an bestimmtem Index überschreiben (`liste[0] = "neu"`)
  - Konzept 2: Vorhandensein prüfen mit `if "wert" in liste:` (und `else`)

### 3. `03_remove_pop.py` (Elemente entfernen: `.remove()` & `.pop()`)
- **Konzepte:**
  - Konzept 1: Gezielt nach Wert löschen mit `.remove("wert")`
  - Konzept 2: Letztes Element entnehmen und verwerten mit `.pop()`

### 4. `04_sort_reverse.py` (Sortieren & Reihenfolge: `.sort()` & `.reverse()`)
- **Konzepte:**
  - Konzept 1: Aufsteigend / alphabetisch sortieren mit `.sort()`
  - Konzept 2: Reihenfolge komplett umdrehen mit `.reverse()` (z. B. für Rollbacks & Leaderboards)

### 5. `05_len_append.py` (Länge messen & Erweitern: `len()` & `.append()`)
- **Konzepte:**
  - Konzept 1: Reale Elementanzahl ermitteln mit `len()` (Datentyp `int`)
  - Konzept 2: Neue Elemente ans Ende anfügen mit `.append()` (in-place)

### 6. `06_count_index.py` (Vorkommen zählen & Position finden)
- **Konzepte:**
  - Konzept 1: Vorkommen zählen mit `.count(wert)` (Datentyp `int`)
  - Konzept 2: Index-Position eines Elements ermitteln mit `.index(wert)`

### 7. `07_slicing.py` (Teillisten herausschneiden: Slicing)
- **Konzepte:**
  - Konzept 1: Standard-Slicing mit Start, Stop und Schritt (`liste[start:stop]`, `liste[:3]`, `liste[2:]`)
  - Konzept 2: Fortgeschrittenes Slicing mit negativen Indizes & Umkehren (`liste[-3:]`, `liste[::-1]`)

### 8. `08_praxis_mix.py` (Praxis-Mix: Alle Methoden im Zusammenspiel)
- **Konzepte:**
  - Kombination aller Methoden im praktischen Sysadmin/DevOps-Alltag
  - Redundanz-Prüfung (`len(...) >= 3`) mit Differenzberechnung & Auto-Recovery (`.append()`)
  - Sichere Administration (`in` vor `.remove()`)
  - Queue-Bearbeitung (`.pop()`), Spam-Schutz (`.count()`), Audit & Slicing (`.sort()`, `[-3:]`)
