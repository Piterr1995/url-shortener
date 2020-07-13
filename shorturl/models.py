from django.db import models


class Url(models.Model):
    long_url = models.CharField(max_length=300)
    short_url = models.CharField(max_length=8)

    def __str__(self):
        return self.long_url

    # def save(self, *args, **kwargs):
    #     super(Url, self).save(*args, **kwargs)
    #     self.short_url = secrets.token_hex(3)
