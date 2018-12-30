#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
    
        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=404)
        
        #이곳이 실행된다는 것은 해당 아이디를 가진 이미지가 존재한다는 뜻임
        print(image_id)
        user = request.user
        
        
        try:
            preexisting_like = models.Like.objects.get(
                creator = user,
                image =  found_image
            )
            preexisting_like.delete()
            return (Response(status=202))
            
        except models.Like.DoesNotExist:
            new_like = models.Like.objects.create(
                creator = user,
                image =  found_image
            )
            new_like.save()
            return (Response(status=200))

class CommentOnImage(APIView):
    def post(self,request,image_id,fromat=None):
    
        user = request.user
        
        print(image_id)
        
        try:
            found_image = models.Image.objects.get(id=image_id)
            print("i found image")
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(data=request.data)
        
        if serializer.is_valid():
            print("i'm valid")
            serializer.save(creator = user, image = found_image)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class Comment(APIView):
    def delete(self, request, comment_id,format=None):
        
        user = request.user
    

        try:
            comment = models.Comment.objects.get(id = comment_id,creator = user)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Comment.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)


    

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