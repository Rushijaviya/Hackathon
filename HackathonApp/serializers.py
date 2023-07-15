from rest_framework import serializers
from .models import HackathonTable, SubmissionTable

class HackathonTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackathonTable
        fields = '__all__'


class SubmissionTableSerializer(serializers.ModelSerializer):
    hackathon_title = serializers.SerializerMethodField()
    submission = serializers.SerializerMethodField()

    class Meta:
        model = SubmissionTable
        fields = ('name','Summary','hackathon_title','submission','submission_date')

    def get_hackathon_title(self,obj):
        return obj.hackathon.title
    
    def get_submission(self,obj):
        if obj.hackathon.submission_type=='image':
            return obj.submission_image
        elif obj.hackathon.submission_type=='file':
            return obj.submission_file
        else:
            return obj.submission_link