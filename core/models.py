from django.db import models

class IpUsage(models.Model):
    ip = models.CharField(max_length=16, primary_key=True)
    date = models.DateField(auto_now_add=True)
    usage = models.IntegerField(default=0)

    def __str__(self):
        return "%s: %s usages on %s" % (self.ip, self.usage, self.date)