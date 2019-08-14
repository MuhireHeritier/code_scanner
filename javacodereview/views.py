from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .forms import UserRegisterForm, QueryBoxForm
from django.http import HttpResponseRedirect, HttpResponse
import  re
from .check import checkV

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'javacodereview/register.html', {'form': form})

def upload_code(request):
    if request.method == 'POST':
        form = QueryBoxForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('queryForm')
            findings = checkV(code)
            return render(request, 'javacodereview/findings.html', {'findings': findings})
    else:
        form = QueryBoxForm()
    return render(request, 'javacodereview/upload.html', {'form': form})

def findings(request):
    return render(request, 'javacodereview/findings.html', {'title': 'About'})

def home(request):
    return render(request, 'javacodereview/home.html')