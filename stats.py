import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
printables = ''
filez = "okaminokiba315_202327935.csv"
bannedwords = []

filez = input("Add .csv input to check> ")
if filez[-4:] != ".csv":
    filez = filez + ".csv"

def median(x):
    print('a')
    print (len(x))
    medianplace = int(len(x)/2)
    if len(x) % 2 == 0:
        medianplace2 = int(medianplace - 1)
        print(medianplace,medianplace2)
        
        a= str(x[medianplace])[1:-3]
        b= str(x[medianplace2])[1:-3]
        print(a,b)
        a = int(a)
        b = int(b)
        dv = int((int(a)+int(b))/2)
        print("\nMedian: "+str(dv))
        return int(dv)
    else:
        print(x[medianplace])
        dv = int(str(x[medianplace])[1:-3])
        print("\nMedian: "+ str(dv))
        return int(dv)

def fave_ct(filez):
    try:
        df=pd.read_csv(filez,usecols=["Faves"])
    except FileNotFoundError:
        print("File not found! Make sure you typed the file name correctly or the file exists!")
        exit()
    yg=pd.read_csv(filez,usecols=["Title"])
    x = df.values.tolist()[:-1]
    yg = yg.values.tolist()[:-1]
    aaaa = []

    #y = average
    y = 0
    for i in range (len(x)):
        xy = str(x[i])
        #print(xy)
        y += float(xy[1:-1])
        aaaa.append(float(xy[1:-1]))
    y=y/len(x)
    #print(y)

    #Variance = sum(value i - average)**2
    variance_case = 0
    ssss = []
    for i in range (len(x)):
        spr = str(x[i])
        a = float(spr[1:-1])
        a = a-y
        #print(a)
        ssss.append(a)
        a = pow(a,2)
        variance_case += a
        #print(f"{i+1}. {a}")
    variance_case = variance_case/len(x)
    print(f"\nVar: {variance_case}")

    std_deviation = math.sqrt(variance_case)
    print(f"\nStd Deviation: {std_deviation}")

    medyan = median(x)

    zscore = []
    outlier_yes_no = []
    for i in range(len(x)):
        z = (aaaa[i]-y)/std_deviation
        if z < -2.5 or z > 2.5:
            outlier_yes_no.append('Outlier')
        else:
            outlier_yes_no.append('')
        zscore.append(z)
        print (yg[i],zscore[i],outlier_yes_no[i])
    
    plt.hist(aaaa)
    plt.show()
    plt.hist(ssss)
    plt.show()


def sensitive_params(filez,content_toleration,tolerate_suggestive):
    df=pd.read_csv(filez,usecols=["Mature"])
    x = df.values.tolist()[:-1]
    aaaa = []
    for i in range (len(x)):
        xy = str(x[i])
        aaaa.append(xy)
    count = 0
    if tolerate_suggestive == 'y':
        for i in range (len(aaaa)):
            if 'Safe' in aaaa[i] or 'Suggestive' in aaaa[i]:
                count += 1
    else:
        for i in range (len(aaaa)):
            if 'Safe' in aaaa[i]:
                count += 1
    #print((len(x)-count)/len(x))
    if ((len(x)-count)/len(x)) > content_toleration:
        return "Autobanned"
    else:
        return "Mostly safe content"


def title_params(filez,bannedwords,content_toleration):
    global printables
    df=pd.read_csv(filez,usecols=["Title"])
    x = df.values.tolist()[:-1]
    aaaa = []
    y = 0
    for i in range (len(x)):
        xy = str(x[i])
        aaaa.append(xy)
    count = 0
    for i in range (len(aaaa)):
        for j in range (len(bannedwords)):
            if str(bannedwords[j]).lower() in str(aaaa[i]).lower():
                count += 1
                #print(f"{count} Sus Found!")
                break
    if (count/len(aaaa)) > content_toleration:
        printables += 'This user does not pass the safe content test.'
    else:
        printables += "Based by Title, This User is Safe."

def step_two():
    content_toleration = int(input('Add percentage of avoided tags to tolerate. >'))
    content_toleration = content_toleration/100
    title_params(filez,bannedwords,content_toleration)


def safe_content():
    global printables
    print('Add tags to avoid, max 30.\nType "F" to continue.')
    for i in range(30):
        x = input('>')
        x = x.lower()
        if x == 'f':
            break
        bannedwords.append(x)
    filter_sensitive = str(input("Ban for over-toleration level sensitive content? (Y/N)>"))
    
    if filter_sensitive.lower() == 'y':
        content_toleration = int(input('Add percentage of mature content to tolerate. >'))
        content_toleration = content_toleration/100
        tolerate_suggestive = str(input("Tolerate suggestive art? (Y/N)>"))
        tolerate_suggestive = tolerate_suggestive.lower()
        rest = sensitive_params(filez,content_toleration,tolerate_suggestive)
        if rest == 'Autobanned':
            printables +='This user does not pass the safe content test.'
            return
        else:
            step_two()
    else:
        step_two()
fave_ct(filez)
bb = input('Check for unsafe content?(Y/N)>')      
if bb.lower() == 'y':
    safe_content()
    print(printables)
    #with open(f'{filez}_bannable_check.txt','w',encoding='utf-8',newline='') as fyle:
    #    fyle.write(printables)
    #    fyle.close()

