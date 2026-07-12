from django.db import models

from .validators import validate_non_negative


class Product(models.Model):
    name = models.CharField(max_length=150)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[validate_non_negative]
    )

    quantity = models.IntegerField(
        default=0,
        validators=[validate_non_negative]
    )

    delivery_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[validate_non_negative]
    )

    def get_id_and_name(self):
        return f'{self.id} - {self.name}'

    def get_total_sum(self):
        return self.price * self.quantity + self.delivery_price

    def __str__(self):
        return self.get_id_and_name()
