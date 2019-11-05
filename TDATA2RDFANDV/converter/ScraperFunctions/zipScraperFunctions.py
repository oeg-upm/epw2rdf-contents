import zipfile, urllib, os
from urllib.request import Request,urlopen, urlretrieve
from io import BytesIO

from bs4 import BeautifulSoup
import requests
import urllib.request
import time


def scraperZip(url, searchData):
    resultList = [] # Lista donde se va a almacenar los resultados
    response = requests.get(url, timeout=10)
    elements = BeautifulSoup(response.content,"html.parser")

    for element in elements.find_all('a', attrs={"href":""}, href=True):
        elementLink = element['href']
        if str(elementLink).endswith(searchData):
            if str(elementLink).startswith("..\\"):
                elementLink = '/'.join(elementLink.split('/')[1:]) # Quitar ..\
                # print(elementLink)
            if str(elementLink).endswith('/index.html'):
                elementLink = elementLink.replace('/index.html','/')
            resultList.append(url + elementLink)
    return resultList



def extractEPWFile(url):

    resp = urlopen(url)
    zipfiles = zipfile.ZipFile(BytesIO(resp.read()))
    file = zipfiles.namelist()[2]

    epwFile = [file for file in zipfiles.namelist() if file.endswith('.epw')]

    file = epwFile[0]

    data = zipfiles.open(file).readlines() # Información perteneciente al archivo EPW


def getCountryCode(city):
    countryCode = city.split('/')[-1][:3]
    if countryCode.endswith('_'):
        countryCode = countryCode[:2] # Mirar el caso en el que se necesite el "_":
    return countryCode




    