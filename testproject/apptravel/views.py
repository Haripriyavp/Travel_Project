from django.shortcuts import render

from . models import Place
from . models import Transportation
# Create your views here.
def index(request):
    obj=Place.objects.all()
    obj2 = Transportation.objects.all()
    return render(request,'index.html',{'result':obj,'results':obj2})