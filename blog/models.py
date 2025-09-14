# blog/models.py
from django.db import models

class Post(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField()
    tanggal_publikasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul