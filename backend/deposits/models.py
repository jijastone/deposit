from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class OKATO(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'OKATO'
        verbose_name_plural = 'OKATO'

    def __str__(self):
        return f'{self.name}'


class Deposit(models.Model):
    okato = models.ForeignKey(OKATO, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Месторождение'
        verbose_name_plural = 'Месторождения'

    def __str__(self):
        return f'{self.name}'


class OPI(models.Model):
    code = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'OPI'
        verbose_name_plural = 'OPI'

    def __str__(self):
        return f'{self.name}'


class Сoordinates(models.Model):
    title = models.CharField(max_length=128)
    long = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return f'{self.title}'


class Owner(models.Model):
    name = models.CharField(
        'Название пользователя',
        max_length=50)
    address = models.CharField(
        'Юр. адрес',
        max_length=50)
    email = models.CharField(
        'Почта',
        max_length=50)
    number = models.CharField(
        'номер',
        max_length=8)


    class Meta:
        ordering = ['name']
        verbose_name = 'Недропользователь'
        verbose_name_plural = 'Недропользователи'
        constraints = [models.UniqueConstraint(
            fields=['name', 'address'],
            name='unique_name_address'
        )]

    def __str__(self):
        return f'{self.name}, {self.address}.'


class Area(models.Model):
    name = models.CharField(
        'Название участка',
        max_length=50)
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE)
    coordinates = models.ManyToManyField(
        Сoordinates,
        related_name='area'
    )
    owners = models.ManyToManyField(
        Owner,
        through='License')
    opi = models.ManyToManyField(OPI)
    category_a = models.PositiveSmallIntegerField('A')
    category_b = models.PositiveSmallIntegerField('B')
    category_c1 = models.PositiveSmallIntegerField('C1')
    category_c2 = models.PositiveSmallIntegerField('C2')
    year_estimation = models.DateField()

    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'

    def __str__(self):
        return self.name


class License(models.Model):

    area = models.ForeignKey(
        Area,
        related_name='arealicense',
        on_delete=models.CASCADE,
        verbose_name='Участок'
    )
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        verbose_name='Недропользоваетль'

    )
    number = models.CharField(
        'Номер Лицензии',
        max_length=50)
    registration = models.DateField('Дата регистрации')
    end_date = models.DateField('Срок окончания')

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'
        constraints = [models.UniqueConstraint(
            fields=['owner', 'area'],
            name='unique_owner_area'
        )]
