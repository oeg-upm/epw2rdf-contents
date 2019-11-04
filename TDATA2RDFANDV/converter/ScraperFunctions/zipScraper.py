import zipfile, urllib, os
from urllib.request import Request,urlopen, urlretrieve
from io import BytesIO

from bs4 import BeautifulSoup
import requests
import urllib.request
import time

from climateContinents import getContinentsURL
from zipScraperFunctions import scraperZip, extractEPWFile, getCountryCode


# COGEMOS LAS URLs DE LOS CONTINENTES

africaURL, asiaURL, south_AmericaURL, north_central_AmericaURL, southWest_PacificURL, europeURL, antarticaURL = getContinentsURL()

# AKGNDSG

urls = [africaURL, asiaURL, south_AmericaURL, north_central_AmericaURL, southWest_PacificURL, europeURL, antarticaURL]

# urls = [0=Africa,1=Asia,2=Sudamérica,3=Norte-Centroamérica,4=Sudoeste del Pacífico,5=Europa,6=Antartica]


allCountries = [scraperZip(url,'/index.html') for url in urls] # Lista con todos los Países del Mundo


allCountryCodes = [getCountryCode(country) for countries in allCountries for country in countries] # Lista con todos los Códigos de los países del mundo HABRÁ QUE QUITARLA PORQUE SE COGERAN DE LAS CIUDADESS

allCountries = [country for countries in allCountries for country in countries]

# [print(country) for country in allCountries]

# AQUÍ YA TENEMOS UNA LISTA CON LOS PAISES Y OTRA LISTA CON LOS CÓDIGOS DE CADA PAÍS, TIENEN LAS MISMAS POSICIONES ENTRE ELLOS
allCities = []

# for country in allCountries:
#     listCountry = scraperZip(country,'.zip')
#     print(country)
#     allCities.append(listCountry)

[allCities.append(scraperZip(str(country),'.zip')) for country in allCountries]


# allCities = [scraperZip(str(country),'.zip') and print(country) for country in allCountries]


allCountries = [city for cities in allCities for city in cities]

print(allCities)


# url = urls[0] + firstCountry

# citiesList = scraperZip(url,'.zip')

# firstCity = citiesList[0]



#http://climate.onebuilding.org/WMO_Region_7_Antarctica/HMD_Heard_and_McDonald_Islands/

# lista = scraperZip('http://climate.onebuilding.org/WMO_Region_7_Antarctica/HMD_Heard_and_McDonald_Islands/','.zip')


# print(lista)





