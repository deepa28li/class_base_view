from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View,TemplateView

# returning the string by using the function base views
def fbv_string(request):
    return HttpResponse('<h1>This is the string from fbv_string')

# returning the string by using the class base views
class Cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>String of Cbv String')
    
# rendering the html by function base views
def fbvhtml(request):
    return render(request,'fbvhtml.html')

# rendering the html by class base views
class cbvhtml(View):
    def get(self,request):
        return render(request,'cbvhtml.html')
    
#Insert data by fbv through model forms   
def insert_school_by_fbv(request):
    SFO=SchoolForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SO=SchoolForm(request.POST)
        if SO.is_valid():
            SO.save()
            return HttpResponse('insert_school_by_fbv is done')
    return render(request,'insert_school_by_fbv.html',d)

#Insert data by cbv through model forms   
class insert_school_by_cbv(View):
    def get(self,request):
        ESCO=SchoolForm()
        d={'ESCO':ESCO}
        return render(request,'insert_school_by_cbv.html',d)
    

    def post(self,request):
         SCO=SchoolForm(request.POST)
         if SCO.is_valid():
            SCO.save()
            return HttpResponse('insert_school_by_cbv is done')
         
class cbv_template(TemplateView):
    template_name='cbv_template.html'