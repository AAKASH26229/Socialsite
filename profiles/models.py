from django.db import models
from django.conf import settings

CONNECTION_STATUS_PENDING = "pending"
CONNECTION_STATUS_CONFIRMED = "confirmed"

CONNECTION_STATUS_CHOICES = (
    (CONNECTION_STATUS_PENDING, "Pending"),
    (CONNECTION_STATUS_CONFIRMED, "confirmed"),
)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, default="")

    def __str__(self):
        return "{}".format(self.user.phone_number)


class Connection(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user2")
    status = models.CharField(
        max_length=15, choices=CONNECTION_STATUS_CHOICES, default="pending"
    )
    
    def __str__(self):
        return "{} - {}".format(self.user1, self.user2)
