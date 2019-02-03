from rest_framework import serializers
from . import models
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from nomad.users import models as user_models


class SmallImageSerializer(serializers.ModelSerializer):
    #used for the notifications

    class Meta:
        model = models.Image
        fields = (
            'file',
        )

class CountImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'like_count',
            'comment_count',
        )


class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = (
            'username',
            'profile_image'
        )


class CommentSerializer(serializers.ModelSerializer):
#    image = ImageSerializer()
    creator = FeedUserSerializer(read_only=True)
   
    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator',
        
        )
        
class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = "__all__"



class ImageSerializer(TaggitSerializer,serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    
    #count_likes라는 property를 이미지 모델에 생성했기 때문에 시리얼라이저가 불필요
#    likes = LikeSerializer(many=True)
    
    #위에서 생성한 FeedUserSerializer를 이용하여 생성자의 이름과 프로필사지을 보여줌 
    #생성자는 한명이므로 many옵션은 필요없음.
    creator = FeedUserSerializer()

    tags = TagListSerializerField()
    

    class Meta:
        model =  models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'like_count',
            'creator',
            'created_at',
            'tags',


        )
#        fields = "__all__"

class InputImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = (
            'file',
            'location',
            'caption'
        )

