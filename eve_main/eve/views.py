from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import eve.loginFunctions as lf
import eve.customerFunctions as cf
import eve.operatorFunctions as mf
import eve.managerFunctions as m
import json
import io
import matplotlib.pyplot as plt
import base64, urllib
import eve.mailer as mailer

def index(request):
    return render(request, "index.html")

def transactions(request):
    
    uid = request.GET.get('id')
    transactions = cf.userTransactions(uid)
    
    context = {"transactions": transactions, "id":uid}
    
    return render(request, "transactions.html", context) 

def paydamages(request):
    
    uid = request.POST.get('uid')
    tid = request.POST.get('id')
    
    pending = cf.payDamages(uid, tid)
    if(pending):
        context = {'id': uid, "error": "insufficient balance. Please add {} to the wallet and pay the charges".format(pending)}
        return render(request, "addmoney.html",context)
        
    transactions = cf.userTransactions(uid)
    context = {"transactions": transactions, "id":uid, "message": "Damages Paid Successfully!!"}
    
    return render(request, "transactions.html", context) 

def contactus(request):
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    
    body = "{} with email id {}, has sent following message.\nsubject: {}\nmessage: {}".format(name,email,subject,message)
    subject = "Contact us form Request - EVE"
    
    mailer.sendmail("progsdproject@gmail.com", body, subject)
    
    body = "Hello {},\nWe have received your request and we will reach out to you soon. Thank you for checking out our services.\n\nTeam EVE LC02-LB01-A".format(name)
    
    mailer.sendmail(email, body, subject)
    
    context = {'message': "we will reach out to you soon!!"}
    return render(request, "index.html", context) 

def login(request):
    return render(request, "login.html") 

def register(request): 
    return render(request, "register.html") 

def addmoney(request):
    uid = request.GET.get('id')
    
    ride = cf.checkOngoingRides(uid)
    if(ride != None):
        context = {'rideid': ride[0], 'id': uid, 'vehid': ride[2], 'ststation': ride[7], 'endstation': ride[8], 'enddate': ride[6], 'hours': ride[9], 'lat': ride[3], 'lon': ride[4], 'price': ride[10]}
        return render(request, "onride.html", context)
    
    
    context = {'id': uid}
    return render(request, "addmoney.html",context)

def bookride(request):
    uid = request.GET.get('id')
    
    ride = cf.checkOngoingRides(uid)
    if(ride != None):
        context = {'rideid': ride[0], 'id': uid, 'vehid': ride[2], 'ststation': ride[7], 'endstation': ride[8], 'enddate': ride[6], 'hours': ride[9], 'lat': ride[3], 'lon': ride[4], 'price': ride[10]}
        return render(request, "onride.html", context)
    
    
    stations = cf.allStations()
    vehicles = list(cf.allVehicleID('1'))
    res = cf.getUserDetails(uid)
    
    if(res[10]=='2'):
        for i in range(len(vehicles)):
            vehicles[i] = list(vehicles[i])
    context = {'id': uid, 'stations':stations,'vehicles':vehicles}
    return render(request, "bookride.html",context)

@csrf_exempt
def bookrided(request):
    if request.method == 'POST':
        ststation = request.POST.get('ststation')
        
        vehicles = cf.allVehicleID(ststation)
        
        veh = list()
        
        for i in vehicles:
            a = dict()
            a['veh_id'] = i[0]
            a['veh_name'] = i[1]
            veh.append(a)
            
        print(veh)
    
    return HttpResponse(json.dumps(veh),content_type="application/json")

def bookridemain(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        ststation = request.POST.get('ststation')
        endstation = request.POST.get('endstation')
        exphours = request.POST.get('exphours')
        vehicle = request.POST.get('vehicle')
        price = cf.calculatePrice(uid, vehicle) * int(exphours)
        res = cf.getUserDetails(uid)
        if(int(price) > int(res[14])):
            context = {'name': res[3], 'credits': res[14], 'rides': res[13], 'id': res[0]}
            if(res[10] == "3"):
                return render(request, "manageruser.html", context)
            return render(request, "user.html", context)
    context = {'id': uid, 'vehid': vehicle, 'ststation': ststation, 'endstation': endstation, 'hours': exphours, 'lat': lat, 'lon': lon, 'price': price}
    return render(request, "startride.html",context)

def riding(request):
    if request.method == 'POST':
        uid = request.POST.get('id')
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        ststation = request.POST.get('ststation')
        endstation = request.POST.get('endstation')
        exphours = request.POST.get('hours')
        vehicle = request.POST.get('vehid')
        price = request.POST.get('price')
    rideid = cf.startRideMain(uid,vehicle, ststation, endstation, exphours, price,lat,lon)
    context = {'rideid': rideid, 'id': uid, 'vehid': vehicle, 'ststation': ststation, 'endstation': endstation, 'hours': exphours, 'lat': lat, 'lon': lon, 'price': price}
    return render(request, "onride.html", context)

def stopride(request):
    if request.method == 'POST':
        uid = request.POST.get('id')
        cf.ongoingRideStop(uid)
    res = cf.getUserDetails(uid)
    context = {'name': res[3], 'credits': res[14], 'rides': res[13], 'id': res[0], 'message': 'ride ended successfully!!'}
    return render(request, "user.html", context)

def user(request):
    uid = request.GET.get('id')
    
    ride = cf.checkOngoingRides(uid)
    if(ride != None):
        context = {'rideid': ride[0], 'id': uid, 'vehid': ride[2], 'ststation': ride[7], 'endstation': ride[8], 'enddate': ride[6], 'hours': ride[9], 'lat': ride[3], 'lon': ride[4], 'price': ride[10]}
        return render(request, "onride.html", context)
    
    res = cf.getUserDetails(uid)
    context = {'name': res[3], 'credits': res[14], 'rides': res[13], 'id': res[0]}
    if(res[10] == "3"):
        return render(request, "manageruser.html", context)
    elif(res[10] == "4"):
        return getimage(request)
    return render(request, "user.html", context)

def prides(request):
    uid = request.GET.get('id')
    
    ride = cf.checkOngoingRides(uid)
    if(ride != None):
        context = {'rideid': ride[0], 'id': uid, 'vehid': ride[2], 'ststation': ride[7], 'endstation': ride[8], 'enddate': ride[6], 'hours': ride[9], 'lat': ride[3], 'lon': ride[4], 'price': ride[10]}
        return render(request, "onride.html", context)
    
    rides = cf.ridesListD(uid)
    context = {'id': uid, 'rides': rides}
    return render(request, "prides.html",context)

def preports(request):
    uid = request.GET.get('id')
    
    ride = cf.checkOngoingRides(uid)
    if(ride != None):
        context = {'rideid': ride[0], 'id': uid, 'vehid': ride[2], 'ststation': ride[7], 'endstation': ride[8], 'enddate': ride[6], 'hours': ride[9], 'lat': ride[3], 'lon': ride[4], 'price': ride[10]}
        return render(request, "onride.html", context)
    
    reports = cf.reportsListD(uid)
    context = {'id': uid, 'reports': reports}
    return render(request, "preports.html",context)

def reportissue(request):
    uid = request.GET.get('id')
    
    ride = cf.checkOngoingRides(uid)
    if(ride != None):
        context = {'rideid': ride[0], 'id': uid, 'vehid': ride[2], 'ststation': ride[7], 'endstation': ride[8], 'enddate': ride[6], 'hours': ride[9], 'lat': ride[3], 'lon': ride[4], 'price': ride[10]}
        return render(request, "onride.html", context)
    
    context = {'id': uid}
    return render(request, "reportissue.html",context)

def reportd(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        
        ride = cf.checkOngoingRides(uid)
        if(ride != None):
            context = {'rideid': ride[0], 'id': uid, 'vehid': ride[2], 'ststation': ride[7], 'endstation': ride[8], 'enddate': ride[6], 'hours': ride[9], 'lat': ride[3], 'lon': ride[4], 'price': ride[10]}
            return render(request, "onride.html", context)
        
        comment = request.POST.get('comment')
        cf.createReportD(uid, comment)
        res = cf.getUserDetails(uid)
        context = {'name': res[3], 'credits': res[14], 'rides': res[13], 'id': res[0], 'message':"report has been added successfully!"}
        if(res[10] == "3"):
            return render(request, "manageruser.html", context)
        elif(res[10] == "4"):
            return getimage(request)
        else:
            return render(request, "user.html", context)

def addmoneyd(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        
        ride = cf.checkOngoingRides(uid)
        if(ride != None):
            context = {'rideid': ride[0], 'id': uid, 'vehid': ride[2], 'ststation': ride[7], 'endstation': ride[8], 'enddate': ride[6], 'hours': ride[9], 'lat': ride[3], 'lon': ride[4], 'price': ride[10]}
            return render(request, "onride.html", context)
        
        money = request.POST.get('money')
        card = request.POST.get('card')
        cvv = request.POST.get('cvv')
        expdate = request.POST.get('expdate')
        
        cf.addMoneyTrans(uid,card,cvv,expdate,money)
        
        res = cf.getUserDetails(uid)
        
        context = {'name': res[3], 'credits': res[14], 'rides': res[13], 'id': res[0], 'message':"wallet add request has been sent to bank"}
        
        if(res[10] == "3"):
            return render(request, "manageruser.html", context)
        elif(res[10] == "4"):
            return getimage(request)
        else:
            return render(request, "user.html", context)

def registerd(request):
    if request.method == 'POST':
        fuser = request.POST.get('fuser')
        luser = request.POST.get('luser')
        user = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        dlicense = request.POST.get('license')
        sos = request.POST.get('sos')
        utype = request.POST.get('utype')
        
        res = lf.register(fuser, luser, user, password, email, age, phone, address, pincode, dlicense, sos, utype)
        if(res == 0):
            context = {"error": "something error has occured!!"}
            return render(request, "register.html", context)
        
    context = {'name': res[3], 'credits': res[14], 'rides': res[13]}
    if(res[10] == "3"):
        return render(request, "manageruser.html", context)
    elif(res[10] == "4"):
        return getimage(request)
    else:
        return render(request, "user.html", context)

def logind(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        res = lf.login(username, password)
        if(res == 0):
            context = {"error": "wrong credentials!!"}
            return render(request, "login.html",context)
    
    
    ride = cf.checkOngoingRides(res[0])
    if(ride != None):
        context = {'rideid': ride[0], 'id': res[0], 'vehid': ride[2], 'ststation': ride[7], 'endstation': ride[8], 'enddate': ride[6], 'hours': ride[9], 'lat': ride[3], 'lon': ride[4], 'price': ride[10]}
        return render(request, "onride.html", context)
    
    context = {'name': res[3], 'credits': res[14], 'rides': res[13], 'id': res[0]}
    if(res[10] == "3"):
        return render(request, "manageruser.html", context)
    elif(res[10] == "4"):
        return getimage(request)
    else:
        return render(request, "user.html", context)

def viewridesm(request):
    uid = request.GET.get('id')
    rides = mf.allRides()
    context = {'id': uid, 'rides': rides}
    return render(request, "allrides.html",context)

def vieworidesm(request):
    uid = request.GET.get('id')
    rides = mf.allOnGoingRides()
    context = {'id': uid, 'rides': rides}
    return render(request, "allorides.html",context)

def vehicles(request):
    uid = request.GET.get('id')
    vehicles = mf.allVehicles()
    stations = mf.allStations()
    context = {'id': uid, 'vehicles': vehicles, 'stations': stations}
    return render(request, "allvehicles.html",context)

def chargevehicle(request):
    vid = request.GET.get('vid')
    mf.chargeVehicle(vid)
    return vehicles(request)

def stations(request):
    uid = request.GET.get('id')
    stations = mf.allStations()
    context = {'id': uid, 'stations': stations}
    return render(request, "allstations.html",context)

def viewreportsm(request):
    uid = request.GET.get('id')
    reports = mf.allReports()
    context = {'id': uid, 'reports': reports}
    return render(request, "allreports.html",context)

def allpendingreports(request):
    uid = request.GET.get('id')
    reports = mf.allPendingReports()
    context = {'id': uid, 'reports': reports}
    return render(request, "allpendingreports.html",context)

def reportapprove(request):
    rid = request.GET.get('rid')
    mf.reportApprove(rid)
    return viewreportsm(request)

def reportreject(request):
    rid = request.GET.get('rid')
    mf.reportReject(rid)
    return viewreportsm(request)

def reportfixed(request):
    rid = request.GET.get('rid')
    mf.reportFixed(rid)
    return viewreportsm(request)

def add(request):
    uid = request.GET.get('id')
    context = {'id': uid}
    return render(request, "addvehicletype.html",context)

def addvehicletype(request):
    uid = request.GET.get('id')
    context = {'id': uid}
    return render(request, "addvehicletype.html",context)

def addvehicle(request):
    uid = request.GET.get('id')
    types = mf.allVehTypes()
    context = {'id': uid, "vTypes":types[0], "stations":types[1]}
    return render(request, "addvehicle.html",context)

def addstation(request):
    uid = request.GET.get('id')
    context = {'id': uid}
    return render(request, "addstation.html",context)

def addvtyped(request):
    if request.method == 'POST':
        uid = request.POST.get('id')
        vehname = request.POST.get('vehname')
        comname = request.POST.get('comname')
        model = request.POST.get('model')
        capacity = request.POST.get('capacity')
        kmpc = request.POST.get('kmpc')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        
        mf.insertVehType(vehname,comname,model,capacity,kmpc,price,discount)
        
        
    context = {'id': uid, 'message':"Vehicle type has been added!"}
    return render(request, "addvehicletype.html",context)

def addvehd(request):
    if request.method == 'POST':
        uid = request.POST.get('id')
        vehname = request.POST.get('vehname')
        vehtype = request.POST.get('vehtype')
        licenseP = request.POST.get('license')
        station = request.POST.get('station')
        
        mf.insertVehicle(vehname,vehtype,licenseP,station)
        
        
    types = mf.allVehTypes()
    context = {'id': uid, "vTypes":types[0], "stations":types[1], 'message':"Vehicle has been added!"}
    return render(request, "addvehicle.html",context)

def addstationd(request):
    if request.method == 'POST':
        uid = request.POST.get('id')
        stationname = request.POST.get('stationname')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        pincode = request.POST.get('pincode')
        
        mf.insertStation(stationname,latitude,longitude,pincode)
        
        
    context = {'id': uid,'message':"Station has been added!"}
    return render(request, "addstation.html",context)



def getimage(request):
    
    stdate = request.GET.get('stdate')
    enddate = request.GET.get('enddate')
    uid = request.GET.get('id')
    
    print(stdate,enddate,sep="\n")
    
    if(uid == None):
        uid = 1
    
    if(int(uid) == 1):
        
        if(stdate == None or enddate == None):
            vehicles = m.bestVehicles()
        else:
            vehicles = m.bestVehicles1(stdate, enddate)
            
        x = [i[0] for i in vehicles]
        y = [i[1] if i[1]!=None else 0 for i in vehicles]
        plt.figure(figsize=(12, 5))
        plt.bar(x,y)
        plt.xlabel("vehicle Name")
        plt.ylabel("Rides count")
        plt.title("Top Rided Vehicle")
        
    elif(int(uid) == 2):
        
        if(stdate == None or enddate == None):
            vehicles = m.bestEarningVehicles()
        else:
            vehicles = m.bestEarningVehicles1(stdate, enddate)
        
        
        x = [i[0] for i in vehicles]
        y = [i[1] if i[1]!=None else 0 for i in vehicles]
        plt.figure(figsize=(12, 5))
        plt.bar(x,y)
        plt.xlabel("Vehicle Name")
        plt.ylabel("Total Earning")
        plt.title("Top Earning Vehicle")
        
    elif(int(uid) == 3):
        
        
        if(stdate == None or enddate == None):
            stations = m.bestStation()
        else:
            stations = m.bestStation1(stdate, enddate)
        
        x = [i[0] for i in stations]
        y = [i[1] if i[1]!=None else 0 for i in stations]
        plt.figure(figsize=(12, 5))
        plt.bar(x,y)
        plt.xlabel("Station Name")
        plt.ylabel("Total Rides")
        plt.title("Busiest Station")
        
    elif(int(uid) == 4):
        
        
        if(stdate == None or enddate == None):
            stations = m.bestEarningStation()
        else:
            stations = m.bestEarningStation1(stdate, enddate)
        
        x = [i[0] for i in stations]
        y = [i[1] if i[1]!=None else 0 for i in stations]
        plt.figure(figsize=(12, 5))
        plt.bar(x,y)
        plt.xlabel("Station Name")
        plt.ylabel("Total Earning")
        plt.title("Top Earning Station")
        
    elif(int(uid) == 5):
        
        if(stdate == None or enddate == None):
            users = m.topSpendingUser()
        else:
            users = m.topSpendingUser1(stdate, enddate)
        
        x = [i[0] for i in users]
        y = [i[1] if i[1]!=None else 0 for i in users]
        plt.figure(figsize=(12, 5))
        plt.bar(x,y)
        plt.xlabel("User Name")
        plt.ylabel("Total Spendings")
        plt.title("Top Spending User")
    
    elif(int(uid) == 6):
        
        if(stdate == None or enddate == None):
            vehicleType = m.bestVehicleType()
        else:
            vehicleType = m.bestVehicleType1(stdate, enddate)
        
        
        x = [i[0] for i in vehicleType]
        y = [i[1] if i[1]!=None else 0 for i in vehicleType]
        plt.figure(figsize=(12, 5))
        plt.bar(x,y)
        plt.xlabel("vehicle Type name")
        plt.ylabel("Total Rides Booked")
        plt.title("Busiest Vehicle Type")
    
    elif(int(uid) == 7):
        
        plt.figure(figsize=(13, 5))
        
        if(stdate == None or enddate == None):
           vehicles = m.bestEarningVehicles()
        else:
            vehicles = m.bestEarningVehicles1(stdate, enddate)
        
        x = [i[0] for i in vehicles]
        y = [i[1] if i[1]!=None else 0 for i in vehicles]
        
        rem = 0
        remid = 0
        for i in range(len(y)):
            if(y[i]==0):
                rem=1
                remid=i
                break
        
        if(rem == 1):
            x = x[0:remid]
            y = y[0:remid]
        explode = [0.1 for i in y]
        
        plt.subplot(1, 2, 1)
        plt.pie(y, explode=explode, labels=x, autopct='%1.1f%%', shadow=True)
        plt.title("top earning vehicle")
        
        
        if(stdate == None or enddate == None):
            stations = m.bestEarningStation()
        else:
            stations = m.bestEarningStation1(stdate, enddate)
        
        x = [i[0] for i in stations]
        y = [i[1] if i[1]!=None else 0 for i in stations]
        
        rem = 0
        remid = 0
        for i in range(len(y)):
            if(y[i]==0):
                rem=1
                remid=i
                break
        
        if(rem == 1):
            x = x[0:remid]
            y = y[0:remid]
        explode = [0.1 for i in y]
        
        plt.subplot(1, 2, 2)
        plt.pie(y,labels=x, explode=explode, autopct='%1.1f%%', shadow=True)
        plt.title("Top Earning Station")
    
    
    buf=io.BytesIO()
    plt.savefig(buf,format='png')
    plt.close()        
    buf.seek(0)
    string =base64.b64encode(buf.read())
    buf.close()
    uri=urllib.parse.quote(string)
    
    context={'imgdata':uri, 'id':int(uid)}
    
    return render(request, "manager.html", context)

def test(request):
    return render(request, "test.html") 

def trackride(request):
    uid = request.POST.get('id')
    
    ride = cf.checkOngoingRides(uid)
    context = {'id': uid, 'lat': ride[3], 'lon': ride[4]}
    return render(request, "trackride.html", context)

def checkrides(request):
    uid = request.POST.get('id')
    
    ride = cf.checkOngoingRides(uid)
    context = {'rideid': ride[0], 'id': uid, 'vehid': ride[2], 'ststation': ride[7], 'endstation': ride[8], 'enddate': ride[6], 'hours': ride[9], 'lat': ride[3], 'lon': ride[4], 'price': ride[10]}
    return render(request, "onride.html", context)

@csrf_exempt
def updateloc(request):
    uid = request.POST.get('id')
    lat = request.POST.get('lat')
    lon = request.POST.get('lon')
    
    ride = cf.checkOngoingRides(uid)
    
    cf.liveLocationd(ride[0], lat, lon)
    
    return HttpResponse()

@csrf_exempt
def sos(request):
    uid = request.POST.get('id')
    lat = request.POST.get('lat')
    lon = request.POST.get('lon')
    
    res = cf.getUserDetails(uid)
    
    message = "{} {} sent an SOS signal at {}, {}.".format(res[2], res[1], lat, lon)
    
    mailer.sendmail("progsdproject@gmail.com", message)
    
    if(res[15] != "" and "@" in res[15]):
        message = "{} {} sent an SOS signal at {}, {}. We are also actively looking into it. \n\nTeam EVE LC02-LB01-A".format(res[2], res[1], lat, lon)
        mailer.sendmail(res[15], message)
    
    return HttpResponse()

@csrf_exempt
def updatevehloc(request):
    vehid = request.POST.get('vehid')
    newloc = request.POST.get('newloc')
    
    mf.updateVehLoc(vehid,newloc)
    
    return HttpResponse()

@csrf_exempt
def lastusers(request):
    vehid = request.POST.get('vehid')
    
    users = mf.lastusers(vehid)
    
    usersmain = list()
    
    usersveh = list()
    
    for i in range(len(users)):
        users[i] = list(users[i])
        if(str(users[i][1])+str(users[i][7]) in usersveh):
            pass
        else:
            usersveh.append(str(users[i][1])+str(users[i][7]))
            usersmain.append(users[i])
    
    return HttpResponse(json.dumps(usersmain),content_type="application/json")

@csrf_exempt
def damages(request):
    
    uid = request.POST.get('userid')
    amount = request.POST.get('amount')
    vehid = request.POST.get('vehid')
    comment = request.POST.get('comment')
    
    print(uid, amount, vehid, comment)
    
    res = cf.getUserDetails(uid)
    
    print(res)
    
    message = "Hello {} {},\nDamage Charges of {} are leivied on your account. Please log in to check and pay it.\n\nTeam EVE LC02-LB01-A".format(res[1], res[2], amount)
    subject = "Vehicle Damages Penality - EVE"
    
    mailer.sendmail(res[5], message, subject)
    
    mf.addDamages(uid, amount, vehid, comment)
    
    return HttpResponse()