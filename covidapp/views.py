from django.shortcuts import render
import requests
import json
# Create your views here.


def index(request):
 # api_request = requests.get('https://mazitekgh.com/covid19/v1/')
  ghana_request = requests.get('https://corona.lmao.ninja/v2/countries/Ghana')
  ghana = json.loads(ghana_request.content)
  
  
  api_request = requests.get('https://corona.lmao.ninja/v2/countries?sort=country')
  api = json.loads(api_request.content)
  
  
  context = {'api':api,'ghana':ghana}
  return render(request,'index.html',context)