from python_test.models import Client
from python_test.forms import ClientForm
from python_test.tables import ClientTable
from python_test.filters import ClientFilter

from django.views.generic import View
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.shortcuts import render, redirect, get_object_or_404


class ClientListView(SingleTableMixin, FilterView):
    model = Client
    table_class = ClientTable
    filterset_class = ClientFilter
    template_name = "view_clients.html"


class ClientCreateView(View):

    def get(self, request, *args, **kwargs):
        client_form = ClientForm()

        return render(request, 'action_client.html', {
            'client_form': client_form,
            'client_title': 'New'
        })

    def post(self, request, *args, **kwargs):
        client_form = ClientForm(request.POST)

        if client_form.is_valid():
            client_form.save()
            return redirect('view_clients')
        return render(request, 'action_client.html', {
            'client_form': client_form,
            'client_title': 'New'
        })


class ClientUpdateView(View):

    def get(self, request, *args, **kwargs):
        client_id = kwargs.get('client_id', None)
        client = get_object_or_404(Client, pk=client_id)
        client_form = ClientForm(instance=client)

        return render(request, 'action_client.html', {
            'client_form': client_form,
            'client_title': 'Update'
        })

    def post(self, request, *args, **kwargs):
        client_id = kwargs.get('client_id', None)
        client = get_object_or_404(Client, pk=client_id)
        client_form = ClientForm(request.POST, instance=client)

        if client_form.is_valid():
            client_form.save()
            return redirect('view_clients')
        return render(request, 'action_client.html', {
            'client_form': client_form,
            'client_title': 'Update'
        })
