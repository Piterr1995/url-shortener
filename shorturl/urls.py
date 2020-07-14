from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("/url-generator/", views.url_generator, name="url-generator"),
    path("<str:shortened_url>/", views.link_redirect, name="link-redirect"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
