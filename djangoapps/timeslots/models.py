from django.db import models


class TimeSlot(models.Model):
    """ TimeSlot Model """
    id = models.IntegerField(primary_key=True)
    timeStart = models.TimeField()
    timeEnd = models.TimeField()

    class Meta:
        db_table = "time_slot"

    def __repr__(self):
        return f"<TimeSlot id={self.id}>"
