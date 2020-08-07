from django.db import models
from djangoapps.rooms.models import Room
from djangoapps.teachers.models import Teacher
from djangoapps.groups.models import Group
from djangoapps.timeslots.models import TimeSlot


class Class(models.Model):
    """ University Class Model """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10)
    
    day_of_week = models.IntegerField()
    week_number = models.IntegerField()

    room = models.ForeignKey(Room, related_name="classes", on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name="classes")
    teacher = models.ForeignKey(Teacher, related_name="classes", on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, related_name="classes", on_delete=models.CASCADE)

    class Meta:
        db_table = "class"

    def __repr__(self):
        short_name = self.name[:10] + "..." if len(self.name) > 10 else self.name

        return f"<Class id={self.id} name='{short_name}' class_type='{self.type}' " \
               f"room_id={self.room_id} teacher_id={self.teacher_id} " \
               f"day_of_week={self.day_of_week} week_number={self.week_number} class_time_id={self.time_slot_id}>"
