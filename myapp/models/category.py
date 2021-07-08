from django.db import models


class PdfCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
