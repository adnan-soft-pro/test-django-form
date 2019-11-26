import django_tables2 as tables

from django_tables2.utils import A
from python_test.models import Client


class ClientTable(tables.Table):

    class Meta:
        model = Client
        attrs = {
            "class": "table table-bordered table-striped table-hover",
            "id": "clientTable"
        }
        row_attrs = {
            'data-href': lambda record: '/update-client/{}/'.format(record.pk)
        }
        empty_text = "No clients matched to the search criteria!"
