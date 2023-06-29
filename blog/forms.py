from .models import Comment, Feedback
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('content',)