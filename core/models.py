from django.db import models
from utils.model_utils import BaseModel

class Site(BaseModel):
    name = models.CharField(max_length=1024, unique=True)

    def __str__(self):
        return self.name

class Value(BaseModel):
    site = models.ForeignKey(Site, related_name="values", on_delete=models.CASCADE)
    date = models.DateField()
    a = models.FloatField()
    b = models.FloatField()

    def __str__(self):
        return '%s: %s on %s (a: %.2f, b: %.2f)' % (
            self.pk,
            self.site_id,
            self.date.isoformat(),
            self.a,
            self.b
        )