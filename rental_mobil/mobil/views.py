from django.shortcuts import render, redirect, get_object_or_404
from .models import Mobil
from .forms import MobilForm

# 1. READ: Menampilkan semua daftar sewa mobil
def mobil_list(request):
    data_mobil = Mobil.objects.all()
    return render(request, 'mobil/mobil_list.html', {'data_mobil': data_mobil})

# 2. CREATE: Menambah data mobil baru
def mobil_create(request):
    if request.method == "POST":
        form = MobilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mobil_list')
    else:
        form = MobilForm()
    return render(request, 'mobil/mobil_form.html', {'form': form})

# 3. UPDATE: Mengedit data mobil yang sudah ada
def mobil_update(request, pk):
    # Menggunakan get_object_or_404 lebih aman daripada .get() 
    # agar muncul error 404 jika ID tidak ditemukan
    mobil = get_object_or_404(Mobil, id=pk)
    
    if request.method == "POST":
        form = MobilForm(request.POST, instance=mobil)
        if form.is_valid():
            form.save()
            return redirect('mobil_list')
    else:
        form = MobilForm(instance=mobil)
    return render(request, 'mobil/mobil_form.html', {'form': form})

# 4. DELETE: Menghapus data mobil
def mobil_delete(request, pk):
    mobil = get_object_or_404(Mobil, id=pk)
    if request.method == "POST":
        mobil.delete()
        return redirect('mobil_list')
    return render(request, 'mobil/mobil_confirm_delete.html', {'mobil': mobil})