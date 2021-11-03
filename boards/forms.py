from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message  = forms.CharField(widget=forms.Textarea )

    class Meta:
        model = Topic
        fields =  ['subject' , 'message']