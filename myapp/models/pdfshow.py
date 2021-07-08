from django.db import models
from myapp.models.category import PdfCategory


class PdfBook(models.Model):
    title = models.CharField(max_length=122)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(PdfCategory, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')
    coverpage_photo = models.ImageField(
        upload_to='images/', default='image.png')
    uploaded_at = models.DateTimeField(auto_now_add=True)
