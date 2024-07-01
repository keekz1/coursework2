from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Booking.views import ChangePasswordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('Booking.urls')), 
    path('', include('Cart.urls')),  
     path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('', include('django.contrib.auth.urls')),  
]

# Serve static and media files during development

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)