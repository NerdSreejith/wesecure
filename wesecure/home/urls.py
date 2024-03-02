from django.urls import path,include
from . import  views
urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about_us,name="about"),
    path('service/',views.service,name="service"),
    path('team/',views.team,name="team"),
    path('why/',views.why,name="why"),
    path('example/',views.example,name="example")

]