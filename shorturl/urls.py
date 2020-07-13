from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("url-generator", views.url_generator, name="url-generator"),
    path("<str:shortened_url>/", views.link_redirect, name="link-redirect"),
]

urlpatterns += patterns(
    "",
    (
        r"^static/(?P<path>.*)$",
        "django.views.static.serve",
        {"document_root": settings.STATIC_ROOT},
    ),
)

