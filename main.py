import requests
import re
import yaml
from bs4 import BeautifulSoup

class Iso:
    def __init__(self, name, url, version):
        self.name = name
        self.url = url
        self.version = version


def scrapeDate(distro):
    URL = distro.url
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, features='lxml')
    
    for link in soup.find_all('a'):
        if( 'magnet' in link.get('href')):
            matchDate = re.search(r'\d{4}.\d{2}.\d{2}', link.get('href'))
            matchDate = re.sub('\.', '', matchDate.group(0))
            return(matchDate)

#arch = Iso('archlinux', "https://archlinux.org/download/", 0)
#scrapeDate(arch)

with open("distros.yaml", mode="rt", encoding="utf-8") as file:
    data = yaml.safe_load(file)
    distros = []
    for item in data.items():
#        print(item[0]) # Name
#        print(list(item[1].values())[0]) # URL

        distros.append( Iso(item[0], list(item[1].values())[0], 0) )

    for distro in distros:
        print(scrapeDate(distro))
