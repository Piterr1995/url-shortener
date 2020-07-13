from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.views.generic import TemplateView
from .models import Url
from .services import check_available_short_url
import json


class IndexView(TemplateView):
    template_name = "shorturl/index.html"


def url_generator(request):
    """
    Creates a new Url instance
    Returns: JSON Response with shortened url
    """
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        url_received = data.get("urlToShorten")
        shortened_url = check_available_short_url()
        new_url = Url.objects.create(long_url=url_received, short_url=shortened_url)
        new_url.save()

        return JsonResponse(
            {"short_url": new_url.short_url, "long_url": new_url.long_url}
        )


def link_redirect(request, shortened_url: str):
    """
    Redirects to url associated with shortened url
    Args:
        shortened_url -> taken from the url
    
    """
    url = Url.objects.get(short_url=shortened_url)
    long_url = url.long_url
    return redirect(long_url)
