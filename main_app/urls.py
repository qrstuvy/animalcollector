from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('animals/', views.animals_index, name='index'),
  path('animals/<int:animal_id>/', views.animals_detail, name='detail'),
  path('animals/create/', views.AnimalCreate.as_view(), name='animals_create'),
  path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animals_update'),
  path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animals_delete'),
  path('animals/<int:animal_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('animals/<int:animal_id>/assoc_clothes/<int:c_id>/', views.assoc_clothes, name='assoc_clothes'),
  path('animals/<int:animal_id>/unassoc_clothes/<int:c_id>/', views.unassoc_clothes, name='unassoc_clothes'),

  path('clothes/', views.ClothesList.as_view(), name='clothes_index'),
  path('clothes/<int:pk>/', views.ClothesDetail.as_view(), name='clothes_detail'),
  path('clothes/create/', views.ClothesCreate.as_view(), name='clothes_create'),
  path('clothes/<int:pk>/update/', views.ClothesUpdate.as_view(), name='clothes_update'),
  path('clothes/<int:pk>/delete/', views.ClothesDelete.as_view(), name='clothes_delete'),
]