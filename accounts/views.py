from rest_framework import generics

from accounts.serializer import UserSerializer
from accounts.models import User


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
