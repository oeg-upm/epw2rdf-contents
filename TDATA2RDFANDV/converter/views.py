from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


# TAKE DATA FUNCTIONS

from converter.Functions.takeDataJson import takeData # take data from json['code']
from converter.Functions.extractFile import extractEPWFile # extract the epw file from url zip

# directory to storage data == DataStorage



def index(request):
	return render(request,'converter/page.html')



@csrf_exempt
def mapData(request):
	if request.method == "POST":
		response = json.loads(request.body)
		data = takeData(response)
		# print(data)
		with open('converter/static/converter/taxonomyCities.json') as jsonFile:
			jsonData = json.load(jsonFile)

		jsonDictionary ={'cities':[]}

		[jsonDictionary['cities'].append({'adm0_a3':city['adm0_a3'],'link':city['link']}) for city in jsonData['cities'] if city['adm0_a3']==data]

		jsonFile.close()

		# print(jsonDictionary)

		return JsonResponse(jsonDictionary,safe=False)

@csrf_exempt
def extract_Convert(request):
	if request.method == "POST":
		response = json.loads(request.body)
		link = takeData(response)
		data = extractEPWFile(link) # get data from EPW file that is inside Zip File
		return HttpResponse(data)