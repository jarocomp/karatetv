from django.urls import path
from . import views

urlpatterns = [
   path('', views.domov, name="domov"),
   path('onas', views.onas, name="onas"),
   path('treneriaasistenti', views.treneriaasistenti, name="treneriaasistenti"),
   path('treningy', views.treningy, name="treningy"),
   path('poriadok', views.poriadok, name="poriadok"),
   path('prihlaska', views.prihlaska, name="prihlaska"),
   path('kontakt', views.kontakt, name="kontakt"),
   path('trebisov', views.trebisov, name="trebisov"),
   path('admin', views.admin, name="admin"),



]
