'''Mobile rates analysis '''
import requests
import csv
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.11 Safari/532.9'
in_query = input('Search item : ')
if in_query is '' :
    print('enter any queries..')
    exit()
in_query.replace(' ','+')
URL = 'https://www.flipkart.com/search?q=' + in_query
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
total_avail_stock = soup.find_all('span', attrs={'class':'_2yAnYN'})
tas = ''
tas = total_avail_stock[0].text
print(tas)
tas_1 = tas.split()
tas_1 = tas_1[5].replace(',','')
num_of_pages = round(int(tas_1)/24)
print(num_of_pages)
ct = 0
ct_p = 0
ls_name = []
ls_name_1 = []
ls_name_2 = []
def get_int(a):
    q = ''
    for i in a:
        if i.isdigit():
            q = "".join([q,i])
    return int(q)
def write_out():
    for n in range(0,len(ls_name)):
        with open(in_query.replace('+','_') + '.csv','a',newline='',encoding='utf-8') as f:
            thewriter = csv.writer(f)
            thewriter.writerow([ls_name[n],ls_name_1[n],ls_name_2[n]])
    f.close()
for n in range(0,num_of_pages + 1):
    URL = 'https://www.flipkart.com/search?q='+ in_query + '&page='+ str(n + 1)
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    title_block = soup.find_all('div', attrs={'class':'_3wU53n'})
    rate_block = soup.find_all('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating_block = soup.find_all('div', attrs={'class':'hGSR34'})
    ct_p += 1
    if ct_p == 30 :
        print('Data is too large do you want to continue Y / N ')
        if input() in ['y','Y'] :
            continue
        else:
            write_out()
            exit()
    if(0 < len(title_block)):
        for er in range(0, len(title_block)):
            name_is = title_block[er].text
            rate_is = rate_block[er].text
            rating_is = rating_block[er].text 
            print(name_is,'\t',rate_is,'\t',rating_is)
            ls_name.append(name_is)
            ls_name_1.append(get_int(rate_is))
            ls_name_2.append(rating_is)
            ct += 1
            pass
write_out()
print(ct)
print(ct_p)
