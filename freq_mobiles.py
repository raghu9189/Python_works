import requests
import csv
from bs4 import BeautifulSoup
URL = 'https://www.flipkart.com/mobile-phones-store?otracker=nmenu_sub_Electronics_0_Mobiles'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
result_block = soup.find_all('td')
print (len(result_block))
ls_name = []
if(0 < len(result_block)):
    print("Data is found..!\nFrequently Searched Mobiles\n")
    for er in range(0, 11):
        name_is   = result_block[er].text
        print(name_is)
        ls_name.append(name_is)
        pass
    print('\nDo you want a CSV copy Y / N')
    to_csv = input()
    to_check = ['Y','y']
    if(to_csv in to_check):
        for n in range(0,len(ls_name)):
            with open('flipkart_Frequently_Searched_Mobiles.csv','a',newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([ls_name[n]])
        f.close()
        print('Saved..!')
    else:
        print('Done..!')
else:
    print('\nNo data found..!')