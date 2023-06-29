from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    has_answer = models.BooleanField(default=True)  # 답변가능 여부

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('boards:index', args=[self.name])

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, null=True, blank=True, related_name='voter_question')  # 추천인 추가

    head_image = models.ImageField(upload_to='boards/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='boards/files/%Y/%m/%d/', blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_question')

    def __str__(self):
        return self.subject

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]


    def get_absolute_url(self):
        return f'/boards/{self.pk}'

#    def get_absolute_url(self):
#        return reverse('boards:question_detail', args=[self.id])

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

