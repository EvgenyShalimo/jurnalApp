from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .fake_data import generate_fake_persons
from .models import Person

def generate_fake_data(request):
    generate_fake_persons(10)
    return HttpResponse('Мы сгенерировали фейк данные!')

def phone_numbers(request):
    return render(request, 'test.html')

def ends_with_seven(request):
    numbers = Person.objects.filter(phone_number__endswith='7')
    context = {'numbers': numbers}
    return render(request, 'ends_with_seven.html', context)

def ends_with_nine_eight_five(request):
    numbers = Person.objects.filter(phone_number__endswith='985')
    context = {'numbers': numbers}
    return render(request, 'ends_with_nine_eight_five.html', context)

def all_numbers(request):
    numbers = Person.objects.all()
    return render(request, 'all_nubmers.html', {'numbers': numbers})



