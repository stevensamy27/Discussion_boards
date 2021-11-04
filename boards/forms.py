from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message  = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'placeholder':'what is in your mind ?'}), 
    help_text='Max Legnth 4000')

    class Meta:
        model = Topic
        fields =  ['subject' , 'message']