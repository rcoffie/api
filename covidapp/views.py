from django.shortcuts import render
import requests
import json
# Create your views here.


def index(request):
  api_request = requests.get('https://api.covid19api.com/summary')
  api = json.loads(api_request.content)
  context = {'api':api}
  return render(request,'index.html',context)