
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import index, reset, reset_done, reset_confirm, reset_complete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('redefinir-senha/', reset, name="reset"),
    path('redefinicao-de-senha-enviada/', reset_done, name="reset_done"),
    path('redefindo-senha/<str:token>/<int:pk>/', reset_confirm, name="reset_confirm"),
    path('senha-redefinida/', reset_complete, name="reset_complete"),
    path('', index, name="index"),
    path('', include('accounts.urls', namespace="accounts")),
    path('', include('pets.urls', namespace="pets")),
    path('', include('products.urls', namespace="products")),
    path('', include('services.urls', namespace="services")),
    path('', include('schedules.urls', namespace="schedules")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)