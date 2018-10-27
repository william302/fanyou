from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MerchantUserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = MerchantUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = MerchantUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
