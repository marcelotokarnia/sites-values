from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=1024, primary_key=True)

    def __str__(self):
        return '%s: %s' % (self.pk, self.name)

class Value(models.Model):
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