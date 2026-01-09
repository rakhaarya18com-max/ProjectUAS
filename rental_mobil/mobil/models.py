from django.db import models

# Model untuk data sewa mobil
class Mobil(models.Model):
    nama_mobil = models.CharField(max_length=100)
    merek = models.CharField(max_length=50)
    harga_sewa = models.IntegerField()
    
    # Mengganti transmisi dan kapasitas menjadi data waktu
    tgl_pengambilan = models.DateField()   # Tanggal mulai sewa
    tgl_pengembalian = models.DateField()  # Tanggal selesai sewa

    def __str__(self):
        return f"{self.nama_mobil} - {self.tgl_pengambilan} s/d {self.tgl_pengembalian}"
