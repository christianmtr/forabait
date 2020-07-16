from django.db import models


class Sauce(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
