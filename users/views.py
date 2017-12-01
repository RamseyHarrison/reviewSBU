# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.shortcuts import render

from .tokens import account_activation_token
from .forms import SignUpForm


def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your ReviewSBU Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'users/user_register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'registration/account_activation_invalid.html')


def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html', {})


@login_required
def user_profile(request, userstring):
    uid = get_object_or_404(User, username=request.user.username)
    profile_user = get_object_or_404(User, username=userstring)
    profile_user_plates = []
    return render(request, 'users/user_profile.html',
                  {'user': uid, 'profile_user': profile_user})


@login_required
def user_profile_edit(request, userstring):
    if request.user.username != userstring:
        uid = get_object_or_404(User, username=request.user.username)
        profile_user = get_object_or_404(User, username=userstring)
        return render(request, 'users/user_profile.html', {'user': uid, 'profile_user': profile_user})
    uid = get_object_or_404(User, username=request.user.username)
    return render(request, 'users/user_profile_edit.html', {'user': uid})


@login_required
def user_settings(request):
    return render(request, 'users/user_settings.html', {})