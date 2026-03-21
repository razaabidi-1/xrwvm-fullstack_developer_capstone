from rest_framework import viewsets, permissions
from .models import Dealer, CarMake, CarModel, Review
from .serializers import DealerSerializer, CarMakeSerializer, CarModelSerializer, ReviewSerializer

class DealerViewSet(viewsets.ModelViewSet):
	queryset = Dealer.objects.all()
	serializer_class = DealerSerializer
	permission_classes = [permissions.AllowAny]

class CarMakeViewSet(viewsets.ModelViewSet):
	queryset = CarMake.objects.all()
	serializer_class = CarMakeSerializer
	permission_classes = [permissions.AllowAny]

class CarModelViewSet(viewsets.ModelViewSet):
	queryset = CarModel.objects.all()
	serializer_class = CarModelSerializer
	permission_classes = [permissions.AllowAny]

class ReviewViewSet(viewsets.ModelViewSet):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer
	permission_classes = [permissions.AllowAny]
