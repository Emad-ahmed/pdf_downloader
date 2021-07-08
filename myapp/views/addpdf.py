from django.shortcuts import render, redirect
from django.views import View
from myapp.models import PdfBook, PdfCategory
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from myapp.forms import PdfForm


class PdfView(View):
    def get(self, request):
        fm = PdfForm()
        return render(request, 'addpdf.html', {'form': fm})

    def post(self, request):
        fm = PdfForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
        return render(request, 'addpdf.html', {'form': fm})
