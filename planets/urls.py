from planets import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('planet/list', views.PlanetList.as_view(), name='planet_list'),
    path('planet/add', views.AddPlanet.as_view(), name='add_planet'),
    path('planet/edit/<int:pk>', views.EditPlanet.as_view(),
         name='planet_form'),
    path('planet/delete/<int:pk>', views.DeletePlanet.as_view(),
         name='delete_planet'),
]
