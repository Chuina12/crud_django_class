from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

class Produit(models.Model):
    nom_produit = models.CharField(max_length=50)
    prix = models.IntegerField()
    image = models.ImageField(upload_to='image')
    description = models.TextField()

    verbose_name=('Produit')
    verbose_name_plural =('Produit')
    class Meta:
        def __str__(self):
            return self.nom_produit