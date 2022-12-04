from django.urls import path
from . import views

urlpatterns = [
    path('', views.punkinpatch),
    path('characters/', views.CharactersView.as_view())
]