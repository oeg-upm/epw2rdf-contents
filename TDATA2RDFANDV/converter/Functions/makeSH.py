import os

def makeSHEPW(name): # CHANGE
    if os.getcwd().endswith("DataStorage"):
        command = "cd ../Helio \n java -jar helio.jar -p '../MappingsEPWStorage' -o '../Results/"+ name + ".nt'"
    else:
        command = "cd converter/Helio \n java -jar helio.jar -p '../MappingsEPWStorage' -o '../Results/"+ name + ".nt'"

    os.system(command)

def makeSHJSON(name): # CHANGE
    if os.getcwd().endswith("DataStorage"):
        command = "cd ../Helio \n java -jar helio.jar -p '../MappingsDSAPIStorage' -o '../Results/"+ name + ".nt'"
    else:
        command = "cd converter/Helio \n java -jar helio.jar -p '../MappingsDSAPIStorage' -o '../Results/"+ name + ".nt'"

    os.system(command)