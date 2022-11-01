from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul':'project django',
        'kontributor':'karmanto',
        'nav':[
            ['/', 'Home'],
            ['/about', 'about'],
        ],
    }
    return render(request, 'index.html', context)