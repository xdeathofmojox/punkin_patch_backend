from django.urls import path
from . import views

app_name = "punkin_patch"

urlpatterns = [
    path('', views.punkinpatch),
    path('characters/', views.CharactersView.as_view()),
    path('character/add/', views.CharacterCreateView.as_view(), name='character-add'),
    path('character/<int:pk>/', views.CharacterUpdateView.as_view(), name='character-update'),
    path('character/<int:pk>/delete/', views.CharacterDeleteView.as_view(), name='character-delete'),
    ]