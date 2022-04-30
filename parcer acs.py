import requests
from fake_useragent import UserAgent
import csv

agent = UserAgent()
url = 'https://www.originalcarparts.com/searchautocomplete/index/getjson/cache/1650944919/store/2/part/3'

response = requests.get(url=url, params={
    'user-agent': f'{agent.random}'
}).json()

with open('data_acs.csv', 'w', encoding='utf-8') as F:
    writer = csv.writer(F)
    writer.writerow(['Name', 'Desc', 'Prices', 'Photo'])

for elem in response:
    with open('data_acs.csv', 'a', encoding='utf-8') as F:
        writer = csv.writer(F)
        writer.writerow([elem['name'], elem['description'], elem['prices'], elem['imageurl']])