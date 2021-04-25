from django.shortcuts import render
from django.views import generic
from .models import Bill

# Create your views here.
class IndexView(generic.ListView):
    template_name = "bill/index.html"
    context_object_name = "bills_list"

    def get_queryset(self):
        return Bill.objects.order_by("generated_on")


class DetailView(generic.DetailView):
    model = Bill
    template_name = "bill/details.html"


class AddView(generic.CreateView):
    model = Bill
    template_name = "bill/add.html"
    fields = "__all__"
