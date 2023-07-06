from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Paper(models.Model):
    sender = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='sender_question')
    receiver = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='receiver_question')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.pk}]From.{self.sender} -> To.{self.receiver}'

    def get_absolute_url(self):
        return f'/memo/{self.pk}'

"""

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    
    
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = MarkdownxField()#models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    categoryblog = models.ForeignKey(Categoryblog, null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)
"""