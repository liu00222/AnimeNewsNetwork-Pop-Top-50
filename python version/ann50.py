import requests
from bs4 import BeautifulSoup


path = "https://www.animenewsnetwork.com/encyclopedia/ratings-anime.php?top50=popular"
page = requests.get(path)
contents = page.content


soup = BeautifulSoup(contents, 'html.parser')
table = soup.find('table')

names = []
ratings = []
voters = []


texts = table.findAll('a')
numbers = table.findAll('td', class_ = 'r')[2:]
item_num = len(texts)


for i in range(item_num):
    names.append(texts[i].contents[0])
    ratings.append(numbers[2*i].contents[0])
    voters.append(numbers[2*i + 1].contents[0])
    print(names[i])
    print(ratings[i])
    print(voters[i])
    print()
