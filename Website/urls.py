#Website urls 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('location', views.location, name='location'),
    path('<int:home_id>', views.home_detail, name='home_detail'),
    path('reservations/<int:home_id>/', views.make_reservation, name='make_reservation'),  # Update view function name here
    path('reservation-success/', views.reservation_success, name='reservation_success'),
    path('filter-homes/', views.filter_homes, name='filter_homes'), 
    path('about-us/', views.about_us, name='about_us'),
    path('contactus-success/', views.contact_us_success, name='contact_us_success'),
    path('details/<int:home_id>/', views.home_detail, name='home_detail'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
]