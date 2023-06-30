from django.db import models

# Create your models here.

#for profile
from django.contrib.auth.models import User



class Profile(models.Model):
    thisuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    user_image = models.ImageField(upload_to='profile/images/%Y/%m/%d/', blank=True)
    intro = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    public_approved = models.BooleanField(default=False)
    birthdate = models.DateField(null=True)

    def __str__(self):
        return f'[{self.pk}] {self.thisuser} : {self.intro}'

    def get_absolute_url(self):
        return f'/profilehistory/{self.pk}'

    #birthday = models.DateField(auto_now=False)

    #modify_date = models.DateTimeField(null=True, blank=True) #no #그냥 매번 프로필 만들고, 수정없슴 걍 최근꺼 보여주기, 기록남겨서 개인히스토리
    #nickname = models.CharField(max_length=10)

    #def __str__(self):
    #    return self.nickname


