from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone', 'email', 'date_of_birth', 'gender', 'avatar', 'nationality',
                  )
