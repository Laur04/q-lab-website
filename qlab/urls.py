from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('', include('qlab.apps.base.urls', namespace='base')),
    path('projects/', include('qlab.apps.projects.urls', namespace='projects')),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
