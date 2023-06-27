from django.shortcuts import render
from django.http import HttpResponse
import eve.customerFunctions as cf
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def trackride(request):
    uid = request.GET.get('id')
    
    ride = cf.checkOngoingRides(uid)
    context = {'id': uid, 'lat': ride[3], 'lon': ride[4]}
    return render(request, "trackrideshare.html", context)

@csrf_exempt
def getloc(request):
    uid = request.POST.get('id')
    
    ride = cf.getCurLoc(uid)
    context = {'id': uid, 'lat': ride[3], 'lon': ride[4]}
    
    
    return HttpResponse(json.dumps(context),content_type="application/json")