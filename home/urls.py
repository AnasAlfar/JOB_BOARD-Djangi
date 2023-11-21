from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home,name="home"),
    path('testimonial/',views.testimonial,name="testimonial"),
    path('create_testimonial/',views.create_testimonial,name="create_testimonial"),
]
    
