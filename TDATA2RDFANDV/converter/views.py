from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


# TAKE DATA FUNCTIONS

from converter.Functions.takeDataJson import takeData



def index(request):
	return render(request,'converter/page.html')



@csrf_exempt
def mapData(request):
	if request.method == "POST":
		response = json.loads(request.body)
		data = takeData(response)
		print(data)
		return
