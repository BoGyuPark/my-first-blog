from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    
    #다른 모델에 대한 링크를 의미
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    #글자 수가 제한된 텍스트를 정의할 때 사용합니다. 글 제목같이 짧은 문자열 정보를 저장할 때 사용합니다.
    title = models.CharField(max_length=200)
    
    # 글자 수에 제한이 없는 긴 텍스트를 위한 속성입니다.
    text = models.TextField() 
    
    # 날짜와 시간을 의미
    created_date = models.DateTimeField(
            default=timezone.now)

    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title