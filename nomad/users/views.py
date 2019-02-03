from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers,models

#for facebook login
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

#for create notification
from nomad.notifications import views as notifications_view

class ExplorerUsers(APIView):

    def get(self, request,format=None):
        #최근 가입한 유저 5명을 불러오기

        #최근 순으로 정렬하기 위하여 order_by('-date_joined')를 사용 마이너스 필수!!
        last_five = models.User.objects.all().order_by('-date_joined')[:5]
        serializer = serializers.ListUserSerializer(last_five, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
class FollowUser(APIView):
    def post(self, request, user_id, format=None):
        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.following.add(user_to_follow)
        user.save()

        notifications_view.create_notification(user,user_to_follow,'follow')



        return Response(status=status.HTTP_200_OK)


class UnFollowUser(APIView):
    def post(self, request, user_id, format=None):
        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.following.remove(user_to_follow)
        user.save()
        return Response(status=status.HTTP_200_OK)

class UserProfile(APIView):
    def get_user(self, username):
        try:
            return models.User.objects.get(username = username)
        except models.User.DoseNotExist:
            return None


    def get(self, request, username, format=None):
        
        found_user = self.get_user(username)

        if found_user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserProfileSerializer(found_user)
        return Response(data = serializer.data,status=status.HTTP_200_OK)
    
    def put(self, request, username, format=None):
        user = request.user
        found_user = self.get_user(username)

        if found_user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        elif found_user.username != user.username:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            #우리가 업데이트할 유저는 found_user임
            serializer = serializers.UserProfileSerializer(found_user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        




class UserFollowers(APIView):
    def get(self, request, username, format=None):
        try:
            found_user = models.User.objects.get(username = request.user)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_followers = found_user.followers.all()
        serializer = serializers.ListUserSerializer(user_followers,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class UserFollowing(APIView):
    def get(serlf, request, username,format=None):
        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user_followings = found_user.following.all()
        serializer = serializers.ListUserSerializer(user_followings,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
        

class Search(APIView):
    def get(self, request, format=None):
        username = request.query_params.get('username',None)
        #여기서 정확한 매칭 검색을 원하지 않음 (대소문자 구분 하지 않음)
        if username is not None:        
            # users = models.User.objects.filter(username__icontains=username)
            users = models.User.objects.filter(username__istartswith=username)
            serializer = serializers.ListUserSerializer(users,many=True)
            return Response(data = serializer.data, status=status.HTTP_200_OK)

class ChangePassword(APIView):
    def put(self, request, username, format=None):
    #비밀번호를 변경하기 위해서 이전 비밀번호와 새로운 비밀번호가 필요함.
        user = request.user
        if user.username == username:
            current_password = request.data.get('current_password',None)
            #비밀번호를 확인하는 코드를 장고 패스워드 사이트에서 확인할수 있음 (check password documentation)
            if current_password is not None:
                passwords_match = user.check_password(current_password)

                #기존 비밀번호와 입력값이 같으면 
                if passwords_match:
                    new_password = request.data.get('new_password',None)

                    #새로운 비밀번호가 빈칸이 아니면
                    if new_password is not None:
                        user.set_password(new_password)
                        user.save()
                        return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
# def UserFollowingFBV(request, username):
#     if request.method == 'GET':
#         try:
#             found_user = models.User.objects.get(username=username)
#         except models.User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         user_followings = found_user.following.all()
#         serializer = serializers.ListUserSerializer(user_followings,many=True)

#         return Response(data = serializer.data, status=status.HTTP_200_OK)



