from django.db import models
from django.contrib.auth.models import User




class Project(models.Model):

    PROGRESS_CHOICES = (
                        ("", ""),
                        ("0%", "0%"),
                        ("10%", "10%"),
                        ("20%", "20%"),
                        ("30%", "30%"),
                        ("40%", "40%"),
                        ("50%", "50%"),
                        ("60%", "60%"),
                        ("70%", "70%"),
                        ("80%", "80%"),
                        ("90%", "90%"),
                        ("COMPLETED", "COMPLETED"),
    )


    created_by = models.ForeignKey(User, default=None, blank=True, on_delete=models.CASCADE)
    progress = models.CharField(max_length=200, default="0%")
    assignedto = models.CharField(max_length=50, default="Unassigned")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)
    ongoing_notes = models.TextField(max_length=3000, blank=True)
    completed_notes = models.TextField(max_length=3000, blank=True)

    def __str__(self):
        return self.name

