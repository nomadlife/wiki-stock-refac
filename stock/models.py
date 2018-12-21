from django.db import models

# Create your models here.

class Companies(models.Model):
    company_name = models.CharField(max_length=30)
    ticker_code = models.CharField(max_length=6)