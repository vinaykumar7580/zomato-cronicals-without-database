from django.urls import path
from .views import menu_view,remove_dish, update_availability, order_view, update_status_view, review_orders_view

urlpatterns = [
    path('', menu_view, name='menu'),
    path('menu/remove/<int:dish_id>/', remove_dish, name='remove_dish'),
    path('menu/update/<int:dish_id>/', update_availability, name='update_availability'),
    path('order/', order_view, name='order'),
    path('order/update/<int:order_id>/', update_status_view, name='update_status'),
    path('review_orders/', review_orders_view, name='review_orders'),
]
