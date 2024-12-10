from django.db import models
from django.http import HttpResponse
# Create your models here.


def index(request):
    return HttpResponse('Thi is from the product app view')