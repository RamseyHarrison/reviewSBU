# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import foodItemCommentForm
from django.shortcuts import render


def index(request):
    return render(request, 'homepage/index.html', {})

def reviewItem(request):

    context = {
    "form":foodItemCommentForm,
    "item":"Tofu",
    "outcome":"Submit"
    }
    return render(request, 'pages/review_item.html', context)
