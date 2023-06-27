import mariadb
import eve.customerFunctions as cf

db = mariadb.connect(user='root', password='', host='localhost', database='eve', autocommit=True)
cursor = db.cursor(named_tuple=True)

def checkPending():
    print("select a pending transaction below to either approve or reject it")
    query = ("SELECT * FROM wallet where status=%s")
    cursor.execute(query, ("P",))
    pending = cursor.fetchall()
    for i in range(len(pending)):
        ud = cf.getUserDetails(pending[i][1])
        print("{}. name is {}, {} with card no. {}, requested {} pounds.".format(pending[i][0],ud[1],ud[2],pending[i][2],pending[i][5]))
    wid = input("enter the transaction id you wish to act on(press x to exit): ")
    if(wid=="x"):
        return
    status = input("1. approve. 2. reject: ")
    if(status=="1"):
        status="S"
    elif(status=="2"):
        status="R"
    else:
        return
    userid=""
    reqMoney=""
    for i in range(len(pending)):
        if(int(wid)==int(pending[i][0])):
            userid=pending[i][1]
            reqMoney=pending[i][5]
            break
    ud = cf.getUserDetails(userid)
    query = ("update wallet set status=%s where wid=%s")
    cursor.execute(query, (status,wid))
    if(status=="S"):
        query = ("update users set wallet_money=%s where uid=%s")
        cursor.execute(query, ((int(ud[14])+int(reqMoney)),userid))
    print("status has been updated sucessfully!!")
    
def fetchPending():
    query = ("SELECT * FROM wallet where status=%s")
    cursor.execute(query, ("P",))
    pending = cursor.fetchall()
    return pending

def updateWalletA(wid):
    query = ("update wallet set status=%s where wid=%s")
    cursor.execute(query, ("S",wid))
    
    query = ("SELECT * FROM wallet where wid=%s")
    cursor.execute(query, (wid,))
    
    pending = cursor.fetchone()
    
    ud = cf.getUserDetails(pending[1])
    query = ("update users set wallet_money=%s where uid=%s")
    cursor.execute(query, ((int(ud[14])+int(pending[5])),pending[1]))
    

def updateWalletR(wid):
    query = ("update wallet set status=%s where wid=%s")
    cursor.execute(query, ("R",wid))
