import requests
from bs4 import BeautifulSoup

URL = "https://www.rottentomatoes.com/browse/movies_at_home/"
page = requests.get(URL)

with open('page.txt', 'w', encoding = 'utf-8') as f:
    f.write(page.text)


soup = BeautifulSoup(page.content, "html.parser")
films = soup.find_all("div", class_="js-tile-link")

tagsList = []
for film in films:
    tags = film.find_all("rt-text", slot="audienceScore")
    tagsList = tagsList + tags

with open('js-tile.txt','w',encoding='utf-8') as f:
    for tag in tagsList:
        f.write(tag.text)