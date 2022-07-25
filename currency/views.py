from django.shortcuts import render

import random

def index(request):
    return render(request,'index.html')

def get_currency(request):
    context ={'inr': random.randint(10,100), 'usd': random.randint(100,500),'er': random.randint(1000,5000)}
    return render(request, 'partials/show.html', context)
