from django.db import models

# Create your models here.


class TimeStampeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = true
        
class Images(TimeStampeModel):
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()

#유저의 경우와 달리, 이전에 생성된 데이터가 없기떄문에 디폴트값 (null) 지정할 필요가 없음.
class Comment(TimeStampeModel):
    message = models.TextField()
    



    
    
    
