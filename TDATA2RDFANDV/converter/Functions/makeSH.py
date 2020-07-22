import os

def makeSHEPW(name): # CHANGE
    if os.getcwd().endswith("DataStorage"):
        command = "cd ../RMLMapper \n java -jar rmlmapper-4.8.1.jar -m '../MappingsEPWStorage/mapping.rml' -o '../Results/" + name + ".ttl'"
        #command2 = "cd ../Results \n split -l 200000 " + name + ".nt -s 'turtle'"
        #  \n rm -f " + name + ".nt"
    else:
        command = "cd converter/RMLMapper \n java -jar rmlmapper-4.8.1.jar -m '../MappingsEPWStorage/mapping.rml' -o '../Results/" + name + ".ttl' -s 'turtle'"
        #command2 = "cd converter/Results \n split -l 200000 " + name + ".ttl"
        # \n rm -f " + name + ".nt"

    os.system(command)
    #os.system(command2)





def makeSHJSON(name): # CHANGE
    if os.getcwd().endswith("DSAPIDataStorage"):
        command = "cd ../Helio \n java -jar helio.jar -p '../MappingsDSAPIStorage' -o '../Results/" + name + ".ttl' -s 'turtle'"
    else:
        command = "cd converter/Helio \n java -jar helio.jar -p '../MappingsDSAPIStorage' -o '../Results/" + name + ".ttl' -s 'turtle'"

    os.system(command)