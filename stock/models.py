from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=30)
    ticker_code = models.CharField(max_length=6)
    class Meta:
        verbose_name_plural = "Companies"