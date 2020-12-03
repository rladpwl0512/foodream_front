from django.shortcuts import render

# Create your views here.
def mypage(request):
    return render(request, 'page.html')


def buy(request):
    return render(request, 'buy.html')

def wish(request):
    return render(request, 'wish.html')