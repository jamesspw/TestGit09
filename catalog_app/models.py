from django.db import models

# Create your models here.
VOID_CHOICES = (
    ("0", "0"),
    ("1", "1")
)

class MyUser(models.Model):
    UID = models.UUIDField  # Computer fields

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)

    # Database fields
    created_by = models.CharField(max_length=30, default='Auto')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=30, default='Auto')
    void = models.CharField(max_length=1,
                            choices=VOID_CHOICES,
                            default="0")

    def __str__(self):
        return self.username