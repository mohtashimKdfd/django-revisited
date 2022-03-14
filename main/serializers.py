from rest_framework import serializers
from main.models import Users

class UsersSerializer(serializers.Serializer):
    class Meta:
        model = Users
        fields = ('__all__')