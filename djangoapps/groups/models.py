from django.db import models

# Create your models here.


class Group(models.Model):
    """ Group Model """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)

    class Meta:
        db_table = "group"
        ordering = ["name"]

    def __str__(self):
        return f"<Group id={self.id} name='{self.name}'>"
