import json

data = {
        "city" : "Madrid",
        "country" : "Spain",
        "continent" : "Europe",
        "year" : 1984,
        "source" : "EnergyPlus"
        }

def jsonReader(data):
    city = data["city"]
    country = data["country"]
    continent = data["continent"]
    year = data["year"]
    source = data["source"]
    return city, country, continent, year, source
    

#city, country, continent, year, source = jsonReader(data)
