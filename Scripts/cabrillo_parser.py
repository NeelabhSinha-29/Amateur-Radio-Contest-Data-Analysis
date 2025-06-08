# from extract_callsigns import callsigns_list
#
# callsigns = callsigns_list()
#
# test = []
# n = len(callsigns)
# for i in range(0,n):
#     test.append(callsigns[i])
#
# for _ in test:
#     if "/" in _:
#         _ = _.replace("/", "_")
#         #print(f"Warning! The callsign {_.replace("_","/")} has been renamed to {_} for naming purposes temporarily.")
#     with open(f"./Data/Raw/2024 CQ WW CW Contest/{_}.txt","r", encoding="utf-8", errors="replace") as f:
#         start_of_log = f.readline()
#         if "3" in start_of_log:
#             continue
#          #   print(f"log of entry {_} has been done in cabrillo format v3")
#         elif "2" in start_of_log:
#             print(f"log of entry {_} has been done in cabrillo format v2")
#         else:
#             print(f"log of entry {_} is unacceptable for not having the correct cabrillo format")

def cabrillo_format_version_checker(callsign):
    if "/" in callsign:
        callsign = callsign.replace("/", "_")
        print(f"Warning! The callsign {callsign.replace("_","/")} has been renamed to {callsign} for naming purposes temporarily.")
    with open(f"./Data/Raw/2024 CQ WW CW Contest/{callsign}.txt","r", encoding="utf-8", errors="replace") as f:
        start_of_log = f.readline()
        if "3" in start_of_log:
            return 3
        elif "2" in start_of_log:
            return 2
        else:
            return print("Invalid log")


def callsign_information_parser(log_file_path, newfile_filepath, version):
    if version == 3:
        with open(log_file_path, "r", encoding="utf-8", errors="replace") as f:
            with open(newfile_filepath, "x", encoding="utf-8", errors="replace") as f2:
                for line in f:
                    # removing categories not of interest (personal information)
                    if line.startswith(("X-", "NAME", "ADDRESS", "EMAIL", "OPERATORS"):
                        continue
                    # reading and writing



# def cabrillo_parser(callsign, log, file_path):
#     version = cabrillo_format_version_checker(callsign)
#     if version !=2 or version !=3:
#         return print("Invalid log")
#
#     if version == 3:
#         with open(log, "r", encoding="utf-8", errors="replace") as f:
#             for line in f:
