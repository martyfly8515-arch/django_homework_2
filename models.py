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


class IceCream(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название мороженого'
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[validate_non_negative],
        verbose_name='Цена'
    )

    def __str__(self):
        return self.name


class IceCreamKiosk(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название киоска'
    )

    address = models.CharField(
        max_length=200,
        verbose_name='Адрес'
    )

    ice_creams = models.ManyToManyField(
        IceCream,
        related_name='kiosks',
        blank=True,
        verbose_name='Мороженое'
    )

    def __str__(self):
        return self.name


class Parent(models.Model):
    full_name = models.CharField(
        max_length=150,
        verbose_name='ФИО родителя'
    )

    def __str__(self):
        return self.full_name


class Child(models.Model):
    full_name = models.CharField(
        max_length=150,
        verbose_name='ФИО ребёнка'
    )

    age = models.IntegerField(
        validators=[validate_non_negative],
        verbose_name='Возраст'
    )

    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='Родитель'
    )

    def __str__(self):
        return self.full_name