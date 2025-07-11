import requests
from bs4 import BeautifulSoup

# url = "https://cqww.com/publiclogs/2024cw/"
# html = requests.get(url).text
#
# soup = BeautifulSoup(html, 'html.parser')
#
# # print(soup.prettify())
#
# soup_callsigns = soup.find_all('div', class_='w3-cell w3-mobile')
#
# # print(len(soup_callsigns))
#
# callsigns = []
#
# for column in soup_callsigns:
#     #column_len = len(column.find_all('a'))
#     #print(column_len)
#     for row in column.find_all('a'):
#         callsigns.append(row.text)


def callsigns_list(url = "https://cqww.com/publiclogs/2024cw/", class_ = 'w3-cell w3-mobile'):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    soup_callsigns = soup.find_all('div', class_=class_)
    callsigns = []
    for column in soup_callsigns:
        for row in column.find_all('a'):
            callsigns.append(row.text)
    return callsigns


