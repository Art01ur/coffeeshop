from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from shop.models import Type, Product
from .authentication import CustomAuthentication


class TypeResource(ModelResource):
    class Meta:
        queryset = Type.objects.all()
        resource_name = 'types'
        allowed_methods = ['get']


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'products'
        allowed_methods = ['get', 'post', 'delete']
        excludes = ['created_at']
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.type_id = bundle.data['type_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['type_id'] = bundle.obj.type_id
        bundle.data['type'] = bundle.obj.type
        return bundle

    def dehydrate_title(self, bundle):
        return bundle.data['name'].upper()
