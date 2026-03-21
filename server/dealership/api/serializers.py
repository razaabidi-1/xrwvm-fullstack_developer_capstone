from rest_framework import serializers
from .models import Dealer, CarMake, CarModel, Review
from django.contrib.auth.models import User

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
    make = CarMakeSerializer(read_only=True)
    class Meta:
        model = CarModel
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    dealer = DealerSerializer(read_only=True)
    car = CarModelSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
