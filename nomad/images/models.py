from django.db import models
#그냥 models로 불러올시 기존의 models과 이름이 같아서 충돌이 발생 이를 막기위해 as 를 사용하여 닉네임 지정
from nomad.users import models as user_models

# Create your models here.

#반복작업을 피하기 위한 abstract class생성
class TimeStampeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Image(TimeStampeModel):
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User,on_delete=models.PROTECT)
    
    def __str__(self):
        return '{}-{}'.format(self.location,self.caption) #어드민페널에 어떻게 보일지를 결정 이경우에는 장소-캡션  형택으로 표시

#유저의 경우와 달리, 이전에 생성된 데이터가 없기떄문에 디폴트값 (null) 지정할 필요가 없음.
class Comment(TimeStampeModel):
    message = models.TextField()
    creator = models.ForeignKey(user_models.User,on_delete=models.PROTECT)
    image = models.ForeignKey(Image,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.message
    
    
    
#유저 모델을 사용하기 위해서 User>models>class user를 불러와야 한다

class Like(TimeStampeModel):
    creator = models.ForeignKey(user_models.User,on_delete=models.PROTECT)
    image = models.ForeignKey(Image, on_delete=models.PROTECT)

    def __str__(self):
        return '{}-{}'.format(self.creator.username , self.image.caption)
    
    
    
