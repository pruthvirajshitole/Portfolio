from django.contrib import admin
from django.urls import path
from Portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('education/', views.education, name='education'),  
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'),
]
