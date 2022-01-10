from django.shortcuts import render
from . models import DropDownList
from . forms import DropDownForm

# Create your views here.
def index(request):
  data =  DropDownList.objects.all()

  if request.method == "POST":
    dropdown = DropDownForm(request.POST)
    if dropdown.is_valid():
        dropdown.save()

  dropdown = DropDownForm(request.POST)
  return render(request,'index.html',{"dropdown":dropdown,"data":data})


