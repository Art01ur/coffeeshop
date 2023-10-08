from django.urls import path, include
from tastypie.api import Api

from api.models import TypeResource, ProductResource

api = Api(api_name='v1')
api.register(ProductResource())
api.register(TypeResource())

urlpatterns = [
    path('', include(api.urls), name='index'),
]