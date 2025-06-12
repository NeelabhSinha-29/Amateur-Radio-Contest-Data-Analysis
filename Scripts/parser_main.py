import cabrillo_parser as cp
import pandas as pd
import numpy as np
from extract_callsigns import callsigns_list
#import sqlite3

all_callsigns = callsigns_list()

# forming header dataframe

header_rows = []

for callsign in all_callsigns:
    header_rows.append(cp.header_parser(callsign))

header = pd.DataFrame(header_rows)

# forming logs dataframe

all_logs = []

for callsign in all_callsigns:
    log = cp.log_parser(callsign)
    all_logs.extend(log)

logs = pd.DataFrame(all_logs)

header.to_pickle("./Data/Pre-Processed/header.pickle")
logs.to_pickle("./Data/Pre-Processed/logs.pickle")


















# Not need --------------------
# header['CLAIMED-SCORE'] = pd.to_numeric(header['CLAIMED-SCORE'], errors='coerce')
# header['START-OF-LOG'] = pd.to_numeric(header['START-OF-LOG'], errors='coerce')
#
# conn = sqlite3.connect("contest_database.db")
# cursor = conn.cursor()
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS entries (
#     CALLSIGN TEXT PRIMARY KEY,
#     START_OF_LOG TEXT,
#     CONTEST TEXT,
#     CATEGORY_OPERATOR TEXT,
#     CATEGORY_ASSISTED TEXT,
#     CATEGORY_MODE TEXT,
#     CATEGORY_BAND TEXT,
#     CATEGORY_POWER TEXT,
#     CATEGORY_TRANSMITTER TEXT,
#     CATEGORY_OVERLAY TEXT,
#     GRID_LOCATOR TEXT,
#     CLAIMED_SCORE TEXT,
#     CREATED_BY TEXT,
#     LOCATION TEXT,
#     CATEGORY_STATION TEXT,
#     CATEGORY_TIME TEXT,
#     OFFTIME TEXT
# )
# ''')
# conn.commit()
#
# header.to_sql('entries', conn, if_exists='replace', index=False)