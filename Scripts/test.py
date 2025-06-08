import csv
import numpy as np
import pandas as pd



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

with open("./Data/Log info/2e0cvn.log.txt", "r", encoding = "utf-8") as f:
   lines = f.readlines() # list of strings ; each string is a line in the txt file
   lines1 = [line.rstrip() for line in lines if line.startswith("QSO") == False] # rstrip removes new line whitespace
   header_df = pd.DataFrame(lines1) # n x 1 dataframe
   #header_df = header_df.Series.str.split(": ")
   header_df = header_df[0].str.split(": ", n =1, expand = True) # splitting into n x 2 df;
   header_df = header_df[~header_df[0].str.contains("END-OF-LOG")] # removes column if category is "END of LOG"
   print(header_df.shape)

categories_of_interest = []



