import os


def createEPW(data,epwName):
    documentCTD=open("converter/DataStorage/" + epwName + ".epw", "a+")
    for d in data:
        documentCTD.write(d)
    documentCTD.close()
    