from django.urls import path

from app.views import index_view, contact_view

urlpatterns = [
    path('', index_view, name='index'),
    path('contact/', contact_view, name='contact'),
]