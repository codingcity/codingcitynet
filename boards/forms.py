from django import forms
from boards.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content', 'head_image', 'file_upload']  # QuestionForm에서 사용할 Question 모델의 속성
        """
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        """
        labels = {
            'subject': '제목',
            'content': '내용',
            'head_image': '이미지',
            'file_upload': '파일',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }