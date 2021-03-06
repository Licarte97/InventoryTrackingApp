from django.urls import include, path
from rest_framework import routers
from product import views
from django.views.generic import TemplateView
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/groups', views.GroupViewSet)
router.register(r'api/products', views.ProductViewSet)
router.register(r'api/producttypes', views.ProductTypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/filtered-products/', views.ProductGenericView.as_view(), name="product"),
    path('api/filtered-producttypes/', views.ProductTypeGenericView.as_view(), name="producttypes"),
    path('products/', TemplateView.as_view(template_name='index.html')),
]
