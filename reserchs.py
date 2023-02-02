import requests
from bs4 import BeautifulSoup
import csv 

keyword = ''
keyword = input('Type a deviantart user to see their recent works!>')
keyword = keyword.lower()

url = 'https://www.deviantart.com/{}/gallery/all'.format(keyword)
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
dicts = {}
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

for i in faves:
    try:
        faveone = faves[a].find_all('span')       
    except IndexError as e:
        print("This user needs to draw more art!")
    
    favecount = str(faveone[1])
    
    favecount = favecount.strip('<span>')
    favecount = favecount.strip('</span>')
    
    
    
    if "." in favecount:
        favecount=favecount.replace(".","")
        if "K" in favecount:
            favecount=favecount.replace("K","00")
    else:
        if "K" in favecount:
            favecount=favecount.replace("K","000")

        
    favecountint = int(favecount)
    favelists.append(favecount)
    dicts.update({lists[a]:favecountint})
    a = a+1

count = 1
for i in range(len(favelists)):
    print(f'{count}. '+lists[i]+" - "+favelists[i]+" favorites")
    #numberedfaves = int(favelists[i])
    
    count = count+1
sorteddict = sorted(dicts.items(), key = lambda kv: kv[1])
sorteddict = dict(sorteddict)
sorteddict2 = sorted(dicts.items(), key = lambda kv: kv[1], reverse=True)
sorteddict2 = dict(sorteddict2)
print(("\nThe least favorited deviation recently is "+next(iter(sorteddict)) +" with "+str(list(sorteddict.items())[0][1])+" favorites\nand the most favorited deviation recently is "+next(iter(sorteddict2))+" with "+str(list(sorteddict2.items())[0][1]))+" favorites")
greatest = int((list(sorteddict2.items())[0][1]))
lowest = int((list(sorteddict.items())[0][1]))
between = greatest-lowest
diffs = between/greatest
diffs = diffs * 100
diffs = round(diffs, 2)
diffs = str(diffs)
print(f"The max difference of fave earned by two most recent pictures are {diffs}%")


#list(sorteddict)[0]
#next(iter(sorteddict))
#axa = list(sorteddict)[0]
#print(f"The most faved art recently is {axa}")

keyword = keyword.lower()
csv_header = ['No.', 'Title', 'Faves', 'Artist']
with open(f'{keyword}.csv','w',encoding='utf-8',newline='') as f:
    arts = csv.writer(f)
    arts.writerow(csv_header)
    for i in range(len(lists)):
        arts.writerow([i+1,lists[i],favelists[i],keyword])
exit()
#print(soup.prettify())