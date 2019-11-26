import django_filters as filters

from python_test.models import Client


class ClientFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name='name', lookup_expr='icontains', label="Client Name")
    suburb = filters.CharFilter(
        field_name='suburb', lookup_expr='icontains', label="Suburb")
    phone_number = filters.CharFilter(
        field_name='phone_number', lookup_expr='icontains', label="Phone")
    email_address = filters.CharFilter(
        field_name='email_address', lookup_expr='icontains', label="Email Address")

    class Meta:
        model = Client
        fields = ('name', 'email_address', 'suburb', 'phone_number')
        order_by = ("pk",)
