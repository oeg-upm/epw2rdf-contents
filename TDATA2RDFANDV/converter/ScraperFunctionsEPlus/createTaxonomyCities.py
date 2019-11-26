from urllib.request import Request,urlopen, urlretrieve
from io import BytesIO

from bs4 import BeautifulSoup
import requests
import urllib.request
import time

from makeMetadata import removeFileJSON,createFileJSON

removeFileJSON()



removeFileJSON()

documentJSON=open("../static/converter/taxonomyCitiesEPlus.json", "a+")

documentJSON.write("""{
"cities":[]
}
""")

documentJSON.close()



urlContinents = "https://energyplus.net/weather"
responseContinents = requests.get(urlContinents,timeout=10)
continent = BeautifulSoup(responseContinents.content, "html.parser")

# Primer for para continentes

resultList = []

for continent in continent.find_all('a', attrs={"class": "btn btn-default left-justify blue-btn"}, href=True):
    continentLink = continent['href']
    # print ("Found the URL of continent:", continentLink)
    
    urlCountries = "https://energyplus.net" + continentLink
    responseCountries = requests.get(urlCountries,timeout=10)
    countries = BeautifulSoup(responseCountries.content,"html.parser")

    # Segundo for para paises

    for country in countries.find_all('a', attrs={"class": "btn btn-default left-justify blue-btn"}, href=True):
        countryLink = country['href']
        #print("Found the URL of country:",countryLink)
        # Aquí obtengo los links pertenecientes a los países, que a su vez son pertenecientes a cada continente
        urlCities = "https://energyplus.net" + countryLink
        responseCities = requests.get(urlCities,timeout=10)
        cities = BeautifulSoup(responseCities.content,"html.parser")

        for city in cities.find_all('a', attrs={"class": "btn btn-default left-justify blue-btn"}, href=True):
            cityLink = city['href']
            #print("Found the URL of city:",cityLink)

            urlDownloadEPW = "https://energyplus.net" + cityLink
            responseDownloadEPW = requests.get(urlDownloadEPW,timeout=10)
            downloads = BeautifulSoup(responseDownloadEPW.content,"html.parser")

            #Cuarto for para descargas

            for download in downloads.find_all('a', attrs={"class": "btn btn-default left-justify blue-btn"}, href=True):
                downloadLink = download['href']

                if download.text == 'epw':
                    adm0_a3 = downloadLink.split('/')[3]
                    downloadLink = "https://energyplus.net" + downloadLink
                    # print("adm0_a3:",adm0_a3)
                    # print("Download Link:", downloadLink)
                    result = [adm0_a3,downloadLink]
                    resultList.append(result)

print(resultList[0])

tamaño = (int(len(resultList)/2))

resultList1 = resultList[:tamaño]
resultList2 = resultList[tamaño:]

print("Se empieza a generar el fichero JSON")
[createFileJSON(res[0],res[1]) for res in resultList1]
print("Primera parte completada")
[createFileJSON(res[0],res[1]) for res in resultList2]
print("Segunda parte completada y fin de ejecución")