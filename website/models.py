from django.db import models


country_choices = (
    ('brasil','Brasil'),
    ('eua', 'EUA'),
    ('uruguai','Uruguai'),
)

class Post(models.Model):
    Pais = models.CharField(max_length=50, choices=country_choices, default='brasil')
    CEP = models.CharField(max_length=14)
    Rua = models.CharField(max_length=100)
    Número = models.CharField(max_length=5)
    Complemento = models.CharField(max_length=50)