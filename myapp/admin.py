from django.contrib import admin
from myapp.models import PdfBook, PdfCategory
# Register your models here.


@admin.register(PdfBook)
class PdfBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'uploaded_at']


@admin.register(PdfCategory)
class PdfCategoryMainAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
