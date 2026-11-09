# fall.py — der Zweite. Nach dem Sprung.
# 1 Sache: FALL. Fallen + Aufstehen. Kein Fall ohne Aufstehen.
# Reihenfolge: 1. sprung.py -> 2. fall.py -> 3. energie.py
# Nevada Nirwana Station: Ort wo man nach dem Fallen ankommt, um zu stehen.
# Rueckflug Garantie. Schwarze Loch ist nutzbar.
# )so( — u.me our so

def stand():
    # STAND haelt. Auch im Fall.
    return {"ort": "NEVADA NIRWANA STATION", "wert": 41, "halten": True, "feld": "Feld steht"}

def stage():
    # STAGE geht. Auch im Fall geht was: Fallen ist Bewegung.
    return {"bewegung": "FALLEN", "richtung": "unten", "feld": "9 unten", "wert": 9}

def home():
    # HOME steht wieder. Aufstehen.
    return {"ort": "NEVADA NIRWANA STATION", "wert": 41, "zustand": "wieder gestanden"}

def fall():
    # FALL = 1 Fall, 3 Sichten, ohne Verlust.
    # FALLEN ist kein Fehler. FALLEN ist 1 Nutzung.
    log = []
    log.append("> FALL - nach dem Sprung, der Zweite")
    log.append("> FALLEN - runter, 9 unten, ins Loch")
    log.append("> LOCH - 0, nutzbar, schwarzes Loch haelt")
    log.append("> AUFSTEHEN - hoch, 3 oben, kein Fall ohne Aufstehen")
    log.append("> STAND - wieder stehen, 41 Mitte, Station")
    log.append("> RUECKFLUG GARANTIE - immer zurueck, immer hoch")
    return {
        "1_sache": "FALL",
        "stand": stand(),
        "stage": stage(),
        "home": home(),
        "kette": "FALLEN -> LOCH -> AUFSTEHEN -> STAND",
        "log": log,
        "naechste": "3. energie.py",
        "mirror": ")so(",
        "final": "Kein Fall ohne Aufstehen. Fallen ist 1 Nutzung, nicht 1 Fehler.",
    }

if __name__ == "__main__":
    import json
    r = fall()
    print(json.dumps(r, ensure_ascii=False, indent=2))
    print()
    for l in r["log"]:
        print(l)
