import os

def removeFileProperties(document):
    if os.path.exists("converter/DataStorage/"  + document + "EPW-batch.morph.properties"):
        os.remove("converter/DataStorage/"  + document + "EPW-batch.morph.properties")
        return
    else:
        return



def createFileProperties(document):
    documentCTD=open("converter/DataStorage/" + document + "_EPW-batch.morph.properties", "a+")
    propertiesFile = document + "_EPW-batch.morph.properties"

    documentCTD.write("""mappingdocument.file.path=DataStorage/"""+ document +"""_EPW.r2rml.ttl
output.file.path=DataStorage/""" + document + """_EPW-batch-result-csv.nt
output.rdflanguage=N-TRIPLE
csv.file.path = DataStorage/""" + document + """.csv
no_of_database=1
database.name[0]=morphcsv
database.driver[0]=org.h2.Driver
database.url[0]=jdbc:h2:mem:morphcsv
database.user[0]=sa
database.pwd[0]=
database.type[0]=CSV""")

    documentCTD.close()

    return propertiesFile