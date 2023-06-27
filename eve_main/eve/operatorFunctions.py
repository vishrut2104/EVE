import mariadb
import eve.statusmap as statuses

db = mariadb.connect(user='root', password='', host='localhost', database='eve', autocommit=True)

def allReports():
    
    cursor1 = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT r_id, r.uid, veh_name, comments, r.status, r.veh_id FROM reports r, vehicles v WHERE r.veh_id=v.veh_id order by r_id desc")
    cursor1.execute(query)
    reports = cursor1.fetchall()
    
    for i in range(len(reports)):
        reports[i] = list(reports[i])
        reports[i][4] = statuses.statusmap.get(reports[i][4])
    
    cursor1.close()
    return reports

def insertVehType(vehname,comname,model,capacity,kmpc,price,discount):
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("insert into vehicle_type(vehicle_type_name,vehicle_company,vehicle_model,vehicle_seating_capacity,kms_charge,price_hour,student_discount) values(%s,%s,%s,%s,%s,%s,%s)")
    cursor.execute(query,(vehname,comname,model,capacity,kmpc,price,discount))
    cursor.close()
    
def insertVehicle(vehname,vehtype,licenseP,station):
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("insert into vehicles(veh_name,veh_type_id,vehicles_kms_run,charge_left,license_plate,station_id,status,service) values(%s,%s,%s,%s,%s,%s,%s,%s)")
    cursor.execute(query,(vehname,vehtype,"0","100",licenseP,station,"A","N"))
    cursor.close()
    
def insertStation(stationname,latitude,longitude,pincode):
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("insert into stations(station_name,latidute,longitude,pincode) values(%s,%s,%s,%s)")
    cursor.execute(query,(stationname,latitude,longitude,pincode))
    cursor.close()

def allVehTypes():
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT veh_type_id, vehicle_type_name from vehicle_type")
    cursor.execute(query)
    vehicleTypes = cursor.fetchall()
    query = ("SELECT station_id, station_name from stations")
    cursor.execute(query)
    stations = cursor.fetchall()
    cursor.close()
    return (vehicleTypes,stations)

def allPendingReports():
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT r_id, r.uid, veh_name, comments, r.status FROM reports r, vehicles v WHERE r.veh_id=v.veh_id and (r.status = %s or r.status = %s) order by r_id desc")
    cursor.execute(query, ("A","P",))
    reports = cursor.fetchall()
    
    for i in range(len(reports)):
        reports[i] = list(reports[i])
        reports[i][4] = statuses.statusmap.get(reports[i][4])
    cursor.close()
    return reports

def allRides():
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT p_ride_id, p.uid, date_of_booking,(select station_name from stations where station_id=start_station_id) as start_station, (select station_name from stations where station_id=end_station_id) as end_station, hours_rided, price, veh_id, u.username  FROM past_rides p, users u where p.uid=u.uid order by date_of_booking desc")
    cursor.execute(query)
    rides = cursor.fetchall()
    cursor.close()
    return rides

def allOnGoingRides():
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT ride_id, uid, date_of_booking,(select station_name from stations where station_id=start_station_id) as start_station, (select station_name from stations where station_id=end_station_id) as end_station, hours, estimated_price, if(curr_lat='',0,1) as track_status  FROM ongoing_rides order by date_of_booking desc")
    cursor.execute(query)
    rides = cursor.fetchall()
    cursor.close()
    return rides

def allVehicles():
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT v.veh_id, v.veh_name, vt.vehicle_type_name as veh_type, v.charge_left, s.station_name, v.status, v.service, (select count(*) from past_rides pr where v.veh_id=pr.veh_id) as t_rides from vehicles v, vehicle_type vt, stations s where vt.veh_type_id=v.veh_type_id and s.station_id = v.station_id")
    cursor.execute(query)
    vehicles = cursor.fetchall()
    
    for i in range(len(vehicles)):
        vehicles[i] = list(vehicles[i])
        vehicles[i][5] = statuses.statusmap.get(vehicles[i][5])
        vehicles[i][6] = statuses.statusmap.get(vehicles[i][6])
    cursor.close()
    return vehicles

def chargeVehicle(vid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT status, service FROM vehicles WHERE veh_id=%s")
    cursor.execute(query, (vid,))
    vehicle_status = cursor.fetchone()
    
    if(vehicle_status[0] == "U" and vehicle_status[1] == "Y"):
        query = ("update vehicles set charge_left=%s where veh_id=%s")
        cursor.execute(query, ('100',vid,))
    elif(vehicle_status[0] == "I"):
        pass
    else:
        query = ("update vehicles set status=%s,charge_left=%s where veh_id=%s")
        cursor.execute(query, ('A','100',vid,))
    cursor.close()
        
def updateVehLoc(vehid, stationid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("update vehicles set station_id=%s where veh_id=%s")
    cursor.execute(query, (stationid,vehid,))
    cursor.close()

def allStations():
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT station_id,station_name,pincode from stations")
    cursor.execute(query)
    stations = cursor.fetchall()
    cursor.close()
    return stations

def reportApprove(rid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("update reports set status=%s where r_id=%s")
    cursor.execute(query, ("P",rid))
    
    query = ("SELECT veh_id FROM reports WHERE r_id=%s")
    cursor.execute(query, (rid,))
    vehicle = cursor.fetchone()
    
    query = ("update vehicles set status=%s, service=%s where veh_id=%s")
    cursor.execute(query, ("I","Y", vehicle[0]))
    cursor.close()

def reportReject(rid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("update reports set status=%s where r_id=%s")
    cursor.execute(query, ("R",rid))
    cursor.close()

def reportFixed(rid):
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("update reports set status=%s where r_id=%s")
    cursor.execute(query, ("F",rid))
    
    query = ("SELECT veh_id FROM reports WHERE r_id=%s")
    cursor.execute(query, (rid,))
    vehicle = cursor.fetchone()
    
    query = ("update vehicles set status=%s, service=%s where veh_id=%s")
    cursor.execute(query, ("A","N", vehicle[0]))
    cursor.close()
    
def lastusers(vehid):
    cursor1 = db.cursor(named_tuple=True, buffered=True)
    query = ("SELECT p_ride_id, p.uid, date_of_booking,(select station_name from stations where station_id=start_station_id) as start_station, (select station_name from stations where station_id=end_station_id) as end_station, hours_rided, price, veh_id, u.username  FROM past_rides p, users u where p.uid=u.uid order by date_of_booking desc")
    cursor1.execute(query, (vehid,))
    users = cursor1.fetchall()
    
    cursor1.close()
    return users

def addDamages(uid, amount, vehid, comment):
    cursor = db.cursor(named_tuple=True, buffered=True)
    query = ("insert into damages(uid, amount, veh_id, comments, status) values(%s,%s,%s,%s,%s)")
    cursor.execute(query, (uid, amount, vehid, comment, "P"))
    cursor.close()