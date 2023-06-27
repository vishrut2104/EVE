import mariadb

db = mariadb.connect(user='root', password='', host='localhost', database='eve', autocommit=True)
cursor = db.cursor(named_tuple=True)

def login(username,password):
    #check login status
    query = ("SELECT * FROM users where username=%s and password=%s")
    cursor.execute(query, (username,password))
    if(cursor.rowcount>0):
        return cursor.fetchone()
    else:
        return 0

def register(firstName,lastName,userName,password,email,age,phone,address,pincode,drivingLicense,sos,uType):
    #check register status
    cursor.execute("INSERT INTO users(firstname, lastname, username, password, email, age, phone, user_address, user_pincode, driving_license, sos_contact, user_type_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (firstName,lastName,userName,password,email,age,phone,address,pincode,drivingLicense,sos,uType))
    return login(userName,password)



