
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages


def home(request):
    return render(request, 'accounts/dashboard.html')
