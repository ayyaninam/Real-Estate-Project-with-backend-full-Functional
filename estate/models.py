from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Propertie(models.Model):
    purpose_choice = (
    ("BUY", "BUY"),
    ("SELL", "SELL"),
    ("RENT", "RENT"),
)
    unit_choice = (
    ("MARLA", "MARLA"),
    ("Kanal", "Kanal"),
)
    category_choice = (
    ("Plots", "Plots"),
    ("Houses", "Houses"),
    ("Appartment", "Appartment"),
    ("Commercial", "Commercial"),
)
    location_choice = (
    ("Lahore", "Lahore"),
    ("Gujranwala", "Gujranwala"),
    ("Faisalabad", "Faisalabad"),
)
    sno = models.AutoField(primary_key=True)
    purpose = models.CharField(choices=purpose_choice,max_length=2000)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="properties_uploads")
    area = models.IntegerField()
    unit = models.CharField(choices=unit_choice,max_length=2000)
    price = models.IntegerField()
    category = models.CharField(choices=category_choice,max_length=2000)
    city = models.CharField(choices=location_choice,max_length=2000)
    full_location = models.CharField(max_length=2000)
    description = models.CharField(max_length=20000)
    name = models.CharField(max_length=2000)
    number = models.CharField(max_length=2000)
    email = models.CharField(max_length=2000)
    posted_by = models.IntegerField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}, {self.title}, {self.price}"

class Email(models.Model):
    email = models.CharField(max_length=300)
    def __str__(self):
        return f"{self.email}"

class Dealer_Register(models.Model):
    eligible_choice = (
        ("YES","YES"),
        ("NO","NO"),
    )
    sno = models.AutoField(primary_key=True)
    age = models.IntegerField()
    request_by = models.CharField(max_length=300)
    current_phone_number = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    address_2 = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    zip = models.CharField(max_length=300)
    eligible = models.CharField(choices=eligible_choice ,max_length=5, default="NO")
    def __str__(self):
        return f"{self.sno}"
