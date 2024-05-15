from django.shortcuts import render


def home(request):
    return render(request, 'base/index.html',{})
def getstarted(request):
    return render(request, 'base/bio.html', {})



# Create your views here.
