from django.urls import path
from myapp.views import HomeView, pdf_view, showcat, PdfView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('addpdf', PdfView.as_view(), name='addpdf'),
    path('pdf_view/<int:id>', pdf_view, name='pdf_view'),
    path('showcat/<int:id>', showcat, name='showcat'),
]
