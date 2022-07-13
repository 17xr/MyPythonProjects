import requests
from bs4 import BeautifulSoup
import datetime

count = 0

curr_year = datetime.date.today().year
url = "https://www.cisa.gov/uscert/ncas/alerts/" + str(curr_year)
our_request = requests.get(url)
html = our_request.content
soup = BeautifulSoup(html,'html.parser')
tags = soup.find_all('span',class_="field-content")

count += len(tags)

i = 1
while True:
    new_url = url + "?page=" + str(i)
    new_request = requests.get(new_url)
    new_html = new_request.content
    phrase = b"There are no alerts currently available for this year."
    if phrase in new_html:
        break
    new_soup = BeautifulSoup(new_html,'html.parser')
    new_tags = new_soup.find_all('span',class_="field-content")
    count += len(new_tags)
    i += 1

print("The number of security alerts issued by US-CERT in the current year is: {}.".format(count))