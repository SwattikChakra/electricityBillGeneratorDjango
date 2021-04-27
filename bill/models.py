from django.db import models
from django.urls import reverse
from django import forms
CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]


class Bill(models.Model):
    generated_on = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=200)
    outstanding_dues = models.BooleanField()
    total_units_consumed = models.IntegerField("Units of electricity consumed")

    class duration(models.TextChoices):
        month1 = "1 Month"
        month3 = "3 Months"
        month6 = "6 Months"
    duration_of_bill = models.CharField(
        max_length=20, choices=duration.choices)
    amount_payable = models.FloatField("Due Amount")
    image_of_meter = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse("bill:detail", kwargs={"pk": self.pk})
