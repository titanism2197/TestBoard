from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from board.models import Meeting, Reply
from board.serializers import MeetingSerializer
from django.http import Http404


# Create your views here.
class MeetingList(APIView):
    def get(self, request, format=None):
        meetings = Meeting.objects.all()
        serializer = MeetingSerializer(meetings, many=True)
        return Response(serializer.data)

class AddMeeting(APIView):
    def post(self, request, format=None):
        data = request.data
        serializer = MeetingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class MeetingDetail(APIView):
    def get_object(self, pk):
        try:
            return Meeting.objects.get(pk=pk)
        except Meeting.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        meeting = self.get_object(pk)
        serializer = MeetingSerializer(meeting)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        meeting = self.get_object(pk)
        serializer = MeetingSerializer(meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        meeting = self.get_object(pk)
        meeting.delete()
        return Response(status=status.HTTP_200_OK)
        