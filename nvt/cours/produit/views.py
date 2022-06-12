from ast import Delete
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from . form import Ajout, UserForm
from . models import Produit
from django.contrib import messages
from django.urls import path
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import  authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin

class produitCreateView(LoginRequiredMixin, CreateView):
    model = Produit
    form_class= Ajout
    success_url = '/ajout'
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Votre product a ete enregistre')
        return super().post(request, *args, **kwargs)
    
    
    
class produitListView(ListView):
    model = Produit
    template_name = 'affiche.html'
    def get_queryset(self):
        return super().get_queryset()
    
class produitUpdateView(UpdateView):
    model = Produit
    form_class = Ajout
    template_name = 'modifier.html'
    success_url ='/affiche'
    
class produitDeleteView(DeleteView):
    model = Produit
    template_name ='supprimer.html'
    success_url='/affiche'
    
class produitDetailView(DetailView):
    model = Produit
    template_name = 'detail.html'
    
    
@login_required(login_url='/login')    
def addProduct(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        file = request.FILES.get('image')
        if name and description and price and file:
            Produit.objects.create(nom_produit=name, description=description, prix=price, image=file)
            messages.success(request, 'product has been added')
        else:
            messages.error(request, 'Data has been rejected!')   
    return render(request, 'add.html') 


def log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'you are logged!!')
        else:
            messages.error(request, 'Hello sorry your password and username are not matching!!! try again')   
    return render(request, 'auth/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Congratulation!! your account has been created successfully!!')
    else:
        messages.error(request, form.errors)
    return render(request, 'auth/register.html', {'form':form})

def outfuc(request):
    logout(request)
    return redirect('affiche')        
        



                   