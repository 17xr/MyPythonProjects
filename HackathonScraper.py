import requests
from bs4 import BeautifulSoup
from datetime import date

year = date.today().year + 1
url = "https://mlh.io/seasons/" + str(year) + "/events"
response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')
tags = soup.find_all('div', class_="event-wrapper")[:25]
for tag in tags:
    title = tag.find('a').attrs['title'].strip()
    flag = tag.find('div',class_="event-hybrid-notes").get_text().strip()
    date = tag.find('p').get_text().strip()
    city = tag.find_all("span")[0].get_text().strip()
    state = tag.find_all("span")[1].get_text().strip()
    print("The name of the hackathon: {}. It is: {}.".format(title,flag))
    if 'digital' in flag.lower():
        print("It takes place {}, at {}.".format(state,city))
    else:
        print("It takes place in the city : {}, in the state : {}.".format(city,state))
    print("Its date is : {}.".format(date))
    print()
    