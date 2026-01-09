from django import forms
from .models import Mobil

class MobilForm(forms.ModelForm):
    class Meta:
        model = Mobil
        fields = ['nama_mobil', 'merek', 'harga_sewa', 'tgl_pengambilan', 'tgl_pengembalian']
        
        # Menambahkan widget agar input tanggal muncul sebagai kalender (datepicker)
        widgets = {
            'tgl_pengambilan': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tgl_pengembalian': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nama_mobil': forms.TextInput(attrs={'class': 'form-control'}),
            'merek': forms.TextInput(attrs={'class': 'form-control'}),
            'harga_sewa': forms.NumberInput(attrs={'class': 'form-control'}),
        }