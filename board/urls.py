from django.urls import path
from board.views import MeetingList, MeetingDetail, AddMeeting

urlpatterns = [
    path('', MeetingList.as_view()),
    path('add/', AddMeeting.as_view()),
    path('<int:pk>/', MeetingDetail.as_view()),
]