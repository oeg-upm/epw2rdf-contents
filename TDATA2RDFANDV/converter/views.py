from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
import json
import shutil
import pathlib
import glob, os
from os import listdir
from os.path import isfile, join

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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

		

		makeSH(propertiesFile)

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





from .models import downlEPW
import coreapi
from rest_framework.schemas import AutoSchema



@swagger_auto_schema(
	method='POST',
	operation_description="Obtain EPW files from one specific year.",
	request_body=openapi.Schema(
		type=openapi.TYPE_OBJECT,
		properties={
				'city': openapi.Schema(type=openapi.TYPE_STRING,example="Madrid"),
				'country': openapi.Schema(type=openapi.TYPE_STRING,example="Spain"),
				'continent':openapi.Schema(type=openapi.TYPE_STRING,example="Europe"),
				'year':openapi.Schema(type=openapi.TYPE_INTEGER,example="1989"),
				'source':openapi.Schema(type=openapi.TYPE_STRING,example="EnergyPlus or OneBuilding"),
				'output':openapi.Schema(type=openapi.TYPE_STRING,example="file or link"),
		}
	),
	responses={
		200:openapi.Schema(
			type=openapi.TYPE_OBJECT,
			description="If the year is in the EPW files, the response will be a zip file (if you want to download this file you have to do the curl call with an external terminal writing at the end --output 'EPW.zip'). If the year is not in the EPW files, the response will be a json with the years that these files contain, as below you can see:",
			properties={
				'info': openapi.Schema(type=openapi.TYPE_STRING,example="Your year does not coincide with any of the years established within the epw files, please select one of the following"),
				'years': openapi.Schema(type=openapi.TYPE_STRING,example="1985,1986,1987,1989,1990,1991,1993,1994,1999"),
			},
		),
	}
)


@api_view(['POST'])
@csrf_exempt
def downloadEPW(request):
	if request.method == "POST":
		response = request.data
		resultList = main(response)
		if resultList[0].endswith('.epw') and not resultList[0].startswith("http"):
			onlyfiles = [f for f in listdir('converter/DownloadEPWRS/tmpFiles') if isfile(join('converter/DownloadEPWRS/tmpFiles/', f))]
			os.mkdir('converter/DownloadEPWRS/tmpFiles/EPW')
			for result in resultList:
				shutil.move("converter/DownloadEPWRS/tmpFiles/"+result, "converter/DownloadEPWRS/tmpFiles/EPW/"+result)
			zipdir("converter/DownloadEPWRS/tmpFiles/EPW/","converter/DownloadEPWRS/tmpFiles/EPW.zip",True)
			zip_file = open("converter/DownloadEPWRS/tmpFiles/EPW.zip",'rb')
			return FileResponse(zip_file)
		
		elif resultList[0].startswith("http"):
			resultList = ','.join(resultList)
			dictionary = {
				'info' : 'The links of the epw files that you have requested are as follows:',
				'links' : resultList
			}
			return JsonResponse(dictionary,safe=False)

		else:
			resultList = ','.join(resultList)
			dictionary = {
				'info' : 'Your year does not coincide with any of the years established within the epw files, please select one of the following',
				'years' : resultList
			}
			
			return JsonResponse(dictionary, safe=False)


@swagger_auto_schema(
	method='POST',
	operation_description=" Obtain the years contained in the EPW documents belonging to the city indicated.",
	request_body=openapi.Schema(
		type=openapi.TYPE_OBJECT, 
		properties={
				'city': openapi.Schema(type=openapi.TYPE_STRING,example="Madrid"),
				'country': openapi.Schema(type=openapi.TYPE_STRING,example="Spain"),
				'continent':openapi.Schema(type=openapi.TYPE_STRING,example="Europe"),
				'source':openapi.Schema(type=openapi.TYPE_STRING,example="EnergyPlus or OneBuilding"),
		}
	),
	responses={
		200:openapi.Schema(
			type=openapi.TYPE_OBJECT,
			properties={
				'years': openapi.Schema(type=openapi.TYPE_STRING,example="1985,1986,1987,1989,1990,1991,1993,1994,1999"),
			},
		),
	}
)

@api_view(['POST'])
@csrf_exempt
def getEPWYears(request):
	if request.method == "POST":
		response = request.data
		resultList = mainYear(response)
		resultList = ','.join(resultList)
		dictionary = {
			'years' : resultList
		}
		return JsonResponse(dictionary,safe=False,)
