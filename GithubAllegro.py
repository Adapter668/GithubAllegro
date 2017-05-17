from bs4 import BeautifulSoup
import urllib.request
import re

def searchLastMadifiedRepo():
    htmlPage = urllib.request.urlopen("https://github.com/allegro")
    soup = BeautifulSoup(htmlPage, "html.parser")
    listOfLinks = list()
    names = list()
    for link in soup.find_all('a', attrs={'href': re.compile("^/allegro/")}):
        listOfLinks.append(link.get('href'))

    for link in listOfLinks:
        name = link[9:]
        names.append(name)
        i = listOfLinks.index(link)
        link = "https://github.com" + link
        listOfLinks[i] = link

    print(names[0])
    print(listOfLinks[0])
    return names[0]

searchLastMadifiedRepo()
