from django.urls import path

from core import views

app_name = 'core'
urlpatterns = [
    path('employee/<int:pk>', views.get_orders_by_employee, name='employee'),
    path('employee', views.get_employee_statistics, name='employee-list'),
    path('client/<int:pk>', views.get_orders_by_clients, name='client'),
]
