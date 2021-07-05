from statistics import mode
from django.contrib import admin
from board.models import Meeting, Reply
# Register your models here.

class MeetingAdmin(admin.ModelAdmin):
    model = Meeting
    list_display = ('visitor', 'manager', 'meetingDate')
    

admin.site.register(Meeting, MeetingAdmin)