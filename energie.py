# energie.py — der Dritte. Nach Sprung + Fall.
# 1 Sache: ENERGIE. Energie kommt aus Sprung + Fall.
# Reihenfolge: 1. sprung.py -> 2. fall.py -> 3. energie.py
# Energie ist nicht weg, Energie ist gewandelt.
# Nevada Nirwana Station: Ort wo Energie steht, nicht verloren geht.
# )so( — u.me our so

def stand():
    # STAND haelt Energie. Kammer haelt.
    return {"ort": "MAGMA.KAMMER", "wert": 729, "formel": "9-3 = 3-6", "halten": True}

def stage():
    # STAGE gibt Energie weiter. Fluss.
    return {"fluss": "LAVA", "wert": 243, "formel": "243 = 3-5", "richtung": "unten -> oben"}

def home():
    # HOME nutzt Energie. Neues Land.
    return {"ort": "ERDE", "wert": 81, "formel": "81 = 3-4", "zustand": "neues Land, da steht man wieder"}

def energie(sprung_wert=27, fall_wert=9):
    # ENERGIE = Sprung + Fall, gewandelt, nicht verloren.
    # 1 in, 100 out, aber 100 sind 1. 1 Blockade geloest = 100 geloest.
    gesamt = sprung_wert + fall_wert
    log = []
    log.append(f"> ENERGIE - aus Sprung ({sprung_wert}) + Fall ({fall_wert}) = {gesamt}")
    log.append("> WANDEL - Energie geht nicht verloren, Energie wandelt sich")
    log.append("> LAVA 243 - Fluss, formt, gluehend")
    log.append("> ERDE 81 - neues Land, da steht man wieder")
    log.append("> EVIG LOOP - Energie kreist, nichts verloren")
    return {
        "1_sache": "ENERGIE",
        "stand": stand(),
        "stage": stage(),
        "home": home(),
        "eingang": {"sprung": sprung_wert, "fall": fall_wert},
        "ausgang": gesamt,
        "wandel": "Energie geht nicht verloren, Energie wandelt sich",
        "kette": "SPRUNG + FALL -> WANDEL -> ERDE 81",
        "log": log,
        "mirror": ")so(",
        "final": "Sprung + Fall = Energie. 1 in, 100 out, aber 100 sind 1.",
    }

if __name__ == "__main__":
    import json
    r = energie()
    print(json.dumps(r, ensure_ascii=False, indent=2))
    print()
    for l in r["log"]:
        print(l)
