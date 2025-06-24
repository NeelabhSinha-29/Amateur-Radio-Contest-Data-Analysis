from extract_callsigns import callsigns_list

all_callsigns = callsigns_list()
count = 0
for callsign in all_callsigns:
    if "/" in callsign:
        callsign = callsign.replace("/", "_")
    with open(f"./Data/Raw/2024 CQ WW CW Contest/{callsign}.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        QSO_lines = [line.strip() for line in lines if line.startswith("QSO") == True]
        count += len(QSO_lines)
print(count)


