from django.contrib import admin
from .models import Dealer, CarMake, CarModel, Review

admin.site.register(Dealer)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Review)
