# with open("./Data/Log info/2e0cvn.log.txt", "r", encoding = "utf-8") as f:
#     lines = f.readlines()
#     lines2 = [line for line in lines if line.startswith("QSO") == True]
#
#     test_lines = [test_line.removeprefix("QSO:").strip() for test_line in lines2]
#     for test_line in test_lines:
#
#         x = test_line.split(" ")
#         x = [_.strip() for _ in x if _.strip() != '']
#         print(len(x))
#
QSO_log_headers = ("freq", "mo", "date", "time", "sent_call", "sent_rst", "sent_exch", "rcvd_call", "rcvd_rst",
                        "rcvd_exch", "t")
#     print(len(QSO_log_headers))

from cabrillo_parser import header_parser
from cabrillo_parser import log_parser
from extract_callsigns import callsigns_list
import pandas as pd

all_callsigns = callsigns_list()
# callsign1 = all_callsigns[1]
# callsign2 = all_callsigns[2]
#
# logs1 = log_parser(callsign1)
# logs2 = log_parser(callsign2)
#
# all_logs = []
# all_logs.extend(logs1)
# all_logs.extend(logs2)
#
# logs = pd.DataFrame(all_logs)
# print(logs)










count = 0
lst1 = []
for callsign in all_callsigns:
    logs = log_parser(callsign)
    if len(logs) == 0:
        #print(f"{callsign} logs error")
        count += 1
        lst1.append(callsign)
print(lst1)

# n = 5
# lst1_test = ['3B8M']# '3B9KW', '3D2Y', '3V8SS', '3Z1K']
#
# for callsign in lst1_test:
#     rows = []
#     with open(f"./Data/Raw/2024 CQ WW CW Contest/{callsign}.txt", "r", encoding="utf-8") as f:
#         lines = f.readlines()
#         lines2 = [line for line in lines if line.startswith("QSO") == True]
#         test_lines = [test_line.removeprefix("QSO:").strip() for test_line in lines2]
#
#         for test_line in test_lines:
#             x = test_line.split(" ")
#             x = [_.strip() for _ in x if _.strip() != '']
#             if len(x) == 10:
#                 x.append(np.nan)
#                 print(x)
#             elif len(x) == 11:
#                 x = x
#             else:
#                 continue
#             # some operation on x
#             row = dict(zip(QSO_log_headers, x))
#             rows.append(row)
#
# print(rows)













# header_rows = []
#
# for callsign in all_callsigns:
#     header_rows.append(header_parser(callsign))
#
# header = pd.DataFrame(header_rows)
# count_of_transmitters = header[(header["CATEGORY-TRANSMITTER"] == "ONE")|(header["CATEGORY-TRANSMITTER"] == "TWO")].shape[0]
# print(f"{count_of_transmitters} transmitters found")
#
# def log_parser_debug(callsign, log_headers = QSO_log_headers):
#     if "/" in callsign:
#         callsign= callsign.replace("/", "_")
#
#     count = 0
#     #callsign = ""
#
#     with open(f"./Data/Raw/2024 CQ WW CW Contest/{callsign}.txt", "r", encoding="utf-8") as f:
#         lines = f.readlines()
#         lines2 = [line for line in lines if line.startswith("QSO") == True]
#         test_lines = [test_line.removeprefix("QSO:").strip() for test_line in lines2]
#         test_line = test_lines[0]
#
#         x = test_line.split(" ")
#         x = [_.strip() for _ in x if _.strip() != '']
#         if len(x) ==11:
#             #print(f"{callsign} has t")
#             count += 1
#             #callsign_with_t = callsign
#
#     return [count]
# t_counter = 0
# lst2 = []
# for callsign in all_callsigns:
#     t_counter += log_parser_debug(callsign)[0]
#     lst2.append(log_parser_debug(callsign)[1])
#
# print(f"{t_counter} logs with t")

# for _ in lst1:
#     if _ not in lst2:
#         print(f"{_} is not in lst2 but in lst1")
#
# for _ in lst2:
#     if _ not in lst1:
#         print(f"{_} is not in lst2 but in lst1")

