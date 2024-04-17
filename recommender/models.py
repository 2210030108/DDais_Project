from django.db import models

class WashingMachine(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ratings = models.FloatField()
    brand_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    washing_capacity = models.IntegerField()
    color = models.CharField(max_length=50)
    maximum_spin_speed = models.IntegerField()  # Add this field
    function_type = models.CharField(max_length=100)
    inbuilt_heater = models.BooleanField(default=False)
    washing_method = models.CharField(max_length=100)
    product_url = models.URLField()

    def __str__(self):
        return self.product_name