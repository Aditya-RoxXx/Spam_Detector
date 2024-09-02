from django.contrib.auth.backends import ModelBackend
from .models import NewUser

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = NewUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except NewUser.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        try:
            return NewUser.objects.get(pk=user_id)
        except NewUser.DoesNotExist:
            return None