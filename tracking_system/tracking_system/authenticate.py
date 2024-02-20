from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user_model = get_user_model()
            user = user_model.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except:
            return None

    def get_user(self, user_id):
        try:
            user_model = get_user_model()
            user = user_model.objects.get(id=user_id)
            return user
        except:
            return None
