from bs4 import BeautifulSoup
import requests
import string
import re

url = "http://www.bobdylan.com/songs/"
main_page = requests.get(url)

main_text = main_page.text
soup = BeautifulSoup(main_text, "html5lib")

spans = soup.find_all("span", {"class": "song"})
link_list = []
for span in spans:
    links = span.find_all('a')
    for link in links:
        link_list.append(link['href'])


f = open("dylan_lyrics.txt", "w")
for link in link_list:
    lyric_page = requests.get(link)
    lyric_text = lyric_page.text
    lyric_soup = BeautifulSoup(lyric_text, "html5lib")
    lyrics = lyric_soup.find("div", {"class": "article-content lyrics"})
    lyrics = lyrics.getText()
    lyrics = lyrics.encode('ascii', 'ignore')
    lyrics = lyrics[: lyrics.find("Copyright")]
    f.write(lyrics.strip())
f.close()



