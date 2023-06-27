import customerFunctions as cf
import operatorFunctions as of
import managerFunctions as mf

def eveServices(userDetails):
    userType=userDetails[10]
    if(userType==3):
        eveOpServices(userDetails)
    elif(userType==4):
        eveMngServices(userDetails)
    onride = cf.checkOngoingRides(userDetails[0])
    if(onride):
        cf.ongoingRide(userDetails[0])
    while(True):
        userDetails = cf.getUserDetails(userDetails[0])
        print("hello {0}, you have {1} credits and you have taken {2} rides.".format(userDetails[3],userDetails[14],userDetails[13]))
        print("what do you want to do?")
        print("1. book a ride. 2. add credits to your account. 3. report an issue. 4. past rides. 5. past reports. 6. logout")
        # to add past ride details, past reports details
        op = int(input())
        if(op==1):
            #book a ride
            cf.bookRide(userDetails[0])
        elif(op==2):
            #add money
            cf.addMoney(userDetails[0])
        elif(op==3):
            #report
            cf.createReport(userDetails[0])
        elif(op==4):
            cf.ridesList(userDetails[0])
        elif(op==5):
            cf.reportsList(userDetails[0])
        elif(op==6):
            return 0
        else:
            print("sorry, you chose something wrong try again")

def eveOpServices(userDetails):
    print("Hello operator")
    while(True):
        print("what do you want to do?")
        print("1. Track a ride. 2. Charge Vehicles. 3. Check Vehicle Reports. 4. logout")
        op = int(input())
        if(op==1):
            #track a ride
            of.trackRide()
        elif(op==2):
            #charge vehicles
            of.chargeVehicles()
        elif(op==3):
            #check report
            of.checkReports()
        elif(op==4):
            return 0
        else:
            print("sorry, you chose something wrong try again")
def eveMngServices(userDetails):
    print("Hello manager")
    while(True):
        print("what do you want to do?")
        print("1. Vehicle Reports. 2. User Reports. 3. logout")
        op = int(input())
        if(op==1):
            #Vehicle Reports
            mf.vehicleReports()
        elif(op==2):
            #User Reports
            mf.userReports()
        elif(op==3):
            return 0
        else:
            print("sorry, you chose something wrong try again")
