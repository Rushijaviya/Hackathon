from django.urls import path
from .views import HackathonListDataView, UserHackathonListDataView, UserRegistrationToHackathonView, UserSubmissionDataView, CreateHackathonView, CreateUserSubmissionView

urlpatterns = [
    path('get-hackathon-list/',HackathonListDataView.as_view()),
    path('get-hackathon-list/<type>/',HackathonListDataView.as_view()),
    path('get-user-hackathon-list/',UserHackathonListDataView.as_view()),
    path('get-user-hackathon-list/<type>/',UserHackathonListDataView.as_view()),
    path('register-to-hackathon/',UserRegistrationToHackathonView.as_view()),
    path('view-user-submission/',UserSubmissionDataView.as_view()),
    path('create-hackathon/',CreateHackathonView.as_view()),
    path('create-user-submission/',CreateUserSubmissionView.as_view())
]