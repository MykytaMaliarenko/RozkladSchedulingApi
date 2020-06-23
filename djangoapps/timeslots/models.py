from django.db import models


class TimeSlot(models.Model):
    """ TimeSlot Model """
    id = models.IntegerField(primary_key=True)
    startTime = models.TimeField()
    endTime = models.TimeField()

    class Meta:
        db_table = "time_slot"

    def __repr__(self):
        return f"<TimeSlot id={self.id}>"
