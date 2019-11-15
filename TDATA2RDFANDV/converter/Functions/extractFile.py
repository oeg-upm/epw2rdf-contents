
import zipfile, urllib, os
from urllib.request import Request,urlopen, urlretrieve
from io import BytesIO


def extractEPWFile(url):

    resp = urlopen(url)
    zipfiles = zipfile.ZipFile(BytesIO(resp.read()))
    file = zipfiles.namelist()[2]

    epwFile = [file for file in zipfiles.namelist() if file.endswith('.epw')]

    file = epwFile[0]

    data = zipfiles.open(file).readlines() # Información perteneciente al archivo EPW
    return data