from django.db import models


country_choices = (
    ('brasil','Brasil'),
    ('eua', 'EUA'),
    ('uruguai','Uruguai'),
)

uf_choices = (
    ('AC','Acre'),
    ('AL','Alagoas'),
    ('AP','Amapá'),
    ('AM','Amazonas'),
    ('BA','Bahia'),
    ('CE','Ceará'),
    ('DF','Distrito Fedral'),
)

class Home(models.Model):
    Pais = models.CharField(max_length=50, choices=country_choices, default='brasil')
    Estado = models.CharField(max_length=50, choices=uf_choices, default='BA')
    CEP = models.CharField(max_length=14)
    Rua = models.CharField(max_length=100)
    Número = models.CharField(max_length=5)
    Complemento = models.CharField(max_length=50)