from django.urls import path
from . import views

urlpatterns = [
   path('', views.domov, name="domov"),
   path('onas', views.onas, name="onas"),
   path('treneriaasistenti', views.treneriaasistenti, name="treneriaasistenti"),
   path('treningy', views.treningy, name="treningy"),
   path('dokumenty', views.dokumenty, name="dokumenty"),
   path('kontakt', views.kontakt, name="kontakt"),
   path('trebisov', views.trebisov, name="trebisov"),
   path('secovce', views.post_list_se, name="secovce"),
   path('admin', views.admin, name="admin"),
   path('post/listse', views.post_list_se, name='post_list_se'),
   path('post/<int:pk>/', views.post_detail, name='post_detail'),
   path('post/new/', views.post_new, name='post_new'),
   path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
 


]
