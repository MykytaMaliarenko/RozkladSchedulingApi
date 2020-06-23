from django.db import models


class Room(models.Model):
    """ University Room Model """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    university_building = models.IntegerField()

    class Meta:
        db_table = "room"
        ordering = ("-university_building",)

    def __repr__(self):
        return f"<Room id={self.id} room_name='{self.name}' university_building={self.university_building}>"
