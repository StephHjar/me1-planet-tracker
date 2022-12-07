from planets import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('planet_list/', views.PlanetList.as_view(), name='planet_list'),
    path('add_planet/', views.AddPlanet.as_view(), name='add_planet'),
    path('edit_planet/<pk>', views.EditPlanet.as_view(),
         name='planet_form'),
    path('delete_planet/<int:pk>', views.DeletePlanet.as_view(),
         name='delete_planet'),
]
