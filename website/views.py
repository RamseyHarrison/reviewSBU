# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import foodItemCommentForm
from django.shortcuts import render


def index(request):
    return render(request, 'homepage/index.html', {})

<<<<<<< HEAD
def reviewItem(request):

    context = {
    "form":foodItemCommentForm,
    "item":"Tofu",
    "outcome":"Submit"
    }
    return render(request, 'pages/review_item.html', context)
=======
def dining(request, dining_area):
    return render(request, 'dining/dining.html', {})
>>>>>>> a6d7231a669f27c33bc0d1f8ebaee008cda8810e
