from . import views
from django.urls import path
urlpatterns = [
    path('ajout', views.produitCreateView.as_view(template_name = 'ajout.html'), name='ajout'),
    path('affiche', views.produitListView.as_view(), name='affiche'),
    path('modifier/<int:pk>', views.produitUpdateView.as_view(), name='modifier'),
    path('supprimer/<int:pk>', views.produitDeleteView.as_view(), name='supprimer'),
    path('detail/<int:pk>', views.produitDetailView.as_view(), name='detail'),
    path('addproduct', views.addProduct, name='addproduct'),
    path('login', views.log, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.outfuc, name='logout'),

    
]
