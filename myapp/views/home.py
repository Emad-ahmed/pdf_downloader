from django.shortcuts import render, redirect
from django.views import View
from myapp.models import PdfBook, PdfCategory
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound


class HomeView(View):
    def get(self, request):
        data = PdfBook.objects.all()
        mycategory = PdfCategory.objects.all()
        for i in data:
            print(i.document)
        return render(request, 'home.html', {'data': data, 'mycategory': mycategory})

    def post(self, request):
        search = request.POST.get('search')
        data = PdfBook.objects.filter(title=search)
        mycategory = PdfCategory.objects.all()
        return render(request, 'home.html', {'data': data, 'mycategory': mycategory})


def pdf_view(request, id):

    maindata = PdfBook.objects.get(pk=id)
    mainfile = maindata.document

    fs = FileSystemStorage()
    filename = str(mainfile)

    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # user will be prompted display the PDF in the browser
            response['Content-Disposition'] = 'inline; filename="filename"'

            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')


def showcat(request, id):
    if request.method == "POST":
        search = request.POST.get('search')
        data = PdfBook.objects.filter(title=search)
        mycategory = PdfCategory.objects.all()
        return render(request, 'home.html', {'data': data, 'mycategory': mycategory})

    mycategory = PdfCategory.objects.all()
    category = PdfCategory.objects.get(pk=id)
    data = PdfBook.objects.filter(category=category)
    return render(request, 'home.html', {'data': data, 'mycategory': mycategory, })
