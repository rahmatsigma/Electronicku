from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun {username} berhasil dibuat! Silakan login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def beranda(request):
    products = Product.objects.all().order_by('-id')    
    konteks = {'products': products}
    return render(request, 'blog/beranda.html', konteks)

@login_required
def pengaturan(request):
    if request.method == 'POST':        
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil berhasil diperbarui!')
            return redirect('pengaturan') 
    else:        
        form = UserChangeForm(instance=request.user)
    
    konteks = {'form': form}
    return render(request, 'blog/pengaturan.html', konteks)