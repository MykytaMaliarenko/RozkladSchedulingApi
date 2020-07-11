from django.db import models


class TimeSlot(models.Model):
    """ TimeSlot Model """
    id = models.IntegerField(primary_key=True)
    time_start = models.TimeField()
    time_end = models.TimeField()

    class Meta:
        db_table = "time_slot"

    def __repr__(self):
        return f"<TimeSlot id={self.id}>"
