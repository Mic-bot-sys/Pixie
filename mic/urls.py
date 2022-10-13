from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view

schema_view = get_swagger_view(title='thenewcart')


urlpatterns = [
    path('', include('estore.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('open_api', schema_view),
]



urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
