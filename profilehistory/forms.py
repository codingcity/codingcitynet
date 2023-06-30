from django import forms
from profilehistory.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  # 사용할 모델
        fields = ['user_image', 'intro', 'public_approved', 'birthdate']

        labels = {
            'user_image': '대표 이미지',
            'intro': '자기소개',
            'public_approved': '프로필 공개여부',
            'birthdate': '생년월일',
        }
