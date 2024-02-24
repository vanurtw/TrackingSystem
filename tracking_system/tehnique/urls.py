from django.urls import path
from .views import *

urlpatterns = [
    path('', TehniqueViewList.as_view(), name='tehnique'),
    path('technique-detail/<int:pk>/', TechniqueDetailView.as_view(), name='tehnique_detail'),
    path('tran/', tehnique_transport, name='tehnique_transport'),
]