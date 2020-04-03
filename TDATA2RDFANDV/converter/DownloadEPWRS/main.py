from converter.DownloadEPWRS.createEPWFile import createEPWFile
from converter.DownloadEPWRS.EnergyPlusScraper import continentGetLink, scrapeEP
from converter.DownloadEPWRS.getDate import getDate
from converter.DownloadEPWRS.jsonReader import jsonReader
from converter.DownloadEPWRS.OneBuildingScraper import continentLink,scrapeOB
import os
import shutil



data = {
        "city" : "Madrid",
        "country" : "Spain",
        "continent" : "Europe",
        "year" : 1984,
        "source" : "EnergyPlus"
        }

def main(data):

    if not os.path.exists('converter/DownloadEPWRS/tmpFiles'):
        os.mkdir('converter/DownloadEPWRS/tmpFiles')
    else:    
        shutil.rmtree('converter/DownloadEPWRS/tmpFiles')
        os.mkdir('converter/DownloadEPWRS/tmpFiles')

    city, country, continent, year, source = jsonReader(data)

    if source == "EnergyPlus":
        continentLink = continentGetLink(continent)
        epwLinkList = scrapeEP(city,country,continentLink)

        createEPWFile(epwLinkList)

        finalDateList, returnEPWListFiles = getDate(year)

        if returnEPWListFiles != []:
            return returnEPWListFiles
        else:
            return finalDateList

    elif source == "OneBuilding":
        return

    else:
        return

main(data)