from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>', views.product_details, name='product_details'),
    path('buy/<int:product_id>', views.product_buying, name='product_buying')
]
