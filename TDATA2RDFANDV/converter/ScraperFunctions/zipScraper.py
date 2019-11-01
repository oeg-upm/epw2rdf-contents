import zipfile, urllib, os
from urllib.request import Request,urlopen, urlretrieve
from io import BytesIO

from bs4 import BeautifulSoup
import requests
import urllib.request
import time

from climateContinents import getContinentsURL


# COGEMOS LAS URLs DE LOS CONTINENTES

africaURL, asiaURL, south_AmericaURL, north_central_AmericaURL, southWest_PacificURL, europeURL, antarticaURL = getContinentsURL()

# AKGNDSG

responseCountries = requests.get(africaURL, timeout=10)
countries = BeautifulSoup(responseCountries.content,"html.parser")

lista = []

for country in countries.find_all('a', attrs={"href": "".endswith('/index.html')}, href=True):
    countryLink = country['href']
    if not str(countryLink).startswith('../') and not str(countryLink).startswith('default.html'):
        lista.append(countryLink)


print(lista)

# PARTE PERTENECIENTE AL ACCESO DEL ZIP Y LA EXTRACCIÓN DE DATOS

# resp = urlopen('http://climate.onebuilding.org/WMO_Region_6_Europe/ESP_Spain/AN_Andalusia/ESP_AN_Malaga.AP.084820_TMYx.2003-2017.zip')
# zipfile = zipfile.ZipFile(BytesIO(resp.read()))
# file = zipfile.namelist()[2]

# epwFile = [file for file in zipfile.namelist() if file.endswith('.epw')]

# file = epwFile[0]

# print(file)


# data = zipfile.open(file).readlines()
# print(data)

# FIN PARTE PERTENECIENTE AL ACCESO DEL ZIP Y LA EXTRACCIÓN DE DATOS








