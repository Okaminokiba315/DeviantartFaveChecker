import requests
from bs4 import BeautifulSoup
import csv 

keyword = ''
keyword = input('Type a deviantart user to see their recent works!>')
keyword = keyword.lower()

url = 'https://www.deviantart.com/{}/gallery?page=1'.format(keyword)
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
}
req = requests.get(url,headers=headers)

nd = str(req)
if nd == '<Response [200]>':
    print(' ')
    print('This user is available!\n')
else:
    print(' ')
    print('This user is not available! Please run this program again.\n')
    exit()


soup = BeautifulSoup(req.content,'html.parser')

keyword = keyword.upper()
print(f'LIST OF RECENT {keyword} WORKS')
print('''
''')
items = soup.find_all('div',{'class':'_22J_R'})
lists = []
for i in items:
    i=str(i)
    i = i.strip('<div class="_22J_R">')
    i = i.strip('</')
    lists.append(i)
    #print(i)
#print(type(lists[0])) checking type

faves = soup.find_all('button',{'class':'_3Vvhk x48yz'})
favelists = []
a = 0
while a < 10: 
    faveone = faves[a].find_all('span')
    favecount = str(faveone[1])
    favecount = favecount.strip('<span>')
    favecount = favecount.strip('</span>')
    favelists.append(favecount)
    a = a+1

count = 1
for i in range(len(lists)):
    print(f'{count}. '+lists[i]+" - "+favelists[i]+" favorites")
    count = count+1


keyword = keyword.lower()
csv_header = ['No.', 'Title', 'Faves', 'Artist']
with open(f'{keyword}.csv','w',encoding='utf-8',newline='') as f:
    arts = csv.writer(f)
    arts.writerow(csv_header)
    for i in range(10):
        arts.writerow([i+1,lists[i],favelists[i],keyword])
exit()
#print(soup.prettify())