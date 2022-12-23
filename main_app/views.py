from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Animal, Clothes
from .forms import FeedingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def animals_index(request):
  animals = Animal.objects.all()
  return render(request, 'animals/index.html', { 'animals': animals })

class AnimalList(ListView):
  model = Animal
  template_name = 'animals/index.html'

class AnimalCreate(CreateView):
  model = Animal
  fields = ['name', 'animal', 'breed', 'description', 'age']
  success_url = '/animals/'

class AnimalUpdate(UpdateView):
  model = Animal
  fields = ['breed', 'description', 'age']

class AnimalDelete(DeleteView):
  model = Animal
  success_url = '/animals/'

def animals_detail(request, animal_id):
  animal = Animal.objects.get(id=animal_id)
  id_list = animal.clothes.all().values_list('id')
  clothes_animal_doesnt_have = Clothes.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'animals/detail.html', { 'animal': animal, 'feeding_form': feeding_form, 'clothes': clothes_animal_doesnt_have })

def add_feeding(request, animal_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.animal_id = animal_id
    new_feeding.save()
  return redirect('detail', animal_id=animal_id)

class ClothesList(ListView):
  model = Clothes

class ClothesDetail(DetailView):
  model = Clothes

class ClothesCreate(CreateView):
  model = Clothes
  fields = '__all__'

class ClothesUpdate(UpdateView):
  model = Clothes
  fields = ['name', 'color']

class ClothesDelete(DeleteView):
  model = Clothes
  success_url = '/clothes/'


def assoc_clothes(request, animal_id, c_id):
  Animal.objects.get(id=animal_id).clothes.add(c_id)
  return redirect('detail', animal_id=animal_id)

def unassoc_clothes(request, animal_id, c_id):
  animal = Animal.objects.get(id=animal_id)
  animal.clothes.remove(c_id)
  return redirect('detail', animal_id=animal_id)