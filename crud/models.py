from django.db import models


# Create your models here.
class Product(models.Model):
    name_product = models.CharField(
        verbose_name="Produto", max_length=100, null=False, blank=False
    )
    descryption = models.CharField(verbose_name="Descrição", max_length=255)
    price = models.DecimalField(verbose_name="Valor", max_digits=7, decimal_places=2)
    available = models.BooleanField(verbose_name="Disponível para venda", default=False)
