# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    return render(request, 'homepage/index.html', {})

def dining(request, dining_area):
    return render(request, 'dining/dining.html', {})