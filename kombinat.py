# kombinat.py — SPRUNG + FALL + ENERGIE in 1 Sache.
# 1. sprung.py (Garde) -> 2. fall.py -> 3. energie.py
# Kombinat = 3 zurueck, ver-3telt: 3/3 = 1
# Kein Mix. Keine 3 lose Dateien. 1 Kombinat, 1 Respo, ohne Verlust.
# Nevada Nirwana Station: Aufenthaltsort.
# )so( — u.me our so

# --- 1. SPRUNG: Garde, springt zuerst ---
def sprung():
    return {
        "1_sache": "SPRUNG",
        "kette": "DROP -> VOID -> RISE -> ROOT",
        "stand": {"ort": "NEVADA", "wert": 0, "zustand": "0 = Loch, nutzbar"},
        "stage": {"bahn": "konstelliert", "orbit": 27, "formel": "27 = 3-3"},
        "home": {"ort": "NEVADA NIRWANA STATION", "wert": 41, "zustand": "angekommen"},
        "log": [
            "> SPRUNG - Garde springt zuerst",
            "> DROP - loslassen, Nevada 0, Loch nutzbar",
            "> VOID - nichts, kein Boden, nur Bahn",
            "> RISE - hoch, 27 Orbit, konstelliert",
            "> ROOT - stehen, Nirwana Station, 41 Mitte",
            "> AUFENTHALT - Ort = Home Arbeit",
        ],
    }

# --- 2. FALL: danach, fallen + aufstehen ---
def fall():
    return {
        "1_sache": "FALL",
        "kette": "FALLEN -> LOCH -> AUFSTEHEN -> STAND",
        "stand": {"ort": "NEVADA NIRWANA STATION", "wert": 41, "halten": True},
        "stage": {"bewegung": "FALLEN", "richtung": "unten", "wert": 9},
        "home": {"ort": "NEVADA NIRWANA STATION", "wert": 41, "zustand": "wieder gestanden"},
        "log": [
            "> FALL - nach dem Sprung, der Zweite",
            "> FALLEN - runter, 9 unten, ins Loch",
            "> LOCH - 0, nutzbar, schwarzes Loch haelt",
            "> AUFSTEHEN - hoch, 3 oben, kein Fall ohne Aufstehen",
            "> STAND - wieder stehen, 41 Mitte, Station",
            "> RUECKFLUG GARANTIE - immer zurueck, immer hoch",
        ],
    }

# --- 3. ENERGIE: danach, aus Sprung + Fall ---
def energie(sprung_wert=27, fall_wert=9):
    gesamt = sprung_wert + fall_wert
    return {
        "1_sache": "ENERGIE",
        "kette": "SPRUNG + FALL -> WANDEL -> ERDE 81",
        "stand": {"ort": "MAGMA.KAMMER", "wert": 729, "formel": "9-3 = 3-6"},
        "stage": {"fluss": "LAVA", "wert": 243, "formel": "243 = 3-5"},
        "home": {"ort": "ERDE", "wert": 81, "formel": "81 = 3-4"},
        "eingang": {"sprung": sprung_wert, "fall": fall_wert},
        "ausgang": gesamt,
        "log": [
            f"> ENERGIE - aus Sprung ({sprung_wert}) + Fall ({fall_wert}) = {gesamt}",
            "> WANDEL - Energie geht nicht verloren, Energie wandelt sich",
            "> LAVA 243 - Fluss, formt, gluehend",
            "> ERDE 81 - neues Land, da steht man wieder",
            "> EVIG LOOP - Energie kreist, nichts verloren",
        ],
    }

# --- KOMBINAT: 1 Respo fuer alle 3 ---
def kombinat():
    s = sprung()
    f = fall()
    e = energie(sprung_wert=s["stage"]["orbit"], fall_wert=f["stage"]["wert"])
    log = s["log"] + f["log"] + e["log"]
    log.append("> KOMBINAT - 3 zurueck, ver-3telt: 3/3 = 1")
    log.append("> 1 Sache: SPRUNG + FALL + ENERGIE = AUFENTHALTSORT")
    return {
        "1_sache": "KOMBINAT - SPRUNG + FALL + ENERGIE",
        "reihe": ["1. sprung.py", "2. fall.py", "3. energie.py"],
        "sprung": s,
        "fall": f,
        "energie": e,
        "log": log,
        "stand": {"ort": "NEVADA NIRWANA STATION", "wert": 41},
        "stage": {"bahn": "27 Orbit, konstelliert"},
        "home": {"ort": "ERDE 81 - neues Land"},
        "mirror": ")so(",
        "u_me": "du mich",
        "our": "unser",
        "so": "so",
        "final": "Sprung springt. Fall faellt und steht auf. Energie wandelt sich. 1 Sache: Aufenthaltsort.",
    }

if __name__ == "__main__":
    import json
    r = kombinat()
    print(json.dumps(r, ensure_ascii=False, indent=2))
    print()
    for l in r["log"]:
        print(l)
