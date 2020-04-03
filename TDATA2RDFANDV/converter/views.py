from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import shutil
import pathlib
import glob, os
from os import listdir
from os.path import isfile, join


# Create your views here.


# TAKE DATA FUNCTIONS

from converter.Functions.takeDataJson import takeData # take data from json['code']
from converter.Functions.extractFile import extractEPWFile # extract the epw file from url zip
from converter.Functions.makeCSVW import removeFileJSON, createFileJson # make metadata
from converter.Functions.getDataFromJson import getJsonData # get json from created csvw
from converter.Functions.parse2CSV import parseToCSV # parse epw file to csv
from converter.Functions.makePropertiesFile import createFileProperties, removeFileProperties # create file properties
from converter.Functions.makeTTLFile import createFileTTL, removeFileTTL # create R2RML file
from converter.Functions.makeSH import makeSH
from converter.Functions.createEPWFile import removeFileEPW, createEPW
from converter.DownloadEPWRS.main import main
from converter.DownloadEPWRS.zipdir import zipdir
# directory to storage data == DataStorage



def index(request):
	return render(request,'converter/page.html')



@csrf_exempt # ONEBUILDIND.ORG WEATHER MAP
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

@csrf_exempt # ENERGY PLUS WEATHER MAP
def mapDataEnergyPlus(request):
	if request.method == "POST":
		response = json.loads(request.body)
		data = takeData(response)
		with open('converter/static/converter/taxonomyCitiesEPlus.json') as jsonFile:
			jsonData = json.load(jsonFile)
			# print(jsonData)
			
		jsonDictionary = {'cities':[]}

		[jsonDictionary['cities'].append({'adm0_a3':city['adm0_a3'],'link':city['link']}) for city in jsonData['cities'] if city['adm0_a3']==data]

		jsonFile.close()
		#print(jsonDictionary)

		return JsonResponse(jsonDictionary,safe=False)

@csrf_exempt # EXTRACT DATA FROM LINK FROM ONEBUILDING.ORG WEATHER
def extract_Convert(request):
	if request.method == "POST":
		if not os.getcwd().endswith("DataStorage"):
			shutil.rmtree('converter/DataStorage/', ignore_errors=True)
			pathlib.Path("converter/DataStorage").mkdir(parents=True, exist_ok=True)
			for file in glob.glob("converter/static/converter/*.nt"):
				os.remove(file)
			for file in glob.glob("converter/static/converter/*.epw"):
				os.remove(file)

		else:
			shutil.rmtree('../../converter/DataStorage/', ignore_errors=True)
			pathlib.Path("../DataStorage").mkdir(parents=True, exist_ok=True)
			os.chdir("../../../../epw2rdf-contents/TDATA2RDFANDV")
			for file in glob.glob("converter/static/converter/*.nt"):
				os.remove(file)
			for file in glob.glob("converter/static/converter/*.epw"):
				os.remove(file)

		

		response = json.loads(request.body)
		link = takeData(response)
		data = extractEPWFile(link) # get data from EPW file that is inside Zip File
		removeFileJSON()
		city = createFileJson(data)
		headers,numberRowstoSkip = getJsonData(city)
		
		headers = str(str(headers).strip('[]').replace("'","").split(', ')).strip('[]').replace(", ",",")
		
		headers = str(headers).strip('[]').replace("'","").replace(", ",",")
		# print(headers)

		parseToCSV(data, numberRowstoSkip, headers, city) # parse data to csv

		# removeFileProperties(city)
		propertiesFile = createFileProperties(city)

		# removeFileTTL(city)
		createFileTTL(city)

		createEPW(data,city)

		# print(propertiesFile)

		

		# makeSH(propertiesFile)

		if not os.getcwd().endswith("DataStorage"):
			os.chdir("converter/DataStorage")

		for file in glob.glob("*.nt"):
			for epw in glob.glob("*.epw"):
				dictionary = {
					'EPW': "static/converter/" + epw,
					'RDF': "static/converter/" + file
				}
				data = file
				data2 = epw
		shutil.move(data, '../../converter/static/converter/')
		shutil.move(epw, '../../converter/static/converter/')

		return JsonResponse(dictionary,safe=False)

@csrf_exempt
def extract_ConvertEnergyPlus(request):
	if request.method == "POST":
		return

@csrf_exempt
def downloadEPW(request):
	if request.method == "POST":
		response = json.loads(request.POST['data'])
		# return HttpResponse(file, content_type='application/zip')
		resultList = main(response)
		print(resultList)
		if resultList[0].endswith('.epw'):
			onlyfiles = [f for f in listdir('converter/DownloadEPWRS/tmpFiles') if isfile(join('converter/DownloadEPWRS/tmpFiles/', f))]
			#return HttpResponse(file, content_type='application/zip')
			print('1',onlyfiles)
			os.mkdir('converter/DownloadEPWRS/tmpFiles/EPW')
			for result in resultList:
				shutil.move("converter/DownloadEPWRS/tmpFiles/"+result, "converter/DownloadEPWRS/tmpFiles/EPW/"+result)
				zipdir("converter/DownloadEPWRS/tmpFiles/EPW/","converter/DownloadEPWRS/tmpFiles/EPW.zip",True)
				return HttpResponse("converter/DownloadEPWRS/tmpFiles/EPW.zip", content_type='application/zip')
		else:
			resultList = ','.join(resultList)
			dictionary = {
				'info' : 'Your year does not coincide with any of the years established within the epw files, please select one of the following',
				'years' : resultList
			}
			return JsonResponse(dictionary,safe=False)