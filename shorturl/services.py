from .models import Url
import pdb
import secrets


def check_available_short_url():
    """
    Returns: an available short url
    """
    short_url_found = False
    while not short_url_found:
        short_url = secrets.token_hex(3)
        if not Url.objects.filter(short_url=short_url):
            return short_url
