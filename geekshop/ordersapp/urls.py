from django.urls import path
from ordersapp import views as ordersapp
app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderListView, name='list'),
    path('create/', ordersapp.CreateListView, name='create'),
    path('update/<pk>/', ordersapp.UpdateListView, name='update'),
    path('read/<pk>/', ordersapp.DetailListView, name='read'),
    path('delete/<pk>/', ordersapp.DeleteListView, name='delete'),
    path('complete/<pk>/', ordersapp.complete(), name='complete'),




]