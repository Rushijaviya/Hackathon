from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class HackathonTable(models.Model):
    
    submission_type_choices = (
        ('image','image'),
        ('file','file'),
        ('link','link')
    )

    title  = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    background_image = models.ImageField(upload_to='static/backgroundphotos/', null=True, blank=True)
    hackathon_image = models.ImageField(upload_to='static/hackathonphotos/', default='static/hackathonphotos/default.png')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)
    submission_type = models.CharField(max_length=15, choices=submission_type_choices, default='link')
    reward_prize  = models.CharField(max_length=128, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ownhackathons')
    registered_by = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

class SubmissionTable(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    Summary = models.TextField(blank=True, null=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(HackathonTable, on_delete=models.CASCADE)
    submission_image = models.ImageField(upload_to='static/submissionphotos/', null=True, blank=True)
    submission_file = models.FileField(upload_to='static/submissionfile/', null=True, blank=True)
    submission_link = models.URLField(max_length=128, null=True, blank=True)
    submission_date = models.DateTimeField(default=timezone.now)