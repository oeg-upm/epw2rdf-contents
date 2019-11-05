import json
from makeMetadata import removeFileJSON
import os

with open("../static/converter/taxonomyCities.json") as f:
    data = json.load(f)
    codes = [city['adm0_a3'] for city in data['cities']]
    codesNoDuplicates = list(dict.fromkeys(codes))
    # print(codesNoDuplicates)

f.close()

def removeFileJSON():
    if os.path.exists("../static/converter/oneBuilding.json"):
        os.remove("../static/converter/oneBuilding.json")
        return
    else:
        return

removeFileJSON()

trueData=open("../static/converter/oneBuilding.json", "a+")

trueData.write("""{
    "type": "FeatureCollection",
    "features": []
    }
""")
trueData.close()


with open('data.json') as f:
        data = json.load(f)


with open('../static/converter/oneBuilding.json') as g:
    dataset = json.load(g)


[dataset['features'].append(feature) for feature in data['features'] if feature['properties']['adm0_a3'] in codesNoDuplicates]

f.close()

with open('../static/converter/oneBuilding.json', 'w') as g:
    json.dump(dataset, g, indent=4)


g.close()