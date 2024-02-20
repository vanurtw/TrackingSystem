from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up/', sign_up, name='sign_up'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

]