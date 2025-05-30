import requests
from bs4 import BeautifulSoup

url = "https://cqww.com/publiclogs/2024cw/"
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())

soup_callsigns = soup.find_all('div', class_='w3-cell w3-mobile')

# print(len(soup_callsigns))

callsigns = []
callsigns_logs = []

for column in soup_callsigns:
    #column_len = len(column.find_all('a'))
    #print(column_len)
    for row in column.find_all('a'):
        callsigns.append(row.text)
        log_URL = row.get('href')
        callsigns_logs.append(url + log_URL)



for log in range(len(callsigns_logs)):
    r = requests.get(callsigns_logs[log]).text
    callsign = callsigns[log]
    if '/' in callsign:
        print(f"️ WARNING: '/' found in callsign '{callsign}', replacing with '_'")
        callsign = callsign.replace('/', '_')
    file_path = f"Data/Raw/2024 CQ WW CW Contest/{callsign}.txt"

    with open(file_path, 'w', encoding= 'utf-8') as f:
        f.write(r)



