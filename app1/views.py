from django.shortcuts import render,HttpResponse
from.models import person


# Create your views here.
def home(request):
    if request.method=="POST":
        n=request.POST.get("name")
        e=request.POST.get("email")
        s=request.POST.get("subject")
        m=request.POST.get("message")
        person.objects.create(name=n,email=e,subject=s,message=m)
        return HttpResponse ("ثبت شد")
    return render(request,"app1/register.html")