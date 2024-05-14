from django.contrib import admin
from django.contrib.admin import display

from .models import (Area, Owner, OPI, License, Сoordinates, OKATO, Deposit)


class LicenseInline(admin.TabularInline):
    model = License
    extra = 1


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',
                     'category_a', 'category_b', 'category_c1', 'category_c2')
    list_filter = ('name',)
    inlines = (
        LicenseInline,
    )



@admin.register(OPI)
class OPIAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

@admin.register(License)
class  LicenseAdmin(admin.ModelAdmin):
    list_display = ('number',)


@admin.register(OKATO)
class OKATOAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('name','id')


@admin.register(Сoordinates)
class СoordinatesAdmin(admin.ModelAdmin):
    list_display = ('long', 'lat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
