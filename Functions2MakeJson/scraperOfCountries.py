from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import os
import re
import json

def removeFileJSON():
    if os.path.exists("Data/trueData.json"):
        os.remove("Data/trueData.json")
        return
    else:
        return

def scrapeData():
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
            #countryLink = country['href']
            countryText = country.find_all(text=True)
            countryText = countryText[0].split(" - ")
            countryText = countryText[0]
            countryText = re.sub(r'\([^()]*\)', '', countryText)
            countriesList.append(countryText)
    return countriesList


removeFileJSON()

trueData=open("Data/trueData.json", "a+")

trueData.write("""{
    "type": "FeatureCollection",
    "features": []
    }
""")
trueData.close()

countriesList = scrapeData()

print(countriesList)

with open('Data/data.json') as f:
        data = json.load(f)


with open('Data/trueData.json') as g:
    dataset = json.load(g)


[dataset['features'].append(feature) for feature in data['features'] if feature['properties']['adm0_a3'] in countriesList]

with open('Data/trueData.json', 'w') as g:
    json.dump(dataset, g, indent=4)