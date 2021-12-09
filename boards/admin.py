from django.contrib import admin
from django.contrib.auth.models import Group
from boards.models import Board
from .models import Board, Topic
from django.contrib.auth.models import Group
# Register your models here.
admin.site.site_header = "Boards Admin Pannel"
admin.site.site_title = "Boards Admin Pannel"

class inlineTopic(admin.StackedInline ):
    model = Topic
    extra =1 

class BoardAdmin(admin.ModelAdmin):
    inlines = [inlineTopic]
    

class TopicAdmin(admin.ModelAdmin):
    feilds = ('subject', 'board','created_by' )
    list_display = ('subject', 'board','created_by','combine_subject_and_board' )
    list_display_links = ('board', 'created_by')
    # list_editable = ('subuject')
    # list_filter = ('created_by')
    search_fields = ('boards','created_by')

    def combine_subject_and_board(self, obj):
        return "{} - {}".format(obj.subject,obj.board)



admin.site.register(Board,BoardAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.unregister(Group)

