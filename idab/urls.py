from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as url_docs
import debug_toolbar
from django.views.generic import TemplateView
from users.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path to djoser end points
    path('auth/', include('djoser.urls')),
    # path to my app's endpoints
    path("api/", include("users.urls")),
    path("api/", include("siteblocks.urls")),
    path("api/", include("bids.urls")),
    path("api/", include("programs.urls")),
    path("api/", include("courses.urls")),
    path("api/", include("tutorials.urls")),
    path("api/", include("schedule.urls")),
    path("api/", include("tasks.urls")),
    path("api/", include("library.urls")),
    path("api/", include("studymaterials.urls")),
    path("api/", include("slack.urls")),
    path("api/", include("attendances.urls")),
    path("api/", include("ratings.urls")),
    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # Token Access Create/Refresh
    path('auth/jwt/create/', MyTokenObtainPairView.as_view(), name='lk_login'),
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),

urlpatterns += url_docs
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]