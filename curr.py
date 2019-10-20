import requests
import csv
from bs4 import BeautifulSoup
print( 'Enter country code and Num : ')
country_code = input('Enter country code : ')
curr = input('Enter currency amount : ')
URl = ''
URL = 'https://www.x-rates.com/table/?from=' + country_code + '&amount=' + curr
try:
    r = requests.get(URL)
except ConnectionError:
    print('Connection error')
soup = BeautifulSoup(r.content, 'html5lib')
result_block = ''
result_block = soup.find_all('td')
print (len(result_block))
ls_name = []
ls_name_1 = []
ls_name_2 = []
for er in range(0, len(result_block),3):
    name_is   = result_block[er].text
    name_is_1 = result_block[er + 1].text
    name_is_2 = result_block[er + 2].text
    ls_name.append(name_is)
    ls_name_1.append(name_is_1)
    ls_name_2.append(name_is_2)
for n in range(0,len(ls_name)):
    with open('mycsv.csv','a',newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow([ls_name[n],ls_name_1[n],ls_name_2[n]])
f.close()