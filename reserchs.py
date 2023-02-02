import requests, re
from urlextract import URLExtract 
#from lipoja https://github.com/lipoja/URLExtract 
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
#with open(f'{keyword}.txt','w',encoding='utf-8',newline='') as fyle:
#    fyle.write(soup.prettify())
#    fyle.close()

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

linkss= soup.find_all('a',{'data-hook':'deviation_link'})
linklists = []
a = 0
for i in range (len(linkss)):
    if i % 2 == 0:
        #print(linkss[i])
        linksone = str(linkss[i])
        extractor = URLExtract()
        linksone = extractor.find_urls(linksone)
        linklists.append(linksone[0])
        


sensitive = soup.find_all('div',{'class':'tF4Rv'})
sensilist = []
for i in sensitive:
    i=str(i)
    i = i.strip('<div class="tF4Rv">')
    i = i.strip('</')
    sensilist.append(i)

if len(sensilist) == 0:
    print("They got no posts for now.\n")
    exit()

questionable = 0
straight_nsfw = 0
if len(lists) <= 10:
    if len(sensilist) > ((7 * len(lists))/10):
        for a in sensilist:
            if "May" in a:
                questionable = questionable + 1
            else:
                straight_nsfw = straight_nsfw + 1
        if questionable > straight_nsfw:
            print("\nThis artist's contents are mostly suggestive.\n")
        else:
            print("\nThis artist's contents are not safe for work.\n")
    elif len(sensilist) > ((4 * len(lists))/10):
        for a in sensilist:
            if "May" in a:
                questionable = questionable + 1
            else:
                straight_nsfw = straight_nsfw + 1
        if questionable >= straight_nsfw:
            print("\nSome of this artist's contents might not be safe for work and some are suggestive.\n")
        else:
            print("\nSome of this artist's contents are not be safe for work.\n")
    elif len(sensilist) >= ((1 * len(lists))/10) and len(sensilist) <= ((4 * len(lists))/10):
        for a in sensilist:
            if "May" in a:
                questionable = questionable + 1
            else:
                straight_nsfw = straight_nsfw + 1
        print("\nThis artist's contents are mostly safe for work!\n")
    else:
        print("\nThis artist's contents are safe for work!\n")

if questionable > 0 or straight_nsfw > 0:
    print(f"\nFrom their {len(lists)} recent works, {questionable} are questionable, and {straight_nsfw} are mature.\n")
else:
     print(f"\nFrom their {len(lists)} recent works, {len(sensilist)} are either questionable or mature.")


faves = soup.find_all('button',{'class':'_3Vvhk x48yz'})
favelists = []

a = 0

for i in faves:
    try:
        faveone = faves[a].find_all('span')       
    except IndexError as e:
        print("This user needs to draw more art!")
   # print(faveone)
    favecount = str(faveone[1])
    #print(favecount)
    
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
    print(f'{count}. '+lists[i]+" - "+favelists[i]+" favorites,\nLink: "+linklists[i]+"\n")
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
print(f"The max difference of fave earned by two most recent pictures are {diffs}%\n")


#list(sorteddict)[0]
#next(iter(sorteddict))
#axa = list(sorteddict)[0]
#print(f"The most faved art recently is {axa}")

keyword = keyword.lower()
csv_header = ['No.', 'Title', 'Faves', 'Artist','Link']
with open(f'{keyword}.csv','w',encoding='utf-8',newline='') as f:
    arts = csv.writer(f)
    arts.writerow(csv_header)
    for i in range(len(lists)):
        arts.writerow([i+1,lists[i],favelists[i],keyword,linklists[i]])
exit()
