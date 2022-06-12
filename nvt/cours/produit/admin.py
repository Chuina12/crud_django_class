from django.contrib import admin
from . models import Produit


class ordre(admin.ModelAdmin):
    list_display = ('nom_produit', 'prix','image','description')

admin.site.register(Produit, ordre)





