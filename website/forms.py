from django import forms

from .models import foodItemComment

class foodItemCommentForm(forms.ModelForm):
    class Meta:
        model = foodItemComment
        fields = ['comment']
