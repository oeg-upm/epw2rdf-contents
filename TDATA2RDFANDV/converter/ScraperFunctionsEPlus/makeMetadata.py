
import os
import json




def removeFileJSON():
    if os.path.exists("../static/converter/taxonomyCitiesEPlus.json"):
        os.remove("../static/converter/taxonomyCitiesEPlus.json")
        return
    else:
        return


def createFileJSON(link,countryCode):

    a_dict = {
    "link": link,
    "adm0_a3": countryCode
    }

    with open("../static/converter/taxonomyCitiesEPlus.json") as f:
        data = json.load(f)

    data['cities'].append(a_dict)

    with open("../static/converter/taxonomyCitiesEPlus.json", 'w') as f:
        json.dump(data, f, indent=4)
