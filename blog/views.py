from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
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
    products = [
        {'nama': 'iPhone 16 Pro Max', 'harga': 'Rp 12.500.000', 'gambar': 'images/ip16pm.jpg'},
        {'nama': 'Laptop UltraBook 14"', 'harga': 'Rp 18.750.000', 'gambar': 'images/laptop.jpg'},
        {'nama': 'Smartwatch Series 8', 'harga': 'Rp 6.200.000', 'gambar': 'images/smartwatch.jpg'},
        {'nama': 'Headphone Noise-Cancelling', 'harga': 'Rp 4.500.000', 'gambar': 'images/headphone.jpg'},
        {'nama': '4K QLED TV 55"', 'harga': 'Rp 15.000.000', 'gambar': 'images/tv.jpg'},
        {'nama': 'Gaming Console Gen 5', 'harga': 'Rp 9.800.000', 'gambar': 'images/console.jpg'},
    ]
    
    konteks = {'products': products}
    return render(request, 'blog/beranda.html', konteks)