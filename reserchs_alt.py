import requests, re
from urlextract import URLExtract 
#from lipoja https://github.com/lipoja/URLExtract 
from bs4 import BeautifulSoup
import csv,time



written = False
printables=""
pagenums=1

questionable_a = 0
straight_nsfw_a = 0

keyword = ''
keyword = input('Type a deviantart user to see their recent works!>')
keyword = keyword.lower()

url = 'https://www.deviantart.com/{}/gallery/all?page={}'.format(keyword,pagenums)
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

#Saving in .csv
def save_csv(keyword, lists,favelists,arttype,maturelevel,linklists):
    global written
    csv_header = ['Title', 'Faves','Type','Artist','Mature','Link']
    keyword=keyword.lower()
    with open(f'{keyword}.csv','a',encoding='utf-8',newline='') as f:
        arts = csv.writer(f)
        if written == False:
            arts.writerow(csv_header)
            written = True
        for i in range(len(lists)):
            arts.writerow([lists[i],favelists[i],arttype[i],keyword,maturelevel[i],linklists[i]])

#Saving in .txt
def printprintables(printables_a):
    with open(f'{keyword.lower()}_written_data.txt','a',encoding='utf-8',newline='') as dataz:
        dataz.write(printables_a)
        dataz.close()

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
    else:
        keyword = keyword



keyword = keyword.upper()
#print_txt(keyword)
#exit()
printme = input("\nPrint .csv proof (Y/N)?>")
printme2 = input("\nPrint .txt proof (Y/N)?>")

printables += '\nLIST OF ALL '+ keyword +' WORKS'
printables += '\n\n'

totaldevs = soup.find_all('span',{'class':'_2USdI'})
devsnumber = str(totaldevs[0])
devsnumber = devsnumber.strip('<span class="_2USdI">')
devsnumber = devsnumber.strip('</')

devsnumber = int(devsnumber)
numofdeviation = devsnumber

if devsnumber == 0:
    print("They got no posts for now.\n")
    exit()



#Printing their recent art titles
while devsnumber > 0:
    url = 'https://www.deviantart.com/{}/gallery/all?page={}'.format(keyword,pagenums)
    req = requests.get(url,headers=headers)
    nd = str(req)
    soup = BeautifulSoup(req.content,'html.parser')
    questionable = 0
    straight_nsfw = 0
    maturelebels = ['']*10
    arttype = ['']*10
    #saving number of faves
    dicts = {}

    items = soup.find_all('div',{'class':'_22J_R'})
    lists = []
    for i in items:
        i=str(i)
        i = i.strip('<div class="_22J_R">')
        i = i.strip('</')
        lists.append(i)

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
        printables+=f'\n-'+lists[i]+" - "+favelists[i]+" favorites,\n"+"Art Type: "+arttype[i]+",\nMature Level: "+maturelebels[i]+",\nLink: "+linklists[i]+"\n"
    if printme == 'Y' or printme == 'y':
        save_csv(keyword, lists,favelists,arttype,maturelebels,linklists)

    devsnumber -= 10
    pagenums += 1
    questionable_a += questionable
    straight_nsfw_a += straight_nsfw
    totaldone=numofdeviation-devsnumber
    totaldone = (totaldone*100)/numofdeviation
    if totaldone < 100:
        print (f'\nCalculation {totaldone}% done!')
    else:
        print('\nCalculation done!')
    #To give requests some delay
    time.sleep(1)

questionable_arts = questionable_a/numofdeviation
nsfw_arts = straight_nsfw_a/numofdeviation
printables_a = ''
printables_a += f'\nFrom {numofdeviation} total arts, \n{questionable_a} ({questionable_arts*100}%) are questionable, \nand {straight_nsfw_a} ({nsfw_arts*100}%) are not safe for work.\n'
printables_a += printables

del printables

keyword = keyword.lower()
#Displaying results
printmea = input("\nDisplay results in terminal (Y/N)?>")
if printmea == 'Y' or printmea == 'y':
    print(printables_a)

if printme2 == 'Y' or printme2 == 'y':
    #print_txt(keyword) #--> Only uncomment in maintenances or mods.
    printprintables(printables_a)



print("\nThank you for using this checker!\n")
exit()
