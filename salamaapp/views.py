from django.shortcuts import render
from .models import Banner,youthpost,January,Feburary,March,April,May,June,July,August,September,October,November,December

# Create your views here.

def index(request):

    banners= Banner.objects.all()


    return render(request, 'index.html', {'banner': banners} )


def about(request):

    return render(request, 'about.html')


def donation(request):
    


    return render(request, 'donation.html')


def programs(request):
    jan= January.objects.all()
    feb= Feburary.objects.all()
    march= March.objects.all()
    april= April.objects.all()
    may= May.objects.all()
    june= June.objects.all()
    july= July.objects.all()
    aug= August.objects.all()
    sept= September.objects.all()
    oct= October.objects.all()
    nov= November.objects.all()
    dec= December.objects.all()

    

    return render(request, 'programs.html', {'jan': jan, 'feb': feb, 'march': march, 'april': april, 'may': may, 'june':june, 'july':july, 'august': aug, 'sept': sept, 'oct':oct, 'nov': nov, 'dec': dec})

def post(request,pk):

    post= youthpost.objects.get(id=pk)

    return render(request, 'post.html', {'posts':post})

def youthpage(request):
    post= youthpost.objects.all()


    return render(request, 'youthpage.html', {'posts':post})
