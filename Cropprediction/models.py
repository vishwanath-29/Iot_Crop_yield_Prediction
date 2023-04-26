from django.db import models

# Create your models here
class Valuesfromsensor(models.Model):
    temperature = models.FloatField(db_column='TEMPERATURE', blank=True, null=True)  # Field name made lowercase.
    humidity = models.FloatField(db_column='HUMIDITY', blank=True, null=True)  # Field name made lowercase.
    moisture = models.FloatField(db_column='MOISTURE', blank=True, null=True)  # Field name made lowercase.
    ph = models.FloatField(db_column='Ph', blank=True, null=True)  # Field name made lowercase.
    eventprocessedutctime = models.DateTimeField(db_column='EventProcessedUtcTime', blank=True, null=False,primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VALUESFROMSENSOR'