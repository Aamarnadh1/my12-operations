from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'amar','l':[1,2,3,4,5]}
    return render(request,'looping.html',d)
