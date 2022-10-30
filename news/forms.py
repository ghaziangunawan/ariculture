from django import forms
from news.models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = {
            'name',
            'review',
        }
