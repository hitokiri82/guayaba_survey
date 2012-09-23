from django.db import models


class Visit(models.Model):
    ip_address = models.IPAddressField(max_length=15)
    created_date = models.DateTimeField(auto_now_add=True)
    num_lawyers = models.IntegerField()
    answer1 = models.TextField()
    answer2 = models.TextField()
    email = models.EmailField(blank=True)
    country = models.TextField()
    city = models.TextField()
