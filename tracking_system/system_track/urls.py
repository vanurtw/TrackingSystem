from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('transferred-equipment', TrackView.as_view(), name='track'),
    path('hand_over_technique/', hand_over_technique, name='hand-over-technique'),
]