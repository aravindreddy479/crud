from django.shortcuts import redirect, render
from .models import paitents # type: ignore

# Create your views here.
def index(request):
    emp = paitents.objects.all()
    context = {
        'emp':emp,
    }
    return render(request,"index.html",context)
def ADD(request):
   if request.method =='POST':
       paitent_ID=request.POST.get('paitent_ID')
       Name=request.POST.get('Name')
       Age=request.POST.get('Age')
       Disease=request.POST.get('Disease')
       Location=request.POST.get('Location')
       emp = paitents(
           paitent_ID = paitent_ID, # type: ignore
           Name = Name, # type: ignore
           Age = Age, # type: ignore
           Disease = Disease, # type: ignore
           Location = Location # type: ignore
        )
       emp.save()
       return redirect('home')
   return render(request,"index.html")
       
def EDIT(request):
 emp = paitents.objects.all()
 context = {
        'emp':emp,
    }
 return redirect(request,"index.html",context)

def Update(request,id):
 
    if request.method == "POST":
        paitent_ID=request.POST.get('paitent_ID')
        Name=request.POST.get('Name')
        Age=request.POST.get('Age')
        Disease=request.POST.get('Disease')
        Location=request.POST.get('Location')

        emp = paitents(
            id = id,
            paitent_ID = paitent_ID, # type: ignore
            Name = Name, # type: ignore
            Age = Age, #
            Disease = Disease, 
            Location = Location 
            )
        emp.save()
        return redirect('home')
    return redirect(request,"index.html")

def Delete(request,id):
   emp = paitents.objects.filter(id=id)
   emp.delete()
   return redirect("home")
   context = {
      'emp':emp,
   }
   return redirect(request,"index.html",context)  
def Sin(request) :
   return render(request,'sin.html') 
def Login(request) :
   return render(request,'login.html') 
