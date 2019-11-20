import os

def makeSH(propertiesFile):
    if os.getcwd().endswith("DataStorage"):
        command = "cd ../MorphRDB \n java -cp .:morph-rdb.jar:dependency/* es.upm.fi.dia.oeg.morph.r2rml.rdb.engine.MorphCSVRunner .. DataStorage/" + propertiesFile + ""
    else:
        command = "cd converter/MorphRDB \n java -cp .:morph-rdb.jar:dependency/* es.upm.fi.dia.oeg.morph.r2rml.rdb.engine.MorphCSVRunner .. DataStorage/" + propertiesFile + ""
    os.system(command)