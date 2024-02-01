
from django.urls import path
from .views import home, isa, calc_tension, name_inst, data_sheet, construction, open_external_web
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('isa', isa, name='isa'),
    path('calc_tension', calc_tension, name='calc_tension'),
    path('name_inst', name_inst, name='name_inst'),
    path('data_sheet', data_sheet, name='data_sheet'),
    path('construction', construction, name='construction'),
    path('open_external_web', open_external_web, name='open_external_web'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)