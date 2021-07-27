
from django.conf import settings
from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import training_prn_admin

app_name = 'training_prn'

urlpatterns = [
    path('admin/', training_prn_admin.urls),
    path('', RedirectView.as_view(url='admin/'), name='home_url'),
]

if settings.APP_NAME == 'training_prn':
    from django.contrib import admin

    urlpatterns += [
        path('admin/', admin.site.urls),
    ]
