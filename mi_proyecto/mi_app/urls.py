from django.urls import path
from . import views
urlpatterns = [
    path('ingresar_persona/',views.ingresar_persona, name='ingresar_persona'),
    path('ver_personas/',views.ver_personas, name='ver_personas'),
]