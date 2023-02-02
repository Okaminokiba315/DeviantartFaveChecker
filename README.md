# DeviantartFaveChecker
By: Okaminokiba315



Outside Sources:
get-pip.py from pypa.io
URL Extreactor from https://github.com/lipoja/URLExtract

This mini project is useful to see a summary of your and your fellow deviant's recent arts number of favorites.

![Screenshot 2023-01-12 141556](https://user-images.githubusercontent.com/97293254/212002194-e35e0573-2405-4e72-8792-f806dfcfeaa3.jpg)

# How to use the fave checker

1. Clone the file by going to your command prompt, and go to your preffered directory.
Then, copy the line below (without the ' ') and paste it to the command prompt. 

'git clone https://github.com/Okaminokiba315/DeviantartFaveChecker.git'

A folder named DeviantartFaveChecker and its contents will appear in your directory.

2. Open the entire folder with your favorite compiler, and run the 'reserchs.py' file. 
If you have downloaded the package for the first time, you might be asked to
install "requests", "urlextract", and "bs4" (Thanks PeterKart for pointing out).
There's also user-agent field that might have to be replaced first.
Find your user agent here:
https://www.whatismybrowser.com/detect/what-is-my-user-agent/

By default, the user agent is 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' .

How to replace user agent: 

headers = {
    'user-agent': '(Replace this part with your user agent, keep the '' outside but delete the ().)'
}

3. You will be asked about the deviant name you wanted to check.
Keep in mind that this favechecker can tolerate uppercase and lowercase letters, but not typos.
The program will continue properly if the user is found.
(The program accepts a deviant's old username before being replaced by their new username but the program will terminate if the deviant's account is suspended or deleted.)

4. After you see the result, a .csv file would be made.

# Hopes for Future Works
1. Ranking Recent Works based on faves
2. Better Error Handling
3. Better handling for deviants with fave number of 1K and up

# Updates

-1st Feb 2023 = Least faved and most faved, with percentage of faves difference.
-2nd Feb 2023 = Handling 1K+ faves with basic approach (removing '.' and converting K to '000'), Adding Links and Mature content warning for some artists