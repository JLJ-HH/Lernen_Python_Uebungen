# ==============================================================================
# Modul 1.2 - Vertiefung: Bedingungen & Verzweigungen (Runde 2)
# Datei: C:\Lernen_Python\01_grundlagen\bedingungen\02_vertiefung_fstrings.py
# ==============================================================================
# WICHTIGE ERKENNTNIS ZU PRINT-TEXTEN:
# Alles, was innerhalb von print("...") steht, ist DEINE freie Entscheidung!
# Das '[STATUS]' oder der Pfeil '->' aus den vorherigen Beispielen sind KEINE
# Vorschriften von Python, sondern nur menschliche Deko fuer die Konsole.
#
# Du kannst beliebige Texte schreiben – und natuerlich darfst du auch im
# if-Block jederzeit f-Strings benutzen, um Werte einzubinden!
# Beispiel:
# if temp > 80.0:
#     print(f"Achtung, die Temperatur {temp} Grad ist zu hoch!")
# ==============================================================================


# ------------------------------------------------------------------------------
# AUFGABE 1: Download-Status pruefen (if / else)
# Szenario: Ein Software-Update wird heruntergeladen. Der aktuelle Fortschritt
# liegt bei 100 Prozent ('fortschritt = 100').
#
# 1. Schreibe ein if / else:
#    - WENN 'fortschritt == 100' ist:
#      Gib eine Erfolgsmeldung aus (z. B. dass der Download abgeschlossen ist).
#    - SONST (else):
#      Gib eine Meldung mit f-String aus, wie viel Prozent noch geladen werden
#      (z. B. "Download laeuft noch: X% erledigt").
# ------------------------------------------------------------------------------

fortschritt = 90

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2: KI-Konfidenz (Vertrauenswert) bewerten (if / elif / else)
# Szenario: Ein Bilderkennungs-Modell erkennt ein Objekt mit einer Konfidenz
# von 0.78 ('confidence = 0.78', Werte gehen von 0.0 bis 1.0).
#
# 1. Bewerte die Sicherheit des Modells in 3 Stufen mit if / elif / else:
#    - WENN 'confidence >= 0.90':
#      Gib aus, dass das Ergebnis sehr sicher / hoch verlaesslich ist.
#    - ODER WENN (elif) 'confidence >= 0.70':
#      Gib aus, dass das Ergebnis annehmbar / mittlere Sicherheit ist.
#    - SONST (else):
#      Gib aus, dass das Modell unsicher ist und ein Mensch pruefen muss.
# ------------------------------------------------------------------------------

confidence = 0.68

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3: Bot-Kommando erkennen (Text-Vergleich mit ==)
# Szenario: Ein Chatbot empfaengt ein Steuerkommando 'kommando = "stop"'.
#
# 1. Reagiere mit if / elif / else auf das Kommando:
#    - WENN 'kommando == "start"':
#      Gib aus, dass der Bot seine Arbeit aufnimmt.
#    - ODER WENN 'kommando == "stop"':
#      Gib aus, dass der Bot angehalten wurde.
#    - SONST (else):
#      Gib mit einem f-String aus, dass dieses Kommando unbekannt ist
#      (z. B. f"Unbekannter Befehl: '{kommando}'").
# ------------------------------------------------------------------------------

kommando = "start"

# Hier deinen Code schreiben:



print("=" * 60)

