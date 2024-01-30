
from django.urls import path
from .views import index, home, isa, calc_tension
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    path('isa', isa, name='isa'),
    path('calc_tension', calc_tension, name='calc_tension'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)