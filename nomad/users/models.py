from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified','Not specified')
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    profile_image = models.ImageField(null=True)
    

    name = CharField(_("Name of User"), blank=True, max_length=255)
    
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140,null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES,null=True)
    
    #follwer 와 following은 manytomany relationship임
    followers = models.ManyToManyField('self')
    following = models.ManyToManyField('self')
    
    #포스트 숫자, 팔로워 숫자등을 얻기위한 model property생성
    @property
    def post_count(self):
        #images를 사용할수 있는 이유는 image가 가지고 있는 creator에 대해 related name으로 묶여있기 때문
        #in images's models.py
        #creator = models.ForeignKey(user_models.User,on_delete=models.PROTECT,null=True,related_name='images')
        return self.images.all().count()
    
    @property
    def followers_count(self):
        return self.followers.all().count()
    
    @property
    def following_count(self):
        return self.following.all().count()
     
    # def get_absolute_url(self):
    #     return reverse("users:detail", kwargs={"username": self.username})

