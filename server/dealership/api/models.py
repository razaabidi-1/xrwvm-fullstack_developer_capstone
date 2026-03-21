from django.db import models
from django.contrib.auth.models import User

class Dealer(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=255)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=50)
	zip_code = models.CharField(max_length=20)
	email = models.EmailField()
	phone = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name} ({self.city}, {self.state})"

class CarMake(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

class CarModel(models.Model):
	make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="models")
	name = models.CharField(max_length=100)
	year = models.PositiveIntegerField()

	def __str__(self):
		return f"{self.make.name} {self.name} ({self.year})"

class Review(models.Model):
	dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name="reviews")
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	car = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True, blank=True)
	review_text = models.TextField()
	sentiment = models.CharField(max_length=20, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Review by {self.user.username} for {self.dealer.name}"
