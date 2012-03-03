
from django.conf.urls.defaults import *
from models import *
from views import *
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from resource import *

urlpatterns = patterns('',

    (r'product/create/$', create_product),
    (r'product/list/$', list_product ),
    (r'product/edit/(?P<id>[^/]+)/$', edit_product),
    (r'product/view/(?P<id>[^/]+)/$', view_product),
    (r'^store/$', store_view),
    (r'^cart/view', view_cart),
    (r'^cart/view/(?P<id>[^/]+)/$', add_to_cart),
    (r'cart/clean', clean_cart),
    (r'API/cart/items', RESTforCart.as_view(resource=LineItemResource)),

    (r'order/create/$', create_order),
    (r'order/list/$', list_order),
    (r'order/edit/(?P<id>[^/]+)/$', edit_order),
    (r'order/view/(?P<id>[^/]+)/$', view_order),
)
