from rest_framework import serializers

from .models import User

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'encrypted_password')
        
from .models import Employee

class employeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'title', 'email', 'facial_keypoints')      