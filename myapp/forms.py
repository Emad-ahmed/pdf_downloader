from django import forms
from myapp.models import PdfBook


class PdfForm(forms.ModelForm):
    class Meta:
        model = PdfBook
        fields = ['title', 'description', 'category',
                  'document', 'coverpage_photo']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
