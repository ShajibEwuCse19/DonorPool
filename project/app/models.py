from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
import hashlib
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

GENDERS = [
    ("M", "Male"),
    ("F", "Female"),
]
OCCUPATIONS = [
    ("Student", "Student"),
    ("Doctor", "Doctor"),
    ("Engineer", "Engineer"),
]
BLOOD_GROUPS = [
    ("a_positive",'A+'),
    ("a_negative","A-"),
    ("b_positive",'B+'),
    ("b_negative","B-"),
    ("ab_positive","AB+"),
    ("ab_negative","AB-"),
    ("o_positive","O+"),
    ("o_negative",'O-'),

]

class User(AbstractUser):
    blood_group = models.CharField(max_length=11, choices=BLOOD_GROUPS)

    gender = models.CharField(max_length=1, choices=GENDERS)
    occupation = models.CharField(max_length=20, choices=OCCUPATIONS)
    workplace = models.CharField(max_length=1024, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone_number = PhoneNumberField()
    district = models.CharField(max_length=100,null=True, blank=True)
    present_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    last_blood_donation_date = models.DateField(null=True)

    @property
    def get_next_donation_date(self) -> str:
        if self.last_blood_donation_date:
            return self.last_blood_donation_date + datetime.timedelta(6 * 30)
        else:
            return ""

    @property
    def md5_email(self) -> str:
        return hashlib.md5(self.email.strip().lower().encode("utf-8")).hexdigest()
