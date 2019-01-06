from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from nomad.users import models as user_models
from nomad.images import models as image_models
# Create your models here.

#create at, updated_at를 사용하기 위해 image model의 TimeStampeModel를 가져옴
class Notification(image_models.TimeStampeModel):
    TYPE_CHOICES = (
        ('like','Like'),
        ('comment','Comment'),
        ('follow','Follow'),
    )
    creator= models.ForeignKey(user_models.User , on_delete=models.PROTECT, related_name='creator')
    to = models.ForeignKey(user_models.User,on_delete=models.PROTECT,related_name='to')
    notification_type = models.CharField(max_length = 20, choices = TYPE_CHOICES)
    #null = True blank = True를 설정하면 기본값으 아님.
    image = models.ForeignKey(image_models.Image, on_delete=models.PROTECT,null=True, blank = True)
    # creator = models.ForeignKey(user_models.User,on_delete=models.PROTECT,null=True,related_name='images')



# from django.db import models
# from nomadgram.users import models as user_models
# from nomadgram.images import models as image_models


# class Notification(image_models.TimeStampedModel):

#     TYPE_CHOICES = (
#         ('like', 'Like'),
#         ('comment', 'Comment'),
#         ('follow', 'Follow')
#     )

#     creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, related_name='creator')
#     to = models.ForeignKey(user_models.User, on_delete=models.PROTECT, related_name='to')
#     notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
#     image = models.ForeignKey(image_models.Image, on_delete=models.PROTECT, null=True, blank=True)