from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from django.contrib.auth.models import User
from .models import HackathonTable, SubmissionTable
from django.utils import timezone
from .serializers import HackathonTableSerializer, SubmissionTableSerializer
import datetime
# Create your views here.

class HackathonListDataView(APIView):
    ''' Get list of Hackathon based on type(live/past/future). All Hackathon is retured if no type is given '''

    def get(self,request,type=None):
        if type=='live':
            hackathon_query = HackathonTable.objects.filter(end_date__gte=timezone.now(),start_date__lte=timezone.now())
        elif type=='past':
            hackathon_query = HackathonTable.objects.filter(end_date__lt=timezone.now())
        elif type=='future':
            hackathon_query = HackathonTable.objects.filter(start_date__gt=timezone.now())
        else:
            hackathon_query = HackathonTable.objects.all()
        data = HackathonTableSerializer(hackathon_query,many=True).data
        return Response(data,status=HTTP_200_OK)
    
class UserHackathonListDataView(APIView):
    ''' Get list of user registered Hackathon based on type(live/past/future). All user registered Hackathon is retured if no type is given '''

    def get(self,request,type=None):
        username = self.request.GET.get('username')
        user_query = User.objects.filter(username=username)
        if not user_query:
            return Response({'message':'user not found!'},status=HTTP_404_NOT_FOUND)
        user_query = user_query[0]

        if type=='live':
            hackathon_query = user_query.hackathontable_set.filter(end_date__gte=timezone.now(),start_date__lte=timezone.now())
        elif type=='past':
            hackathon_query = user_query.hackathontable_set.filter(end_date__lt=timezone.now())
        elif type=='future':
            hackathon_query = user_query.hackathontable_set.filter(start_date__gt=timezone.now())
        else:
            hackathon_query = user_query.hackathontable_set.all()
        
        data = HackathonTableSerializer(hackathon_query,many=True).data
        return Response(data,status=HTTP_200_OK)
    
class UserRegistrationToHackathonView(APIView):
    ''' Register user to hackathon '''

    def patch(self,request):
        try:
            hackathon_id = self.request.GET.get('hackathon_id')
            user_id = self.request.GET.get('user_id')
            hackathon_query=HackathonTable.objects.get(id=hackathon_id)
            hackathon_query.registered_by.add(User.objects.get(id=user_id))
            hackathon_query.save()
            return Response({'message':'user registered successfully!'},status=HTTP_200_OK)
        except:
            return Response({'message':'something went wrong!'},status=HTTP_400_BAD_REQUEST)
        
class UserSubmissionDataView(APIView):
    ''' View user submission for particular hackathon. All hackathon submission of user is returned if no hackathon is given '''

    def get(self,request):
        user_id = self.request.GET.get('user_id')
        try:
            user_query = User.objects.get(id=user_id)
        except:
            return Response({'message':'user not found!'},status=HTTP_404_NOT_FOUND)
        hackathon_id = self.request.GET.get('hackathon_id')
        user_submissions = SubmissionTable.objects.filter(submitted_by=user_query)
        if hackathon_id:
            user_submissions.filter(submitted_by=user_query,hackathon__id=hackathon_id)
            
        return Response(SubmissionTableSerializer(user_submissions,many=True).data,status=HTTP_200_OK)

class CreateHackathonView(APIView):
    ''' Create new hackathon '''

    def post(self,request):
        title = self.request.data.get('title')
        description = self.request.data.get('description')
        start_date = self.request.data.get('start_date')
        end_date = self.request.data.get('end_date')
        submission_type = self.request.data.get('submission_type')
        reward_prize = self.request.data.get('reward_prize')
        background_image = self.request.data.get('background_image')
        hackathon_image = self.request.data.get('hackathon_image')
        created_by = self.request.data.get('created_by')
        if end_date:
            end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d %H:%M:%S")

        hackathon = HackathonTable.objects.create(title=title,description=description,submission_type=submission_type,created_by_id=created_by,background_image=background_image,end_date=end_date,reward_prize=reward_prize)
        if start_date:
            start_date = datetime.datetime.strptime(start_date,"%Y-%m-%d %H:%M:%S")
            hackathon.start_date = start_date
        if hackathon_image:
            hackathon.hackathon_image = hackathon_image
        hackathon.save()

        return Response({'message':'hackathon created successfully!'},status=HTTP_200_OK)
    
class CreateUserSubmissionView(APIView):
    ''' Make user submission for hackathon '''

    def post(self,request):
        name = self.request.data.get('name')
        Summary = self.request.data.get('Summary')
        submission_image = self.request.data.get('submission_image')
        submission_file = self.request.data.get('submission_file')
        submission_link = self.request.data.get('submission_link')
        submitted_by = self.request.data.get('submitted_by')
        hackathon = self.request.data.get('hackathon')

        hackathon_query = HackathonTable.objects.get(id=hackathon)
        if hackathon_query.end_date < timezone.now():
            return Response({'message':'hackathon is expired!'},status=HTTP_400_BAD_REQUEST)
        if (hackathon_query.submission_type=='link' and (submission_image or submission_file or (not submission_link))) or (hackathon_query.submission_type=='file' and (submission_image or submission_link or (not submission_file))) or (hackathon_query.submission_type=='image' and (submission_file or submission_link or (not submission_image))):
            return Response({'message':'invalid submission!'},status=HTTP_400_BAD_REQUEST)
        SubmissionTable.objects.create(name=name,Summary=Summary,submission_file=submission_file,submission_image=submission_image,submission_link=submission_link,submission_date=timezone.now(),submitted_by_id=submitted_by,hackathon_id=hackathon)
        return Response({'message':'submission created successfully!'},status=HTTP_200_OK)