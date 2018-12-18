from django.conf.urls import url
from aplicacion import views

urlpatterns = [
	url(r'^receta/$', views.receta_list, name = 'receta_list'),
]
