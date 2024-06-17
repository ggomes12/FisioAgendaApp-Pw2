from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class AuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **Kwargs):
        User = get_user_model()
        try:
            clients = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            if clients.check_password(password):
                return clients
        return None
