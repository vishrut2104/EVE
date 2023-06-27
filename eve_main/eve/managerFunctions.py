import mariadb

db = mariadb.connect(user='root', password='', host='localhost', database='eve', autocommit=True)
cursor = db.cursor(named_tuple=True)


def bestVehicles():
    query = ("SELECT v.veh_name, (select count(*) from past_rides pr where v.veh_id=pr.veh_id) as t_rides from vehicles v order by t_rides desc LIMIT 6")
    cursor.execute(query)
    vehicles = cursor.fetchall()
    return vehicles

def bestEarningVehicles():
    query = ("SELECT v.veh_name, (select sum(price) from past_rides pr where v.veh_id=pr.veh_id) as t_price from vehicles v order by t_price desc LIMIT 6")
    cursor.execute(query)
    vehicles = cursor.fetchall()
    return vehicles

def bestStation():
    query = ("SELECT s.station_name, (select count(*) from past_rides pr where s.station_id=pr.start_station_id) as t_rides from stations s order by t_rides desc LIMIT 6")
    cursor.execute(query)
    stations = cursor.fetchall()
    return stations

def bestEarningStation():
    query = ("SELECT s.station_name, (select sum(price) from past_rides pr where s.station_id=pr.start_station_id) as t_price from stations s order by t_price desc LIMIT 6")
    cursor.execute(query)
    stations = cursor.fetchall()
    return stations

def topSpendingUser():
    query = ("SELECT u.username, (select sum(amount) from wallet w where u.uid=w.uid) as t_amount from users u order by t_amount desc LIMIT 6")
    cursor.execute(query)
    users = cursor.fetchall()
    return users

def bestVehicleType():
    query = ("select vehicle_type_name, (select count(*) from past_rides pr, vehicles v where v.veh_id = pr.veh_id and v.veh_type_id=vt.veh_type_id) as t_rides from vehicle_type vt order by t_rides desc limit 6")
    cursor.execute(query)
    vehicleType = cursor.fetchall()
    return vehicleType

def bestVehicles1(stdate, enddate):
    query = ("SELECT v.veh_name, (select count(*) from past_rides pr where v.veh_id=pr.veh_id and STR_TO_DATE(pr.date_of_booking,'%Y-%m-%d') between STR_TO_DATE(%s,'%Y-%m-%d') and STR_TO_DATE(%s,'%Y-%m-%d')) as t_rides from vehicles v order by t_rides desc LIMIT 6")
    cursor.execute(query, (stdate, enddate))
    vehicles = cursor.fetchall()
    return vehicles

def bestEarningVehicles1(stdate, enddate):
    query = ("SELECT v.veh_name, (select sum(price) from past_rides pr where v.veh_id=pr.veh_id and STR_TO_DATE(pr.date_of_booking,'%Y-%m-%d') between STR_TO_DATE(%s,'%Y-%m-%d') and STR_TO_DATE(%s,'%Y-%m-%d')) as t_price from vehicles v order by t_price desc LIMIT 6")
    cursor.execute(query, (stdate, enddate))
    vehicles = cursor.fetchall()
    return vehicles

def bestStation1(stdate, enddate):
    query = ("SELECT s.station_name, (select count(*) from past_rides pr where s.station_id=pr.start_station_id and STR_TO_DATE(pr.date_of_booking,'%Y-%m-%d') between STR_TO_DATE(%s,'%Y-%m-%d') and STR_TO_DATE(%s,'%Y-%m-%d')) as t_rides from stations s order by t_rides desc LIMIT 6")
    cursor.execute(query, (stdate, enddate))
    stations = cursor.fetchall()
    return stations

def bestEarningStation1(stdate, enddate):
    query = ("SELECT s.station_name, (select sum(price) from past_rides pr where s.station_id=pr.start_station_id and STR_TO_DATE(pr.date_of_booking,'%Y-%m-%d') between STR_TO_DATE(%s,'%Y-%m-%d') and STR_TO_DATE(%s,'%Y-%m-%d')) as t_price from stations s order by t_price desc LIMIT 6")
    cursor.execute(query, (stdate, enddate))
    stations = cursor.fetchall()
    return stations

def topSpendingUser1(stdate, enddate):
    query = ("SELECT u.username, (select sum(amount) from wallet w where u.uid=w.uid and STR_TO_DATE(w.date_of_adding,'%Y-%m-%d') between STR_TO_DATE(%s,'%Y-%m-%d') and STR_TO_DATE(%s,'%Y-%m-%d')) as t_amount from users u order by t_amount desc LIMIT 6")
    cursor.execute(query, (stdate, enddate))
    users = cursor.fetchall()
    return users

def bestVehicleType1(stdate, enddate):
    query = ("select vehicle_type_name, (select count(*) from past_rides pr, vehicles v where v.veh_id = pr.veh_id and v.veh_type_id=vt.veh_type_id and STR_TO_DATE(pr.date_of_booking,'%Y-%m-%d') between STR_TO_DATE(%s,'%Y-%m-%d') and STR_TO_DATE(%s,'%Y-%m-%d')) as t_rides from vehicle_type vt order by t_rides desc limit 6")
    cursor.execute(query, (stdate, enddate))
    vehicleType = cursor.fetchall()
    return vehicleType