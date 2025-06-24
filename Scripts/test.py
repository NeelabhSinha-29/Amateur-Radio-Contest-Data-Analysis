import csv
import numpy as np
import pandas as pd
from extract_callsigns import callsigns_list


# with open("./Data/Log info/2e0cvn.log.txt", "r", encoding = "utf-8") as f:
#
#     data =[]
#
#     n = 0
#
#     for line in f: # number of lines in header
#         n += 1
#
#     for i in range(n):
#         write = f.readline().strip()
#         write = write.split(": ")
#         data.append(write)

# parsing header information
#def header_parser(X):

# structure of how to parse logfile
#def function : input file? - not possible callsign
    # make dfs for header and QSO log tables with headers predetermined
    # open file using callsign, f
    # loop file for every line
        # if doesn't startswith("QSO"):
            # if line == END of LOG : break
            # header parsing algorithm; input = line of log --> output gets stored in header dataframe
            #

        # elif startwith("QSO"):
            # QSO log parsing algorithm; input = line of log --> output entry into log dataframe

    #return both dfs






# d = {}
#
# for line in data:
#     d.update({line[0]: line[1]})
#
#
# data = np.array(data)
# print(data.T)

#with open("./Data/Log info/test.csv", "w", newline="") as f2:
#    writer = csv.writer(f2)
#    writer.writerows(data.T)



# with open("./Data/Log info/2e0cvn.log.txt", "r", encoding = "utf-8") as f:
#    lines = f.readlines() # list of strings ; each string is a line in the txt file
#    lines1 = [line.rstrip() for line in lines if line.startswith("QSO") == False] # rstrip removes new line whitespace
#    header_df = pd.DataFrame(lines1) # n x 1 dataframe
#    #header_df = header_df.Series.str.split(": ")
#    header_df = header_df[0].str.rsplit(":", n =1, expand = True) # splitting into n x 2 df;
#    header_df = header_df[~header_df[0].str.contains("END-OF-LOG")] # removes column if category is "END of LOG"
#    header_df = header_df.replace("", np.nan)
#    print(header_df)


# for category in categories_of_interest:
#    if category not in header_df[0].values:
#       missing_categories.append(category)

# -------------------------------------------------------------


# categories_of_interest = ("START-OF-LOG", "CALLSIGN", "CONTEST",\
#                           "CATEGORY-OPERATOR", "CATEGORY-ASSISTED", \
#                           "CATEGORY-MODE", "CATEGORY-BAND", "CATEGORY-POWER", \
#                           "CATEGORY-TRANSMITTER", "CATEGORY-OVERLAY", "GRID-LOCATOR",\
#                           "CLAIMED-SCORE", "CREATED-BY", "LOCATION", "CATEGORY-STATION",\
#                           "CATEGORY-TIME", "OFFTIME")
#
# new_df = pd.DataFrame(columns= categories_of_interest)
#
#
#
# callsigns_list = callsigns_list()
# n = 5
# callsigns_list = callsigns_list[:n]
#
# strings_to_exclude = ("X-", "x-", "NAME", "ADDRESS", "EMAIL", "OPERATORS", "QSO", "SOAPBOX", "CLUB", "END-OF-LOG", "CERTIFICATE")
#
# for _ in callsigns_list:
#    if "/" in _:
#       _ = _.replace("/", "_")
#    #print(_)
#    #missing_categories = []
#    with open(f"./Data/Raw/2024 CQ WW CW Contest/{_}.txt", "r", encoding="utf-8") as f:
#       lines = f.readlines()  # list of strings ; each string is a line in the txt file
#
#       lines1 = [line.strip() for line in lines if
#                 line.startswith(strings_to_exclude) == False]  # strip removes new line whitespace
#
#       header_df = pd.DataFrame(lines1)  # n x 1 dataframe
#       # header_df = header_df.Series.str.split(": ")
#
#       header_df = header_df[0].str.split(":", n=1, expand=True)  # splitting into n x 2 df; ":" leaves some whitespace
#
#       header_df = header_df.replace("", np.nan) # Filling empty strings with NaN/None
#
#       header_df[0] = header_df[0].str.strip() # Removing Whitespaces before and after
#       header_df[1] = header_df[1].str.strip()
#
#       header_df.dropna(subset = [0], inplace=True) # Removes Empty
#
#       for information in header_df[0].values:
#          if information not in categories_of_interest:
#             print(f"Warning! - {_} has a unformatted category : {information}")
#       #print(header_df)
#       for category in categories_of_interest:
#          if category not in header_df[0].values:
#             #missing_categories.append(category)
#             new_row = pd.DataFrame([[category, np.nan]])
#             header_df = pd.concat([header_df, new_row])
#             header_df = header_df.sort_values(by = 0, ascending = True)
#             header_df.reset_index(drop=True, inplace=True)
#
#       #print(header_df)


#
# with open("./Data/Raw/2024 CQ WW CW Contest/4X5UR.txt", "r", encoding = "utf-8") as f:
#    lines = f.readlines() # list of strings ; each string is a line in the txt file
#    lines1 = [line.strip() for line in lines if line.startswith("QSO") == False] # rstrip removes new line whitespace
#    header_df = pd.DataFrame(lines1) # n x 1 dataframe
#    #header_df = header_df.Series.str.split(": ")
#    header_df = header_df[0].str.rsplit(":", n =1, expand = True) # splitting into n x 2 df;
#    header_df = header_df[~header_df[0].str.contains("END-OF-LOG")] # removes column if category is "END of LOG"
#    header_df = header_df.replace("", np.nan)
#    header_df.dropna(subset=[0], inplace=True)
#
#    print(header_df)
#
#

# -------------------------------------------------------------

categories_of_interest = ("START-OF-LOG", "CALLSIGN", "CONTEST",\
                          "CATEGORY-OPERATOR", "CATEGORY-ASSISTED", \
                          "CATEGORY-MODE", "CATEGORY-BAND", "CATEGORY-POWER", \
                          "CATEGORY-TRANSMITTER", "CATEGORY-OVERLAY", "GRID-LOCATOR",\
                          "CLAIMED-SCORE", "CREATED-BY", "LOCATION", "CATEGORY-STATION",\
                          "CATEGORY-TIME", "OFFTIME")

new_df = pd.DataFrame(columns= categories_of_interest)



callsigns_list = callsigns_list()

sample_callsign = callsigns_list[0]

strings_to_exclude = ("X-", "x-", "NAME", "ADDRESS", "EMAIL", "OPERATORS", "QSO", "SOAPBOX", "CLUB", "END-OF-LOG", "CERTIFICATE")

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

n = 7961

test_callsigns = callsigns_list[:n]

rows = []

for callsign in test_callsigns:
    rows.append(header_parser(callsign))

header = pd.DataFrame(rows)

QSO_log_headers = ("freq", "mo", "date", "time", "sent_call", "sent_rst", "sent_exch", "rcvd_call", "rcvd_rst", "rcvd_exch", "t")

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
                continue
            row = dict(zip(log_headers, x))
            rows.append(row)

    return rows

for callsign in test_callsigns:
    logs = log_parser(callsign)
    print(logs[:5])
