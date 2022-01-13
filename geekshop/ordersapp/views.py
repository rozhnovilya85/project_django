from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class OrderListView(ListView):
    pass

class CreateListView(CreateView):
    pass

class UpdateListView(UpdateView):
    pass

class DetailListView(DetailView):
    pass

class DeleteListView(DeleteView):
    pass

def complete():
    pass

