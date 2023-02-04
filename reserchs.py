import requests, re
from urlextract import URLExtract 
#from lipoja https://github.com/lipoja/URLExtract 
from bs4 import BeautifulSoup
import csv

questionable = 0
straight_nsfw = 0
maturelebels = ['']*10
arttype = ['']*10
printables=""

keyword = ''
keyword = input('Type a deviantart user to see their recent works!>')
keyword = keyword.lower()

url = 'https://www.deviantart.com/{}/gallery/all'.format(keyword)
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
}
req = requests.get(url,headers=headers)

nd = str(req)
soup = BeautifulSoup(req.content,'html.parser')

#To print entire HTML Page. Used for maintenance.
def print_txt(keyword):
    with open(f'{keyword}.txt','w',encoding='utf-8',newline='') as fyle:
        fyle.write(soup.prettify())
        fyle.close()


#To determine an active account. An active account should return Response 200 at all times.
if nd == '<Response [200]>':
    print(' ')
    print('This user is available!\n')

else:
    print(' ')
    deact = str(soup.prettify())
    if "DeviantArt: Deactivated Account" in deact:
        print('Deactivated Account!\n')
    elif "DeviantArt: 404" in deact:
        print('Account has never existed!\n')
    print('This user is not available! Please run this program again.\n')
    exit()



#saving number of faves
dicts = {}


#To determine name change of an user
name = soup.find_all('span',{'class':'_2UI2c'})
username = str(name[0])
del name
username = username.strip('span ')
username = username.strip('</span>')
username = username[16:]

if keyword.lower() != username.lower():
    printables+=f'\nThis user used to be around Deviantart with the name of {keyword.lower()},\nand now their name is {username}\n'
    print(printables)
    nowname = input("Would you like to use their current name (Y/N)?>")
    if nowname == 'Y' or nowname == 'y':
        keyword = username


keyword = keyword.upper()
printables += '\nLIST OF RECENT '+ keyword +' WORKS'
printables += '\n\n'

#Printing their recent art titles
items = soup.find_all('div',{'class':'_22J_R'})
lists = []
for i in items:
    i=str(i)
    i = i.strip('<div class="_22J_R">')
    i = i.strip('</')
    lists.append(i)
    
#Determining if a user have made no posts.
if len(items) == 0:
    print("They got no posts for now.\n")
    exit()

#Differ Visual and Literature arts and then
#Determining the contents
def addappend(lists,sensiti,maturelebels):
    for i in range (len(sensiti)):
        x = str(sensiti[i])
        if 'visual art' in x:
            for q in range (10):
                if lists[q] in x:
                    arttype[q] = 'Visual Art'
                    break 
        elif 'literature' in x:
            for q in range (10):
                if lists[q] in x:
                    arttype[q] = 'Literature'
                    break 
        if '<div class="tF4Rv">May contain sensitive content</div>' in x:
            for p in range (10):
                if lists[p] in x:
                    maturelebels[p] = 'Suggestive'
                    break 
            
        elif '<div class="tF4Rv">Sensitive content</div>' in x:
            for p in range (10):
                if lists[p] in x:
                    maturelebels[p] = 'Mature'
                    break 
            
        else:
            for p in range (10):
                if lists[p] in x:
                    maturelebels[p] = 'Safe'
                    break   

#For visual arts
sensiti1 = soup.find_all('a',{'class':'_1mCeE'})
for i in range (len(sensiti1)):
    addappend(lists,sensiti1,maturelebels)

#For literature arts
sensiti2 = soup.find_all('div',{'class':'_1mCeE'})
for i in range (len(sensiti2)):
    addappend(lists,sensiti2,maturelebels)

#Extracting URL
linkss= soup.find_all('a',{'data-hook':'deviation_link'})
linklists = []
a = 0
for i in range (len(linkss)):
    if i % 2 == 0:
        linksone = str(linkss[i])
        extractor = URLExtract()
        linksone = extractor.find_urls(linksone)
        linklists.append(linksone[0])

#Counting Mature and Suggestive Arts
for i in range (len(maturelebels)):
    if maturelebels[i] == 'Suggestive':
        questionable += 1
    elif maturelebels[i] == 'Mature':
        straight_nsfw += 1
    else:
        continue

#Stats to determine whether an acc is NSFW or not
#Determined with > 70%, > 40%, >= 10%
if len(lists) <= 10:
    if (questionable+straight_nsfw) > ((7 * len(lists))/10):
        if questionable > straight_nsfw:
            printables+="\nThis artist's contents are mostly suggestive.\n"
        else:
            printables+="\nThis artist's contents are not safe for work.\n"
    elif (questionable+straight_nsfw) > ((4 * len(lists))/10):
        if questionable >= straight_nsfw:
            printables+="\nSome of this artist's contents might not be safe for work and some are suggestive.\n"
        else:
            printables+="\nSome of this artist's contents are not be safe for work.\n"
    elif (questionable+straight_nsfw) >= ((1 * len(lists))/10) and (questionable+straight_nsfw) <= ((4 * len(lists))/10):
        printables+="\nThis artist's contents are mostly safe for work!\n"
    else:
        printables+="\nThis artist's contents are safe for work!\n"

if questionable > 0 or straight_nsfw > 0:
    printables+="\nFrom their "+ str(len(lists)) +" recent works, "+ str(questionable) +" are questionable, and "+ str(straight_nsfw) +" are mature.\n"
else:
    printables+="\nFrom their "+ str(len(lists)) + " recent works, "+ str(questionable+straight_nsfw) +" are either questionable or mature.\n"


#Counting faves and storing it on a dictionary
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

#Collecting results
for i in range(len(favelists)):
    printables+=f'\n{i+1}. '+lists[i]+" - "+favelists[i]+" favorites,\n"+"Art Type: "+arttype[i]+",\nMature Level: "+maturelebels[i]+",\nLink: "+linklists[i]+"\n"

#Basic stats of most and least popular work
sorteddict = sorted(dicts.items(), key = lambda kv: kv[1])
sorteddict = dict(sorteddict)
sorteddict2 = sorted(dicts.items(), key = lambda kv: kv[1], reverse=True)
sorteddict2 = dict(sorteddict2)
printables+= f"\nThe least favorited deviation recently is {next(iter(sorteddict))} with {str(list(sorteddict.items())[0][1])} favorites\nand the most favorited deviation recently is {next(iter(sorteddict2))} with {str(list(sorteddict2.items())[0][1])} favorites"
greatest = int((list(sorteddict2.items())[0][1]))
lowest = int((list(sorteddict.items())[0][1]))
del sorteddict, sorteddict2
between = greatest-lowest
diffs = between/greatest
diffs = diffs * 100
diffs = round(diffs, 2)
diffs = str(diffs)
printables+= f"\nThe max difference of fave earned by two most recent pictures are {diffs}%\n"


keyword = keyword.lower()

#Saving in .csv
def save_csv(keyword, lists,favelists,arttype,maturelevel,linklists):
    csv_header = ['No.', 'Title', 'Faves','Type','Artist','Mature','Link']
    with open(f'{keyword}.csv','w',encoding='utf-8',newline='') as f:
        arts = csv.writer(f)
        arts.writerow(csv_header)
        for i in range(len(lists)):
            arts.writerow([i+1,lists[i],favelists[i],arttype[i],keyword,maturelevel[i],linklists[i]])

#Saving in .txt
def printprintables(printables):
    with open(f'{keyword}_written_data.txt','w',encoding='utf-8',newline='') as dataz:
        dataz.write(printables)
        dataz.close()

#Displaying results
printmea = input("\nDisplay results in terminal (Y/N)?>")
if printmea == 'Y' or printmea == 'y':
    print(printables)

printme = input("\nPrint .csv proof (Y/N)?>")
if printme == 'Y' or printme == 'y':
    save_csv(keyword, lists,favelists,arttype,maturelebels,linklists)
printme2 = input("\nPrint .txt proof (Y/N)?>")
if printme2 == 'Y' or printme2 == 'y':
    #print_txt(keyword) #--> Only uncomment in maintenances or mods.
    printprintables(printables)

print("\nThank you for using this checker!\n")
exit()
