from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


UserModel = get_user_model()


class EmailModelBackend(ModelBackend):
    def authenticate(self, request, email, password, **kwargs):
        try:
            user = UserModel.objects.get(email=email)

            if (
                user.check_password(password) and
                self.user_can_authenticate(user)
            ):
                return user
        except UserModel.DoesNotExist:
            return None

        return None
