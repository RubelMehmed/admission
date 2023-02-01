from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('course_list', views.course_list, name="course_list"),
    path('contact/', views.contact, name="contact"),
    path('admit/', views.admit, name="admit"),
    path('admission/', views.admit_form, name="admit_form"),
    path('about/', views.about, name="about"),
    path('input_data/', views.input_data, name="input_data"),
    path('data_display/', views.data_display, name="data_display"),
    path('update/', views.update, name="update")
]
