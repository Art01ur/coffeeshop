from django.urls import path

from upload_data_to_db_first_time import defs_for_first_config
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>', views.product_details, name='product_details'),
    path('buy/<int:product_id>', views.product_buying, name='product_buying'),
    path('upload/data', defs_for_first_config.upload_data, name='upload'),

]


