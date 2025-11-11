from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', lambda request: redirect('home')),  # redirects root (/) to /home/

    path('about/', views.about, name='about'),

    path('events/', views.events, name='events'),

    path('gallery/', views.gallery, name='gallery'),

    path('prayer_request/', views.prayer_request, name='prayer_request'),

    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),

    path('contact/', views.contact, name='contact'),

    path('donate/', views.donate, name='donate'),

    path('membership/', views.membership, name='membership'),

    path('ministries/', views.ministries, name='ministries'),

    path('sermons/', views.sermons, name='sermons'),

    path('testimonies/', views.testimonies, name='testimonies'),

    path('live_stream/', views.live_stream, name='live_stream'),

    path('visit/', views.visit, name='visit'),
    


]
