
import csv
import json
import pycountry


def create8LinesJson(data,numberRowstoSkip,epwName):

    json_file = {}

    json_lines = data[:numberRowstoSkip-1]

    first_line = json_lines[0].split(',') # First line ["StartOfLine","city","CityAcronym","adm03","Source","wmo","lat","long","TimeZone","alt"]
    third_line = json_lines[2].split(',') # Third line
    forth_line = json_lines[3].split(',') # Forth Line

    country_name = getCountryName(first_line[3])

    json_location = [first_line[1], country_name, first_line[3], first_line[5], first_line[6], first_line[7], first_line[9], epwName]

    json_periods  = getPeriods(third_line)

    json_ground = getGroundTemperatures(forth_line)

    json_file['location'] = []
    json_file['location'].append({
            "city":json_location[0],
            "country":json_location[1],
            "adm03":json_location[2],
            "wmo":int(json_location[3]),
            "lat":float(json_location[4]),
            "long":float(json_location[5]),
            "alt":float(json_location[6]),
            "epwName":json_location[7]
        })
        
    json_file['typical_extremePeriods'] = []

    for period in json_periods:
        json_file['typical_extremePeriods'].append({
            "typeOfPeriod":period[0],
            "firstDate":period[1].replace("\n","").replace("\r","").replace(" ",""),
            "lastDate":period[2].replace("\n","").replace("\r","").replace(" ",""),
            "season":period[3],
            "city":json_location[0],
            "adm03":json_location[2],
            "wmo":int(json_location[3]),
            "epwName":json_location[7]
        })
  
    json_file['groundTemperatures'] = []

    for elem in json_ground:
        json_file['groundTemperatures'].append({
            "groundTemperatureDepth":elem[0],
            "groundConductivity":elem[1],
            "groundDensity":elem[2],
            "groundSpecificHeat":elem[3],
            "january":elem[4],
            "february":elem[5],
            "march":elem[6],
            "april":elem[7],
            "may":elem[8],
            "june":elem[9],
            "july":elem[10],
            "august":elem[11],
            "september":elem[12],
            "october":elem[13],
            "november":elem[14],
            "december":elem[15]
        })


    # Data of CSV

    epwData = data[numberRowstoSkip:]
    epwDataTransformed = []
    for row in epwData:
        row = row.split(",")
        epwDataTransformed.append([row[0], row[1], row[2], row[3], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[29], row[30], row[31], row[32], row[33], row[34], json_location[0], json_location[2], json_location[3], json_location[7]])

    json_file['epw'] = []


    for epw in epwDataTransformed:
        count = 0
        while count < len(epw):
            epw[count].replace("\n","").replace("\r","")
            count+=1


        json_file['epw'].append({
          "Year": int(epw[0]),
          "Month": int(epw[1]),
          "Day": int(epw[2]),
          "Hour": int(epw[3]),
          "DryBulbTemperature": float(epw[4]),
          "DewPointTemperature": float(epw[5]),
          "RelativeHumidity": float(epw[6]),
          "AtmosphericStationPressure": float(epw[7]),
          "ExtraterrestrialHorizontalRadiation": float(epw[8]),
          "ExtraterrestrialDirectNormalRadiation": float(epw[9]),
          "HorizontalInfraredRadiationIntensity": float(epw[10]),
          "GlobalHorizontalRadiation": float(epw[11]),
          "DirectNormalRadiation": float(epw[12]),
          "DiffuseHorizontalRadiation": float(epw[13]),
          "GlobalHorizontalIlluminance": float(epw[14]),
          "DirectNormalIlluminance": float(epw[15]),
          "DiffuseHorizontalIlluminance": float(epw[16]),
          "ZenithLuminance": float(epw[17]),
          "WindDirection": float(epw[18]),
          "WindSpeed": float(epw[19]),
          "TotalSkyCover": float(epw[20]),
          "OpaqueSkyCover": float(epw[21]),
          "Visibility": float(epw[22]),
          "CeilingHeight": float(epw[23]),
          "PrecipitableWater": float(epw[24]),
          "AerosolOpticalDepth": float(epw[25]),
          "SnowDepth": float(epw[26]),
          "DaysSinceLastSnowfall": float(epw[27]),
          "Albedo": float(epw[28]),
          "LiquidPrecipitationDepth": float(epw[29]),
          "LiquidPrecipitationQuantity": float(epw[30]),
          "city" : epw[31],
          "adm03" : epw[32],
          "wmo" : int(epw[33]),
          "epwName" : epw[34]
        })


        
    
    document = open("converter/DataStorage/" + epwName + ".json", "w")
    json.dump(json_file, document, indent=4)

    document.close()
    


def getCountryName(code):
    country = pycountry.countries.get(alpha_3=code)
    country_name = country.name
    return country_name

def getPeriods(data):

    data.pop(0) # Remove first and second item
    data.pop(0) # Remove first and second item

    lists = [data[x:x+4] for x in range(0, len(data), 4)]

    for l in lists:
        season = l[0].split(' ')[0]
        l.pop(0)
        

        if l[0] == "Extreme":
            l.pop(0)
            l.append("ExtremeWeatherPeriodMeasurement")
        elif l[0] == "Typical":
            l.pop(0)
            l.append("TypicalWeatherPeriodMeasurement")

        firstDate = l[0]
        lastDate = l[1]

        l.pop(0)
        l.pop(0)

        l.append(firstDate)
        l.append(lastDate)
        l.append(season)
        
    return lists


def getGroundTemperatures(data):
    
    data.pop(0) # Remove first and second item
    data.pop(0) # Remove first and second item

    lists = [data[x:x+16] for x in range(0, len(data), 16)]

    for elem in lists:
        count = 0
        while count < len(elem):
            if elem[count] == "":
                count+=1
            elif elem[count].startswith("."):
                elem[count] = float("0"+elem[count])
                count+=1
            else:
                elem[count] = float(elem[count])
                count+=1
    
    return lists
