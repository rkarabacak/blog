from django.shortcuts import render, HttpResponse

def home_view(request):
    # if not request.user.is_authenticated():
    #     context = {
    #         'isim': 'Recep',
    #     }
    # else:
    context = {
        'isim': 'Recep',
    }
    return render(request, 'home.html', context)
    # return HttpResponse('<b>Hoşgeldiniz</b>')