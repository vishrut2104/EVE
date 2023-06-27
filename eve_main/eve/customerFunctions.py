import mariadb
import geocoder
import sys, time, msvcrt
import math
import eve.statusmap as statuses

db = mariadb.connect(user='root', password='', host='localhost', database='eve', autocommit=True)

def bookRide(userid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    #booking ride
    g = geocoder.ip('me')
    currLat = g.latlng[0]
    currLong = g.latlng[1]
    ud = getUserDetails(userid)
    stations = fetchNearbyStations(currLat, currLong)
    for i in range(len(stations)):
        print("{}: {} at {}".format(stations[i][0],stations[i][1],stations[i][4]))
    sid = input("pick a station id: ")
    vehicles = fetchAvailableVehicles(sid)
    for i in range(len(vehicles)):
        cost = vehicles[i][3]
        if(ud[10]=='2'):
            cost = int(vehicles[i][3]) * (100-int(vehicles[i][4])) / 100
            cost=math.floor(cost)
        print("{}: {}, {} with price per hour as {}".format(vehicles[i][0],vehicles[i][1],vehicles[i][2],cost))
    vid = input("pick a vehicle id: ")
    dsid = input("select drop station id: ")
    hours = input("how many hours are you thinking to travel: ")
    price = 0
    for i in range(len(vehicles)):
        if(int(vehicles[i][0])==int(vid)):
            price = int(vehicles[i][3])
            if(ud[10]=='2'):
                price = int(vehicles[i][3]) * (100-int(vehicles[i][4])) / 100
                price = math.floor(price)
            break
    estimatedPrice = price * int(hours)
    print("estimated price: ",estimatedPrice)
    if(int(ud[14]) < estimatedPrice):
        print("sorry.. low money in wallet. please add more money")
        return
    start = int(input("1. start. 2. Go back"))
    if(start == 1):
        startRide(userid,vid, sid, dsid, hours, estimatedPrice)
    cursor.close()

def calculatePrice(uid, vehid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    ud = getUserDetails(uid)
    query = ("SELECT vt.price_hour as price, vt.student_discount from vehicles v, vehicle_type vt where v.veh_type_id=vt.veh_type_id and v.veh_id=%s")
    cursor.execute(query, (vehid,))
    vehicle = cursor.fetchone()
    price = int(vehicle[0])
    if(ud[10]=='2'):
        price = (int(vehicle[0]) * (100-int(vehicle[1]))) / 100
    price = math.floor(price)
    cursor.close()
    return price
    
def allVehicleID(stationid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT veh_id, veh_name from vehicles where station_id=%s and status='A' and service='N'")
    cursor.execute(query, (stationid,))
    vehicles = cursor.fetchall()
    cursor.close()
    return vehicles

def allStations():
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT station_id,station_name,pincode from stations")
    cursor.execute(query)
    stations = cursor.fetchall()
    return stations

def startRide(userid,vid, sid, dsid, hours, estimatedPrice):
    cursor = db.cursor(named_tuple=True, buffered=True)
    #start a new ride
    query = ("update vehicles set status=%s where veh_id=%s")
    cursor.execute(query, ("U",vid))
    g = geocoder.ip('me')
    query = ("INSERT INTO ongoing_rides(uid,veh_id,curr_lat,curr_long,date_of_booking,start_station_id,end_station_id,hours,estimated_price) values(%s,%s,%s,%s,sysdate(),%s,%s,%s,%s)")
    cursor.execute(query, (userid,vid, g.latlng[0],g.latlng[1], sid, dsid, hours, estimatedPrice))
    ongoingRide(userid)
    cursor.close()
    
    
def startRideMain(userid,vid, sid, dsid, hours, estimatedPrice,lat,lon):
    cursor = db.cursor(named_tuple=True, buffered=True)
    #start a new ride
    query = ("update vehicles set status=%s where veh_id=%s")
    cursor.execute(query, ("U",vid))
    query = ("INSERT INTO ongoing_rides(uid,veh_id,curr_lat,curr_long,date_of_booking,start_station_id,end_station_id,hours,estimated_price) values(%s,%s,%s,%s,sysdate(),%s,%s,%s,%s)")
    cursor.execute(query, (userid,vid, lat,lon, sid, dsid, hours, estimatedPrice))
    query = ("SELECT * FROM ongoing_rides where uid=%s")
    cursor.execute(query, (userid,))
    ride = cursor.fetchone()
    rideId = ride[0]
    cursor.close()
    return rideId
    
def getUserDetails(userid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    #check wallet
    query = ("SELECT * FROM users where uid=%s")
    cursor.execute(query, (userid,))
    user = cursor.fetchone()
    cursor.close()
    return user

def deductWallet(userid, money, pRideId, hours):
    cursor = db.cursor(named_tuple=True, buffered=True)
    #remove money
    ud = getUserDetails(userid)
    query = ("update users set wallet_money=%s where uid=%s")
    cursor.execute(query, (int(ud[14])-int(money),userid))
    query = ("insert into transactions(p_ride_id, hours_rided, price, uid, comments) values(%s,%s,%s,%s,%s)")
    cursor.execute(query, (pRideId,hours, money, userid, "testing"))
    cursor.close()
    
def payDamages(userid, tid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    #remove money
    ud = getUserDetails(userid)
    
    query = ("SELECT amount FROM damages WHERE damage_id=%s")
    cursor.execute(query, (tid,))
    damageAmount = cursor.fetchone()
    
    if(int(damageAmount[0]) > int(ud[14])):
        return int(damageAmount[0]) - int(ud[14])
    
    query = ("update users set wallet_money=%s where uid=%s")
    cursor.execute(query, (int(ud[14])-int(damageAmount[0]),userid))
    query = ("update damages set status=%s where damage_id=%s")
    cursor.execute(query, ("S", tid))
    cursor.close()
    return 0

def addMoney(userid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    #adding money
    money = input("how much money you want to add")
    cardNo = input("enter card no: ")
    cvv = input("enter security pin: ")
    expDate = input("Enter expiry date (DD-MM-YYYY): ")
    addMoneyTrans(userid,cardNo,cvv,expDate,money)
    cursor.close()

def addMoneyTrans(userid,cardNo,cvv,expDate,money):
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("insert into wallet(uid, card_no, cvv,exp_date, amount, date_of_adding) values(%s,%s,%s,%s,%s, sysdate())")
    cursor.execute(query, (userid,cardNo,cvv,expDate,money))
    print("your request for adding money has been notified to the bank.")
    cursor.close()

def createReport(userid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    #creating report
    query = ("SELECT p.veh_id, veh_name FROM past_rides p, vehicles v where uid=%s and p.veh_id=v.veh_id order by date_of_booking desc limit 1")
    cursor.execute(query, (userid,))
    latestRide = cursor.fetchone()
    print("your last rided car is {}".format(latestRide[1]))
    comment = input("enter what you felt wrong: ")
    query = ("insert into reports(uid, veh_id, comments,status) values(%s,%s,%s,%s)")
    cursor.execute(query, (userid,latestRide[0],comment,"A"))
    print("your report has been added. Soon operator will verify the report. Thank you!!")
    cursor.close()
    
def createReportD(userid, comment):
    cursor = db.cursor(named_tuple=True, buffered=True)
    #creating report
    query = ("SELECT p.veh_id, veh_name FROM past_rides p, vehicles v where uid=%s and p.veh_id=v.veh_id order by date_of_booking desc limit 1")
    cursor.execute(query, (userid,))
    latestRide = cursor.fetchone()
    query = ("insert into reports(uid, veh_id, comments,status) values(%s,%s,%s,%s)")
    cursor.execute(query, (userid,latestRide[0],comment,"A"))
    cursor.close()

def fetchNearbyStations(currLat, currLong):
    cursor = db.cursor(named_tuple=True, buffered=True)
    #fetch nearby stations
    query = ("SELECT * FROM stations order by abs(latidute - %s), abs(longitude - %s)")
    cursor.execute(query, (currLat, currLong))
    
    stations = cursor.fetchall()
    cursor.close()
    return stations

def fetchAvailableVehicles(stationId):
    cursor = db.cursor(named_tuple=True, buffered=True)
    #fetch available vehicles
    query = ("SELECT veh_id, veh_name, vehicle_type_name, price_hour, student_discount FROM vehicles a, vehicle_type b where a.veh_type_id=b.veh_type_id and station_id=%s and status=%s and service=%s")
    cursor.execute(query, (stationId,"A","N"))
    
    vehicles = cursor.fetchall()
    cursor.close()
    return vehicles

def checkOngoingRides(userid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    #checking ongoing rides
    query = ("SELECT * FROM ongoing_rides where uid=%s")
    cursor.execute(query, (userid,))
    rided = cursor.fetchone()
    
    if(rided != None):
        
        rided = list(rided)
    
        query = ("SELECT latidute, longitude FROM stations where station_id=%s")
        cursor.execute(query, (rided[8],))
        locd = cursor.fetchone()
    
        rided[3] = locd[0]
        rided[4] = locd[1]
    cursor.close()
    
    return rided

def getCurLoc(userid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT * FROM ongoing_rides where uid=%s")
    cursor.execute(query, (userid,))
    
    rides = cursor.fetchone()
    cursor.close()
    return rides

def liveLocation(ride_id):
    cursor = db.cursor(named_tuple=True, buffered=True)
    g = geocoder.ip('me')
    currLat = g.latlng[0]
    currLong = g.latlng[1]
    query = ("update ongoing_rides set curr_lat=%s, curr_long=%s where ride_id=%s")
    cursor.execute(query, (currLat, currLong, ride_id))
    print(currLat, currLong)
    cursor.close()
    
def liveLocationd(ride_id, currLat, currLong):
    
    cursor1 = db.cursor(named_tuple=True)
    
    query = ("update ongoing_rides set curr_lat=%s, curr_long=%s where ride_id=%s")
    cursor1.execute(query, (currLat, currLong, ride_id))
    
    cursor1.close()


def ongoingRide(userid):
    
    cursor = db.cursor(named_tuple=True, buffered=True)
    #on going ride options
    query = ("SELECT * FROM ongoing_rides where uid=%s")
    cursor.execute(query, (userid,))
    ride = cursor.fetchone()
    rideId = ride[0]
    while(True):
        stopper = readInput('Press 1 to stop the ride',"")
        if(stopper=="1"):
            break
        liveLocation(rideId)
    ongoingRideStop(userid)
    cursor.close()

def ongoingRideStop(userid):
    
    cursor = db.cursor(named_tuple=True, buffered=True)
    #finish the ongoing ride
    query = ("SELECT * FROM ongoing_rides where uid=%s")
    cursor.execute(query, (userid,))
    ride = cursor.fetchone()
    cursor.execute("select sysdate() from dual")
    rideId = ride[0]
    
    query = ("select round(time_to_sec(timediff(sysdate(), date_of_booking )) / 3600,2) as hours from ongoing_rides where ride_id = %s")
    cursor.execute(query, (rideId,))
    
    hours = math.ceil(cursor.fetchone()[0])
    price = calculatePrice(userid, ride[2]) * hours
    price = math.ceil(price)
    
    query = ("insert into past_rides(ride_id, uid, veh_id, date_of_booking, date_of_return, start_station_id, end_station_id, hours_rided, price) values(%s,%s,%s,%s,sysdate(),%s,%s,%s,%s)")
    cursor.execute(query, (rideId, userid,ride[2],ride[5], ride[7], ride[8], hours, price))
    query = ("delete FROM ongoing_rides where ride_id=%s")
    cursor.execute(query, (rideId,))

    query = ("select * FROM past_rides where ride_id=%s and uid=%s and date_of_booking=%s")
    cursor.execute(query, (rideId, userid, ride[5]))
    
    pride = cursor.fetchone()
    
    deductWallet(userid, price, pride[0], hours)
    
    query = ("SELECT kms_charge, charge_left, hours_rided from vehicle_type vt, vehicles v, past_rides r where v.veh_type_id = vt.veh_type_id and v.veh_id=r.veh_id and r.p_ride_id = %s")
    cursor.execute(query, (pride[0],))
    charging = cursor.fetchone()
    
    charge = int(charging[1]) - math.ceil(int(charging[2]) * int(charging[1]) / int(charging[0]))
    
    query = ("update vehicles set status=%s, station_id=%s, charge_left=%s where veh_id=%s")
    cursor.execute(query, ("C",ride[8], charge, ride[2]))
    
    ud = getUserDetails(userid)
    query = ("update users set rides=%s where uid=%s")
    cursor.execute(query, (int(ud[13]) + 1,userid))
    
    
    print("ride ended sucessfully!!!")
    cursor.close()

def ridesList(userid):
    
    cursor = db.cursor(named_tuple=True, buffered=True)
    #fetch user last rides
    query = ("SELECT p_ride_id, uid, date_of_booking,(select station_name from stations where station_id=start_station_id) as start_station, (select station_name from stations where station_id=end_station_id) as end_station, hours_rided, price  FROM past_rides WHERE uid=%s")
    cursor.execute(query, (userid,))
    rides = cursor.fetchall()
    for i in range(len(rides)):
        print("{}. rided on {} from {} to {} for {} hours and spent {} pounds.".format(rides[i][0],rides[i][2],rides[i][3],rides[i][4],rides[i][5],rides[i][6]))
    cursor.close()

def ridesListD(userid):
    
    cursor = db.cursor(named_tuple=True, buffered=True)
    #fetch user last rides
    query = ("SELECT p_ride_id, uid, date_of_booking,(select station_name from stations where station_id=start_station_id) as start_station, (select station_name from stations where station_id=end_station_id) as end_station, hours_rided, price  FROM past_rides WHERE uid=%s order by date_of_booking desc")
    cursor.execute(query, (userid,))
    rides = cursor.fetchall()
    cursor.close()
    return rides

def reportsList(userid):
    
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT r_id, veh_name, comments, r.status FROM reports r, vehicles v WHERE r.veh_id=v.veh_id and uid=%s")
    cursor.execute(query, (userid,))
    reports = cursor.fetchall()
    for i in range(len(reports)):
        print("{}. reported on {} vehicle with comment as {} and status is {}.".format(reports[i][0],reports[i][1],reports[i][2],reports[i][3]))
    cursor.close()

def reportsListD(userid):
    
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT r_id, veh_name, comments, r.status FROM reports r, vehicles v WHERE r.veh_id=v.veh_id and uid=%s order by r_id desc")
    cursor.execute(query, (userid,))
    reports = cursor.fetchall()
    
    for i in range(len(reports)):
        reports[i] = list(reports[i])
        reports[i][3] = statuses.statusmap.get(reports[i][3])
        
    cursor.close()
    return reports

def userTransactions(userid):
    
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT damage_id, 'damages' as type, amount, comments, status FROM damages WHERE uid=%s order by damage_id desc")
    cursor.execute(query, (userid,))
    damages = cursor.fetchall()
    
    for i in range(len(damages)):
        damages[i] = list(damages[i])
        damages[i].append("d"+str(damages[i][0]))
        damages[i][4] = statuses.statusmap.get(damages[i][4])
        
    query = ("SELECT wid, 'wallet' as type, amount, 'Add request to wallet' as comments, status FROM wallet WHERE uid=%s order by wid desc")
    cursor.execute(query, (userid,))
    wallet = cursor.fetchall()
    
    for i in range(len(wallet)):
        wallet[i] = list(wallet[i])
        wallet[i].append("w"+str(wallet[i][0]))
        wallet[i][4] = statuses.statusmap.get(wallet[i][4])
        
    damages = damages + wallet
        
    cursor.close()
    return damages

def readInput( caption, default, timeout = 3):

    start_time = time.time()
    sys.stdout.write('%s:'%(caption))
    sys.stdout.flush()
    input = ''
    while True:
        if msvcrt.kbhit():
            byte_arr = msvcrt.getche()
            if ord(byte_arr) == 13: # enter_key
                break
            elif ord(byte_arr) >= 32: #space_char
                input += "".join(map(chr,byte_arr))
        if len(input) == 0 and (time.time() - start_time) > timeout:
            print("")
            break

    print('')  # needed to move to next line
    if len(input) > 0:
        return input
    else:
        return default
