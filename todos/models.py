from django.db import models

from authentication.models import User

# Create your models here.


class Todo(models.Model):
    name = models.CharField(null=False, max_length=200)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    class StatusEnum(models.TextChoices):
        __ordering__ = ["Completed", "Ongoing", "Notstarted"]

        NotStarted = "NotStarted"
        OnGoing = "Ongoing"
        Completed = "Completed"

    status = models.CharField(
        choices=StatusEnum.choices, default=StatusEnum.NotStarted, max_length=10
    )

    def __str__(self):
        return self.name
