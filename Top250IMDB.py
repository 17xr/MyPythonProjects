import requests
import re
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
request = requests.get(url)
html = request.content
soup = BeautifulSoup(html, 'html.parser')

tags = soup.find_all('td', class_="titleColumn")

for tag in tags:
    title = tag.find("a").get_text().strip()
    director = tag.find("a").attrs['title'].split(",")[0][:-7].strip()
    characters = ",".join(tag.find("a").attrs['title'].strip().split(",")[1:])
    release_year = re.sub("[()]","", tag.find("span", class_="secondaryInfo").get_text() ).strip()
    print("The name of the movie is: {}, it was released in: {}.".format(title,release_year))
    print("It was directed by: {}, the main actors are:{}.".format(director,characters))
    print()