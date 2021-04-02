from rest_framework import viewsets
from users.serializer import User, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing User instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
