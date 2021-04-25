from django.db import models
from django.urls import reverse


class Bill(models.Model):
    generated_on = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=200)
    total_units_consumed = models.IntegerField("Units of electricity consumed")
    amount_payable = models.FloatField("Due Amount")
    image_of_meter = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse("bill:detail", kwargs={"pk": self.pk})
