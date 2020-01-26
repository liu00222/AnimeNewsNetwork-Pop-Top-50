import requests
from bs4 import BeautifulSoup


# get the html source code of the target page
path = "https://www.animenewsnetwork.com/encyclopedia/ratings-anime.php?top50=popular"
page = requests.get(path)
contents = page.content

soup = BeautifulSoup(contents, 'html.parser')
table = soup.find('table')

# create three lists to store the values indicated by their variables names
names = []
ratings = []
voters = []

# extract the data we need from the object
texts = table.findAll('a')
numbers = table.findAll('td', class_ = 'r')[2:]
item_num = len(texts)

# create the file in the same directory to receive the data
f = open("ann_pop_50.csv", "w+")

# write the header of the csv file
f.write("names,ratings,voter_num\n")

# iteratively write the data into the file
for i in range(item_num):
    content_lst = texts[i].contents
    if len(content_lst) == 1:
        names.append(str(texts[i].contents[0]))
    else:
        content = ""
        for element in content_lst:
            content += str(element)
        names.append(content)
    ratings.append(str(numbers[2*i].contents[0]))
    voters.append(str(numbers[2*i + 1].contents[0]))
    f.write(names[i] + "," + ratings[i] + "," + voters[i] + "\n")

# close the file
f.close()