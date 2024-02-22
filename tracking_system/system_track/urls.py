from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('transferred-equipment', track_technique, name='track'),
    path('hand_over_technique/', hand_over_technique, name='hand-over-technique'),
]