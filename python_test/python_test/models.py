from django.db import models


class Client(models.Model):
    name = models.CharField(
        verbose_name='Client Name', max_length=255, unique=True, blank=False)
    street_name = models.CharField(
        verbose_name='Street Name', max_length=255, blank=True)
    suburb = models.CharField(
        verbose_name='Suburb', max_length=255, blank=True)
    postcode = models.CharField(
        verbose_name='Postcode', max_length=255, blank=True)
    state = models.CharField(
        verbose_name='State', max_length=16, blank=True)
    contact_name = models.CharField(
        verbose_name='Contact Name', max_length=255, blank=True)
    email_address = models.EmailField(
        verbose_name='Email Address', max_length=255, blank=False)
    phone_number = models.CharField(
        verbose_name='Phone Number', max_length=100, blank=False)
