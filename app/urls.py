from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.my_view, name='index'),
    path('client_orders/<int:client_id>/', views.client_orders, name='client_orders'),
    path('client_products/<str:length>/<int:client_id>/', views.client_products, name='client_products'),
    path('product_image/', views.product_image, name='product_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)