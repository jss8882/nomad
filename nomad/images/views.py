#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers

# Create your views here.

class Feed(APIView):

    def get(self, request, format=None):
        user = request.user
        following_users = user.following.all()
        
        image_list = []
        
        for following_user in following_users:
            user_images = following_user.images.all()[:2]
            
            for image in user_images:
                image_list.append(image)
        
        print(image_list)
        
        #key함수의 return값을 기준으로 정렬함
        #key값을 lambda image : image.created_at 으로 사용해도 무관
        sorted_list = sorted(image_list,key=get_key,reverse=True)
        print(sorted_list)
        
        serializer = serializers.ImageSerializer(sorted_list,many=True)
        
        #아무것도 리스폰을 하지 않으면 에러가 뜨므로 empty respone를 넘겨줌.
        # return Response(status=200)
        
        return Response(serializer.data)
        
def get_key(image):
    return image.created_at

class LikeImage(APIView):
    def get(self, request,image_id,format=None):
        print(image_id)
        return (Response(status=200))
# class ListAllImages(APIView):

#     def get(self, request, format='None'):
#         all_images = models.Image.objects.all()
#         serializer = serializers.ImageSerializer(all_images, many=True)
#         return Response(data=serializer.data)
        
        
# class ListAllComments(APIView):
#     def get(self, request, format = 'None'):
#         all_comments = models.Comment.objects.all()
#         serializer = serializers.CommentSerializer(all_comments,many=True)
#         return Response(data=serializer.data)
        
# class ListAllLikes(APIView):
#     def get(self, request, format = 'None'):
#         all_likes = models.Like.objects.all()
#         print(request.user.website)
#         serializer = serializers.LikeSerializer(all_likes,many=True)
#         return Response(data=serializer.data)