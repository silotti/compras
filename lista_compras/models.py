from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField(default=1)
    comprado = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        
    def __str__(self):
        status = '✓' if self.comprado else '✗'
        return f'{self.nome} ({self.quantidade}) {status}'
