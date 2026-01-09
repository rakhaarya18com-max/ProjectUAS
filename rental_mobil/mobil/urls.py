from django.urls import path
from . import views

urlpatterns = [
    # Path ini harus kosong agar menyambung dengan path di atas
    path('', views.mobil_list, name='mobil_list'),
    path('tambah/', views.mobil_create, name='mobil_create'),
    path('edit/<int:pk>/', views.mobil_update, name='mobil_update'),
    path('hapus/<int:pk>/', views.mobil_delete, name='mobil_delete'),
]