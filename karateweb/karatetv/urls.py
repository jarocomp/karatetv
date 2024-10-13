from django.urls import path
from . import views

urlpatterns = [
   path('', views.domov, name="domov"),
   path('onas', views.onas, name="onas"),
   path('treneriaasistenti', views.treneriaasistenti, name="treneriaasistenti"),
   path('treningy', views.treningy, name="treningy"),
   path('dokumenty', views.dokumenty, name="dokumenty"),
   path('kontakt', views.kontakt, name="kontakt"),
   path('trebisov', views.post_list_tv, name="trebisov"),
   path('secovce', views.post_list_se, name="secovce"),
   path('admin', views.admin, name="admin"),
   path('post/listse', views.post_list_se, name='post_list_se'),
   path('post/listtv', views.post_list_tv, name='post_list_tv'),
   path('post_se/<int:pk>/', views.post_detail_se, name='post_detail_se'),
   path('post_tv<int:pk>/', views.post_detail_tv, name='post_detail_tv'),
   path('post/newse/', views.post_new_se, name='post_new_se'),
   path('post/newtv/', views.post_new_tv, name='post_new_tv'),
   path('post/<int:pk>/edit_se/', views.post_edit_se, name='post_edit_se'),
   path('post/<int:pk>/edit_tv/', views.post_edit_tv, name='post_edit_tv'),
 


]
