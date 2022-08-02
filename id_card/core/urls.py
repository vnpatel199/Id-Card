from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.Login, name="login"),
    path("regestration", views.reg, name="reg"),
    path("card/<int:id>", views.idcard, name="idcard" )
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)