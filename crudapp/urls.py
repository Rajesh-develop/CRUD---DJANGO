from django.urls import path
from . import views

urlpatterns = [
    path('create_order/', views.orderFormView, name='order_url'),
    path('show_orders/', views.showView, name='show_url'),
    path('update_order/<int:f_oid>', views.updateView, name= 'update_url'),
    path('delete_order/<int:f_oid>', views.deleteView, name= 'delete_url'),
]