from django.contrib import admin
from django.urls import path, include

# to access media file or directory
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('users/', include('accounts.urls')),  # Include the accounts app URLs
    path('',include('vege.urls')),
]


# to access media file or directory
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
