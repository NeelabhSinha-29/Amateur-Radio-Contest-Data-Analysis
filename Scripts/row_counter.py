from extract_callsigns import callsigns_list

def row_count(callsign):
    if "/" in callsign:
        callsign = callsign.replace("/", "_")
        #print(f"Warning! The callsign {callsign.replace("_","/")} has been renamed to {callsign} for naming purposes temporarily.")
    with open(f"./Data/Raw/2024 CQ WW CW Contest/{callsign}.txt","r", encoding="utf-8", errors="replace") as f:
        count = 0
        for line in f:
            if line.startswith("QSO"):
                count += 1
    return count

callsigns = callsigns_list()

total_row_count = 0

for _ in callsigns:
    total_row_count += row_count(_)

print(f"Total row count: {total_row_count}")
print(f"Average row count: {total_row_count / len(callsigns)}")