from django.shortcuts import render
import bank.bankservices as bs

# Create your views here.
def index(request):
    pending = bs.fetchPending() 
    context = {'pending': pending}
    return render(request, "bank.html", context) 

def approve(request):
    wid = request.GET.get('wid')
    bs.updateWalletA(wid)
    return index(request)


def reject(request):
    wid = request.GET.get('wid')
    bs.updateWalletR(wid)
    return index(request)

