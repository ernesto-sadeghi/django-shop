from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from website.forms import  ContactForm,NewstellerForm
# Create your views here.


def index(request):

    # return HttpResponse("<h1>indexPage </h1>")
    return render(request,"index.html")

# def home(request):

#     # return HttpResponse("<h1>home Page </h1>")
#     return render(request,"home.html")
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.add_message(request,messages.SUCCESS,"succesfully sended")
        else:
            messages.add_message(request,messages.ERROR,"sorry there was a problem")

    
    form=ContactForm()
    return render(request,"contact.html",{"form":form})

def elements(request):

    # return HttpResponse("<h1>home Page </h1>")
    return render(request,"elements.html")
def newstellerView(request):
    if request.method == "POST":
        
        form=NewstellerForm(request.POST)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect("/")
    else:
       return HttpResponseRedirect("/")
         
   
# def blog(request):

#     # return HttpResponse("<h1>blog Page </h1>")
#     return render(request,"blog.html")
    
def about(request):

    return render(request,"about.html")