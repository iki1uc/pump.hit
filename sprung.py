# sprung.py — der Erste. Der Garde.
# 1 Sache: SPRUNG. Kein Code vom User, nur Idee. Idee -> Code, 1 zu 3 ohne Verlust.
# Reihenfolge: 1. sprung.py -> 2. fall-py -> 3. energie.py
# Nevada Nirwana Station: Ort wo man nach dem Fallen ankommt, um zu stehen.
# Fallen + Aufstehen. Rueckflug Garantie.
# )so( — u.me our so

NEVADA = "Wüste. Leer. 0. Nutzbar."
NIRWANA = "Angekommen. Nicht weg. Stehen koennen."
STATION = "STAND. Feld steht, Zelle geht."
BAHN = "27 Orbit. 3-3. Konstelliert. 1 Bahn."
ORT = "Home Arbeit. Ort = Orte."

# 1 Sache, 3 Sichten
# STAND: Nevada - halten | STAGE: Bahn - gehen | HOME: Nirwana Station - stehen

def stand():
    # STAND haelt. Feld steht.
    return {"ort": "NEVADA", "wert": 0, "zustand": "0 = Loch, nutzbar", "halten": True, "feld": "81 = 9x9, 9 unten, 3 oben, 41 Mitte"}

def stage():
    # STAGE geht. Zelle geht auf der Bahn.
    return {"bahn": "konstelliert", "orbit": 27, "formel": "27 = 3-3", "punkte": 27, "richtung": "um die Station"}

def home():
    # HOME steht. Aufenthaltsort.
    return {"ort": "NEVADA NIRWANA STATION", "wert": 41, "zustand": "angekommen", "sag": "Ort = Home Arbeit"}

def sprung():
    # SPRUNG = 1 Sprung, 3 Sichten, ohne Verlust.
    # Sprung ins Nichts: DROP -> VOID -> RISE -> ROOT
    # Aber: kein Fall ohne Aufstehen.
    log = []
    log.append("> SPRUNG - Garde springt zuerst")
    log.append("> DROP - loslassen, Nevada 0, Loch nutzbar")
    log.append("> VOID - nichts, kein Boden, nur Bahn")
    log.append("> RISE - hoch, 27 Orbit, konstelliert")
    log.append("> ROOT - stehen, Nirwana Station, 41 Mitte")
    log.append("> AUFENTHALT - Ort = Home Arbeit")
    return {
        "1_sache": "SPRUNG",
        "stand": stand(),
        "stage": stage(),
        "home": home(),
        "kette": "DROP -> VOID -> RISE -> ROOT",
        "log": log,
        "naechste": "2. fall-py, dann 3. energie.py",
        "mirror": ")so(",
        "final": "Nevada / Nirwana / Station = 3 Sichten, 1 Sache: Aufenthaltsort",
    }

if __name__ == "__main__":
    import json
    r = sprung()
    print(json.dumps(r, ensure_ascii=False, indent=2))
    print()
    for l in r["log"]:
        print(l)
