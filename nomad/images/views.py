#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
from nomad.notifications import views as notifications_view
from nomad.users import models as users_models
from nomad.users import serializers as users_serializers


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
        
        my_images = user.images.all()[:2]

        for image in my_images:
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
    def get(self, request, image_id, format=None):
        try:
            likes = models.Like.objects.filter(image__id = image_id)
            like_creators_ids = likes.values('creator_id')
            #filter(id__in)의 의미는 배열 안에 있는 유저 id를 검색하겠다는 의미
            users = users_models.User.objects.filter(id__in = like_creators_ids)
            serializer = users_serializers.ListUserSerializer(users, many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except models.LikeDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def post(self, request,image_id,format=None):
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
#            preexisting_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
        except models.Like.DoesNotExist:
            new_like = models.Like.objects.create(
                creator = user,
                image = found_image,
            )
            new_like.save()

            notifications_view.create_notification(user,found_image.creator,'like',found_image)

            return Response(status=status.HTTP_201_CREATED)

class UnLikeImage(APIView):

    def delete(self,request,image_id,format=None):
        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_like = models.Like.objects.get(
                creator = user,
                image = found_image
            )
            preexisting_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
            

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
            serializer.save(creator = user, image = found_image)

            notifications_view.create_notification(user,found_image.creator,'comment',found_image,serializer.data['message'])

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


class Search(APIView):
    def get(self,request,format=None):
        hashtags = request.query_params.get('hashtags',None)

        if hashtags is not None:
            hashtags = hashtags.split(",")

            #deep relationship를 검색하는 방법
            #in의 의미는 그 안에있는 각각을 다 검색??
            images = models.Image.objects.filter(tags__name__in=hashtags).distinct()

            serializer = serializers.CountImageSerializer(images,many=True)

            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class MorderateComments(APIView):
    def delete(self, request, image_id, comment_id ,format=None):
        user = request.user

        # try:
        #     image = models.Image.objects.get(id = image_id , creator = user )
        # except models.Image.DoesNotExis:
        #     return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            #다음과 같은 코드를 이용해서 앞에 주석 처리한 과정을 생략할수 있음
            #삭제하고자 하는 댓글의 ID가 URL의 ID와 동일하고, image id와 유저에 의해 생성된 이미지인지를 체크한다.
            comment_to_delete = models.Comment.objects.get(id = comment_id, image__id = image_id, image__creator = user)
            comment_to_delete.delete()
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class Images(APIView):
    def get(self, request, format = None):
        images = models.Image.objects.all()
        serializer = serializers.ImageSerializer(images,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format = None):

        user = request.user

        serializer = serializers.InputImageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(creator=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ImageDetail(APIView):
    def find_own_image(self, image_id , user):
        try:
            image = models.Image.objects.get(id = image_id, creator =user  )
            return image
        except models.Image.DoesNotExist:
            return None

    def get(self, request, image_id ,format = None):
        try:
            image = models.Image.objects.get(id = image_id)
            serializer = serializers.ImageSerializer(image)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except models.image.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self,request,image_id,format = None):
        user = request.user
        image = self.find_own_image(image_id, user)
        if image is not None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        #시리어 라이저는 2가지의 인자가 필요함 1) 업데이트 하려는 오브젝트 2)업데이터 하려는 데이터
        serializer = serializers.InputImageSerializer(image, data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save(creator=user)
            return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,image_id,format = None):

        user = request.user
        image = self.find_own_image(image_id , user)

        if image is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        image.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        




