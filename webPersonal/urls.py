from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'webPersonal'
urlpatterns = [
    path('', views.index_view, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)