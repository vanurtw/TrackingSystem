from django.urls import path
from .views import *

urlpatterns = [
    path('', TehniqueViewList.as_view(), name='tehnique'),
    path('det/', tehnique_detail, name='tehnique_detail'),
    path('tran/', tehnique_transport, name='tehnique_transport'),
]