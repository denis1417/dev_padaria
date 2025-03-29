from django.db import models

class Produto(models.Model):
    produto=models.CharField('Produto', max_length=100)
    lote=models.CharField('Lote',max_length=50)
    validade=models.DateField('Data de Validade', null=False)

    def __str__(self):
      return self.produto