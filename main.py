import requests
from bs4 import BeautifulSoup as BeautifulSoup
import pandas as pd

url = 'https://www.cbr.ru/hd_base/metall/metall_base_new/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table1 = soup.find('table', class_='data')

headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)

mydata = pd.DataFrame(columns=headers)
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

mydata.to_csv('metall.csv', index=False)