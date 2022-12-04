import requests
import re
import yaml
import os
from torrentp import TorrentDownloader

from bs4 import BeautifulSoup

class Iso:
    def __init__(self, name, url, version, magnet):
        self.name = name
        self.url = url
        self.version = version
        self.magnet = magnet


def scrapeDateAndMagnet(distro):
    page = requests.get(distro.url)
    soup = BeautifulSoup(page.content, features='lxml')
    
    for link in soup.find_all('a'):
        if('magnet' in link.get('href')):
            distro.magnet = link.get('href')

            distro.version = re.search(r'\d{4}\.\d{2}\.\d{2}', link.get('href'))
            distro.version = re.sub('\.', '', distro.version.group(0))
    
    if distro.magnet == None:
        return 0
    
    else:
        return 1

def downloadDistro(magnetLink):
    torrent_file = TorrentDownloader("magnetLink", '.')
    torrent_file.start_download()

def findFile(fileName):
    for i in os.listdir():
        if fileName in i: 
            return i

def findFileVersion(fileName):
    fileVersion = re.search(r'\d{4}.\d{2}.\d{2}', fileName)
    fileVersion = re.sub('\.', '', fileVersion.group(0))
    return fileVersion

#def compareVersions(distroName):
def checkFile(distroName):
    isoInFolder = findFile(distroName)
    if None == isoInFolder:
        return 0
    else:
        return 1

with open("distros.yaml", mode="rt", encoding="utf-8") as file:
    data = yaml.safe_load(file)
    distros = []
    for item in data.items():
        distros.append(Iso(item[0], list(item[1].values())[0], None, None))

    for distro in distros:

        if (scrapeDateAndMagnet(distro) & checkFile(distro.name)):
            print('a')

#        if (checkFile(distro.name)):
#            file = Iso
#            file.name = checkFile(distro.name)
#            file.version = findFileVersion(file.name)
#        else:




