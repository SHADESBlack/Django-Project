from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    # ......................................................................
    # context = {
    #     'variable':"I am a good boy"
    # }
    # ......................................................................
    # -------For Taking Values from Database and show it in browser---------
    # contact = Contact.objects.all().values()
    # output = ""
    # for x in contact:
    #     output += x["name"]
    # return HttpResponse(output)
    # ----------------------------------------------------------------------
    return render(request, "index.html")
    # return HttpResponse("this is home page")

def about(request):
    return render(request, "about.html")
    # return HttpResponse("this is about page")

def services(request):
    return render(request, "services.html")
    # return HttpResponse("this is serices page")

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get('email')
        number = request.POST.get('number')
        desc = request.POST.get('desc') 
        contact = Contact(name=name, email=email, number=number, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your response has been recorded.')

    return render(request, "contacts.html")
     