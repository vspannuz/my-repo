from django.shortcuts import render

# Create your views here.
def index(request):
    dict = {'text':'hello world','number':100}
    return render(request,'first/index.html',dict)

def others(request):
    return render(request,'first/others.html')

def relative(request):
    return render(request,'first/Relatives_url_templates.html')
