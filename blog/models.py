# blog/models.py

from django.db import models

class Product(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField(blank=True, null=True)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField(default=0)
    gambar = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.nama