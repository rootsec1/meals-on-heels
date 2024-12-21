from django.db import models


# Generic Timestamp model
class AutoTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FoodTruckModel(AutoTimeStampModel):
    location_id = models.BigIntegerField(primary_key=True, unique=True)
    applicant = models.CharField(max_length=255, null=True, default=None)
    facility_type = models.CharField(max_length=50, null=True, default=None)
    cnn = models.BigIntegerField()
    location_description = models.TextField(null=True, default=None)
    address = models.TextField(null=True, default=None)
    blocklot = models.CharField(max_length=32, null=True, default=None)
    block = models.CharField(max_length=32, null=True, default=None)
    lot = models.CharField(max_length=32, null=True, default=None)
    permit = models.CharField(max_length=64, null=True, default=None)
    status = models.CharField(max_length=64, null=True, default=None)
    food_items = models.TextField(blank=True, null=True, default=None)
    x = models.FloatField()
    y = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    schedule_url = models.URLField()
    days_hours = models.CharField(max_length=255, null=True, default=None)
    noi_sent = models.CharField(max_length=64, null=True, default=None)
    received = models.IntegerField(blank=True, null=True)
    prior_permit = models.BooleanField()
    location = models.CharField(max_length=255, null=True, default=None)
    fire_prevention_districts = models.IntegerField()
    police_districts = models.IntegerField()
    supervisor_districts = models.IntegerField()
    zip_codes = models.IntegerField()
    neighborhoods_old = models.IntegerField()

    def __str__(self):
        return f"{self.applicant} ({self.address})"
