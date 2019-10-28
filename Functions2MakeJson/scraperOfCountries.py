from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import os




countriesList = []


urlContinents = "https://energyplus.net/weather"
responseContinents = requests.get(urlContinents,timeout=10)
continent = BeautifulSoup(responseContinents.content, "html.parser")


# Primer for para continentes

for continent in continent.find_all('a', attrs={"class": "btn btn-default left-justify blue-btn"}, href=True):
    continentLink = continent['href']
    # print ("Found the URL of continent:", continentLink)
    
    urlCountries = "https://energyplus.net" + continentLink
    # print(urlCountries)
    responseCountries = requests.get(urlCountries,timeout=10)
    countries = BeautifulSoup(responseCountries.content,"html.parser")

    # Segundo for para paises

    for country in countries.find_all('a', attrs={"class": "btn btn-default left-justify blue-btn"}, href=True):
        countryLink = country['href']
        countryText = country.find_all(text=True)
        countryText = countryText[0].split(" - ")
        countryText = countryText[1]
        countriesList.append(countryText)






print(countriesList)