from django.urls import path
from core.topiapp.views import myfirstview
from core.topiapp.views import mysecondview

urlpatterns = [
    path('uno/', myfirstview),
    path('dos/', myfirstview),
    path('tres/', mysecondview),
]
