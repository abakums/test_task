from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="homepage"),
    path('logout/', views.log_out, name="logout"),
    path('add_info/', views.add_info, name="add_info"),
    path('my_profile/', views.my_profile, name="my_profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('all_users/', views.all_users, name="all_users")
]
