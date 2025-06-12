from extract_callsigns import callsigns_list
import pandas as pd
import numpy as np

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


# def callsign_information_parser(log_file_path, newfile_filepath, version):
#     if version == 3:
#         with open(log_file_path, "r", encoding="utf-8", errors="replace") as f:
#             with open(newfile_filepath, "x", encoding="utf-8", errors="replace") as f2:
#                 for line in f:
#                     # removing categories not of interest (personal information)
#                     if line.startswith(("X-", "NAME", "ADDRESS", "EMAIL", "OPERATORS")):
#                         continue
#                     # reading and writing
#


# def cabrillo_parser(callsign, log, file_path):
#     version = cabrillo_format_version_checker(callsign)
#     if version !=2 or version !=3:
#         return print("Invalid log")
#
#     if version == 3:
#         with open(log, "r", encoding="utf-8", errors="replace") as f:
#             for line in f:


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

categories_of_interest = ("START-OF-LOG", "CALLSIGN", "CONTEST",\
                          "CATEGORY-OPERATOR", "CATEGORY-ASSISTED", \
                          "CATEGORY-MODE", "CATEGORY-BAND", "CATEGORY-POWER", \
                          "CATEGORY-TRANSMITTER", "CATEGORY-OVERLAY", "GRID-LOCATOR",\
                          "CLAIMED-SCORE", "CREATED-BY", "LOCATION", "CATEGORY-STATION",\
                          "CATEGORY-TIME", "OFFTIME")

strings_to_exclude = ("X-", "x-", "NAME", "ADDRESS", "EMAIL", "OPERATORS", "QSO", "SOAPBOX", "CLUB", "END-OF-LOG", "CERTIFICATE")

QSO_log_headers = ("freq", "mo", "date", "time", "sent_call", "sent_rst", "sent_exch", "rcvd_call", "rcvd_rst", "rcvd_exch", "t")

def header_parser(callsign, data_cats = categories_of_interest, exclude_cats = strings_to_exclude):
    if "/" in callsign:
        callsign= callsign.replace("/", "_")
    # print(_)
    # missing_categories = []
    row = {}

    with open(f"./Data/Raw/2024 CQ WW CW Contest/{callsign}.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()  # list of strings ; each string is a line in the txt file

        lines1 = [line.strip() for line in lines if
                  line.startswith(exclude_cats) == False]  # strip removes new line whitespace

        for line in lines1:
            x = line.strip().split(":", 1)
            x = [_.strip() for _ in x]

            if len(x) == 2:

                if x[1] == "":
                    x[1] = np.nan
                row.update({x[0]:x[1]})


            else:
                #print(f"{line} did not split or has issues")
                continue

        for y in data_cats:
            if y not in row.keys():
                #print(f"{y} not in rows of {callsign}")
                row.update({y:np.nan})

    return row

def log_parser(callsign, log_headers = QSO_log_headers):
    if "/" in callsign:
        callsign= callsign.replace("/", "_")

    rows = []

    with open(f"./Data/Raw/2024 CQ WW CW Contest/{callsign}.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines2 = [line for line in lines if line.startswith("QSO") == True]
        test_lines = [test_line.removeprefix("QSO:").strip() for test_line in lines2]
        for test_line in test_lines:
            x = test_line.split(" ")
            x = [_.strip() for _ in x if _.strip() != '']
            if len(x) == 10:
                x.append(np.nan)
            elif len(x) == 11:
                x = x
            else:
                continue
            row = dict(zip(log_headers, x))
            rows.append(row)

    return rows

# Manual analysis of runnin code on shorten files
