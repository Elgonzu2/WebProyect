from django.urls import path
from core.topiapp.views import myfirstview

urlpatterns = [
    path('uno/', myfirstview),
    path('dos/', myfirstview),
]
