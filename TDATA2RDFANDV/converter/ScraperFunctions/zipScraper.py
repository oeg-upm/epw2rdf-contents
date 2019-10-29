import zipfile, urllib, os
from urllib.request import Request,urlopen, urlretrieve
from io import BytesIO

resp = urlopen('http://climate.onebuilding.org/WMO_Region_6_Europe/ESP_Spain/AN_Andalusia/ESP_AN_Malaga.AP.084820_TMYx.2003-2017.zip')
zipfile = zipfile.ZipFile(BytesIO(resp.read()))
file = zipfile.namelist()[2]

epwFile = [file for file in zipfile.namelist() if file.endswith('.epw')]

file = epwFile[0]

print(file)


data = zipfile.open(file).readlines()
print(data)

