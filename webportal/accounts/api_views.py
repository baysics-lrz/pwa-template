from .models import User
from .serializers import UserSerializer
from rest_framework.generics import RetrieveAPIView


class RetrieveAuthenticatedUser(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
