from django.db import models


class Teacher(models.Model):
    """ Teacher Model """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    official_name = models.CharField(max_length=50)

    class Meta:
        db_table = "teacher"
        ordering = ("name",)

    def __repr__(self):
        return f"<Teacher id={self.id} name='{self.name}' official_name='{self.official_name}'>"
