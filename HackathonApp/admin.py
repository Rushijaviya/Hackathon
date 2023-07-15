from django.contrib import admin
from .models import HackathonTable, SubmissionTable

# Register your models here.
@admin.register(HackathonTable)
class HackathonTableAdmin(admin.ModelAdmin):
    list_display = ('created_by','title','start_date','end_date','submission_type','reward_prize')
    search_fields = ('created_by__username','title','start_date','submission_type')

@admin.register(SubmissionTable)
class SubmissionTableAdmin(admin.ModelAdmin):
    list_display = ('name','submitted_by','hackathon','submission_date')
    search_fields = ('submitted_by__username','submission_date','name')