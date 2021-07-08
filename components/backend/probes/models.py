from django.db import models


class Probe(models.Model):
    name = models.TextField(primary_key=True)

    def __str__(self):
        return self.name
