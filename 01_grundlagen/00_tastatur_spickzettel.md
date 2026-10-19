# Tastatur-Spickzettel fuer Python-Einsteiger

Dieser Spickzettel ist in zwei getrennte Abschnitte unterteilt:  
Erst komplett **Windows**, danach komplett **Linux**. So kannst du dich genau auf dein Betriebssystem konzentrieren!

================================================================================
# TEIL 1: WINDOWS
================================================================================

Auf einer deutschen Windows-Tastatur (QWERTZ) erreichst du fast alle Programmier-Zeichen mit der Taste **`Alt Gr`** (rechts neben der Leertaste).

### Windows: Alle wichtigen Zeichen im Ueberblick

| Zeichen | Name | So drueckst du es unter Windows | Wofuer in Python? |
| :---: | :--- | :--- | :--- |
| **`{ }`** | **Geschweifte Klammern** | **`Alt Gr` + `7`** (auf) <br> **`Alt Gr` + `0`** (zu) | **f-Strings:** `{variable}` <br> Später: Dictionaries |
| **`[ ]`** | **Eckige Klammern** | **`Alt Gr` + `8`** (auf) <br> **`Alt Gr` + `9`** (zu) | **Listen:** `["Apfel", "Banane"]` |
| **`( )`** | **Runde Klammern** | **`Shift` + `8`** (auf) <br> **`Shift` + `9`** (zu) | **Funktionen:** `print()`, `type()`, `int()` |
| **`\|`** | **Trennstrich (Pipe)** | **`Alt Gr` + `<`** (Taste links neben Y) | Trennungen in Texten oder logisches ODER |
| **`\`** | **Backslash** | **`Alt Gr` + `ß`** (Taste neben 0) | Zeilenumbrueche (`\n`) |
| **`"`** | **Doppelte Anfuehrungszeichen** | **`Shift` + `2`** | Strings / Texte (`"Hallo"`) |
| **`'`** | **Einfaches Anfuehrungszeichen** | **`Shift` + `#`** (Taste links neben Enter) | Alternative fuer Strings (`'Hallo'`) |
| **`=`** | **Gleichheitszeichen** | **`Shift` + `0`** | Wert zuweisen (`x = 10`) |
| **`==`** | **Doppeltes Gleich** | Zweimal **`Shift` + `0`** | Vergleich: Ist x gleich y? |
| **`_`** | **Unterstrich (Underscore)** | **`Shift` + `-`** (neben rechter Shift-Taste) | Variablennamen (`auto_marke`) |
| **`#`** | **Raute (Hashtag)** | Taste **`#`** (links neben Enter) | Kommentare (Notizen fuer dich) |

### Windows-Merkhilfe: Die Tastenreihe 7 bis 0
Halte **`Alt Gr`** gedrueckt und gehe die Zahlen von links nach rechts durch:
- **`7`** -> **`{`** (geschweift auf)
- **`8`** -> **`[`** (eckig auf)
- **`9`** -> **`]`** (eckig zu)
- **`0`** -> **`}`** (geschweift zu)

---
<br><br><br>

================================================================================
# TEIL 2: LINUX (Ubuntu, Debian, Mint etc.)
================================================================================

Unter Linux hast du zwei Bereiche: 
1. Wie du die **Zeichen im Code-Editor** tippst
2. Wie du im **Linux-Terminal** arbeitest

### Warum sind die Zeichen-Tasten unter Linux gleich?
Wenn du eine deutsche Tastatur angeschlossen hast, nutzt Linux das gleiche deutsche Tastaturlayout (QWERTZ). Die Tasten mit **`Alt Gr`** liegen an exakt derselben Stelle wie bei Windows.

### Linux: Zeichen im Code-Editor (z. B. VS Code / PyCharm)

| Zeichen | Name | So drueckst du es unter Linux | Wofuer in Python? |
| :---: | :--- | :--- | :--- |
| **`{ }`** | **Geschweifte Klammern** | **`Alt Gr` + `7`** (auf) <br> **`Alt Gr` + `0`** (zu) | **f-Strings:** `{variable}` |
| **`[ ]`** | **Eckige Klammern** | **`Alt Gr` + `8`** (auf) <br> **`Alt Gr` + `9`** (zu) | **Listen:** `["A", "B"]` |
| **`( )`** | **Runde Klammern** | **`Shift` + `8`** (auf) <br> **`Shift` + `9`** (zu) | **Funktionen:** `print()` |
| **`\|`** | **Trennstrich (Pipe)** | **`Alt Gr` + `<`** (Taste links neben Y) | Texttrenner / Oder |
| **`\`** | **Backslash** | **`Alt Gr` + `ß`** (Taste neben 0) | Zeilenumbrueche (`\n`) |
| **`"`** | **Doppelte Anfuehrungszeichen** | **`Shift` + `2`** | Strings / Texte (`"Hallo"`) |
| **`'`** | **Einfaches Anfuehrungszeichen** | **`Shift` + `#`** (Taste links neben Enter) | Alternative Strings (`'Hallo'`) |
| **`=`** | **Gleichheitszeichen** | **`Shift` + `0`** | Zuweisung (`x = 10`) |
| **`_`** | **Unterstrich** | **`Shift` + `-`** | Variablennamen (`mein_wert`) |
| **`#`** | **Raute** | Taste **`#`** (links neben Enter) | Kommentare |

### Das Linux-Terminal (Die wichtigsten Unterschiede zu Windows)

Im Linux-Terminal funktionieren normale Tastenkombinationen wie `Strg + C` anders als gewohnt. Hier sind die wichtigsten Terminal-Shortcuts:

| Aktion | Tastenkombination Linux-Terminal | Warum ist das so? |
| :--- | :--- | :--- |
| **Laufendes Skript abbrechen** | **`Strg` + `C`** | Bricht dein Python-Programm sofort ab (Not-Aus). |
| **Text kopieren** | **`Strg` + `Umschalt` + `C`** | Da `Strg + C` schon fuer "Abbrechen" reserviert ist, braucht man zusaetzlich `Umschalt`! |
| **Text einfuegen** | **`Strg` + `Umschalt` + `V`** | Fuegt kopierten Text in das Terminal ein. |
| **Terminal leeren** | **`Strg` + `L`** | Macht den Terminal-Bildschirm wieder frei und sauber (wie `clear`). |
| **Letzten Befehl aufrufen** | Pfeiltaste **`Hoch ^`** | Spart Tipparbeit beim erneuten Ausfuehren deines Skripts. |
