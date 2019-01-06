from django.urls import path
from . import views

# from nomad.users.views import (
#     user_list_view,
#     user_redirect_view,
#     user_update_view,
#     user_detail_view,
# )

app_name = "users"
urlpatterns = [
    path("explore", view=views.ExplorerUsers.as_view(), name="explore_users"),
    path("<int:user_id>/follow/",view=views.FollowUser.as_view(), name="follow_user"),
    path("<int:user_id>/unfollow/",view=views.UnFollowUser.as_view(), name="unfollow_user"),

    #순서가 바뀌면 User_Profile로 들어감
    path("search/",view=views.Search.as_view(), name="user_serach"),
    path("<str:username>/",view=views.UserProfile.as_view(), name="user_profile"),

    path("<str:username>/followers",view=views.UserFollowers.as_view(), name="user_followers"),
    path("<str:username>/following",view=views.UserFollowing.as_view(), name="user_following"),
    
    #function based view로 동작하는 followings 
    # path("<str:username>/followingFBV",view=views.UserFollowingFBV(), name="user_following"),
    
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]