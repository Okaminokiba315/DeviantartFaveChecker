# DeviantartFaveChecker
By: Okaminokiba315

# Background:
I have known deviantArt since I was young, probably started on 2012's.
In 2023, I planned to make a data project based on deviantArt.

With my novice-basic knowledge of Python and Data Scraping, I started off
by retrieving important datas from front-end/surface like username, work titles, and favorites.

However, I noticed that if used properly, this DA Fave Checker can
do so much more. It might help people to pick safe deviants to follow (If you see my arts
you might want to avoid me, but still, feel free to use this tool in consideration.),
commission potential artists, find old deviants, track deactivated accounts,
comparing progresses, or just giving quick infos and access to new arts of an artist.

This tool is free for all to use, copy, or modify.
Any modifications uploaded to the internet mentioning me as the maker of the
parent code will be highly appreciated.

# Warning

1. Use and modify this program wisely. 
You can track progresses, deviant trolls, unsafe accounts,
a bully's activity, collect evidences at real time, etc. 
I am not responsible for any damages or dramas caused by the usage of this program.

2. This program will not hack or penetrate dA's security in any way, since this program
only retrieves visible information from the front-end (visible) layer and summarizes it.
However, the program 'reserchs_alt.py' might cause traffic that returns response 403
due to retrieving too much URL in some cases.

# Outside Sources:
1. get-pip.py from pypa.io
2. URL Extractor from https://github.com/lipoja/URLExtract

# This mini project is useful for:
1. Seeing a summary of your and your fellow deviant's recent arts number of favorites.
2. Detecting a change of a deviant's username or art status.
3. Determining whether an account is safe for general audiences or not.
4. Knowing deactivated accounts and unused account names.
5. Collecting newest proofs of an account's arts in .txt and .csv format.
6. Basic stats of most popular and least popular arts.
7. Comparing updates based on timestamps.

# Questions

1. Will this replace manual proof-searching and manual-reviewing? No. 
It will make your data collection faster, but it won't replace manual
reviewing as manual proof-searching allows you to look 
for more proofs inside or outside dA, and manual reviewing helps you
to make a better decision regarding a deviant.

2. Will there be updates? Probably yes. Use 'git pull' command to
update.

![Screenshot 2023-01-12 141556](https://user-images.githubusercontent.com/97293254/212002194-e35e0573-2405-4e72-8792-f806dfcfeaa3.jpg)

# How to use the fave checker

1. Clone the file by going to your command prompt, and go to your preffered directory.
Then, copy the line below (without the ' ') and paste it to the command prompt. 

'git clone https://github.com/Okaminokiba315/DeviantartFaveChecker.git'

A folder named DeviantartFaveChecker and its contents will appear in your directory.

2. Open the entire folder with your favorite compiler, and run the 'reserchs.py' or 'reserchs_alt.py' file with the command 'python reserchs.py' or 'python reserchs_alt.py'

If you have downloaded the package for the first time, you might be asked to
install "requests", "urlextract", and "bs4" (Thanks PeterKart for pointing out).

However, now you can install all packages by running 
'pip install -r requirements.txt' command on your terminal.

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

4. A .csv or .txt file would be made by your preferences. You will also be free to choose
to display the result on the terminal.

# Hopes for Future Works
1. Better Error Handling
2. Better handling for deviants with fave number of 1K and up
3. Ranking most used tags of a deviant to determine their interests.
4. Faster process for 'reserchs_alt.py'

# Updates

1. 1st Feb 2023 = Least faved and most faved, with percentage of faves difference.
2. 2nd Feb 2023 = Handling 1K+ faves with basic approach (removing '.' and converting K to '000'), Adding Links and Mature content warning for some artists
3. 4th Feb 2023 = Handling mature content indicator separately for visual-art and literature works. Adding choice to display proofs with terminal or by csv table and txt. Deleted repeated function. Added documentation.
4. 5th Feb 2023 = Added 'reserchs_alt.py'. Limited function and slower than its
counterpart, but can retrieve more art infos up to all arts of an user. Added Timestamps.