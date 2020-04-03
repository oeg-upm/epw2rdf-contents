import os

def removeFileEPW(data,city):
    if os.path.exists("converter/DataStorage/"  + city + "EPW-batch.morph.properties"):
        os.remove("converter/DataStorage/"  + city + "EPW-batch.morph.properties")
        return
    else:
        return


def createEPW(data,city):
    documentCTD=open("converter/DataStorage/" + city + ".epw", "a+")
    for d in data:
        documentCTD.write(d)
    documentCTD.close()
    