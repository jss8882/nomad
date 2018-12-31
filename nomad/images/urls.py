from django.urls import path
from . import views

app_name = "images"

urlpatterns = [
    path(
        #all로 이동
        "feed/",
        view = views.Feed.as_view(),
        name = 'all image'
    ),
    path(
        "<int:image_id>/like/",
        view = views.LikeImage.as_view(),
        name = "like_image"
    ),
    path(
        "<int:image_id>/unlike/",
        view = views.UnLikeImage.as_view(),
        name = "unlike_image"
    ),
    path(
        "comments/<int:image_id>/",
        view = views.CommentOnImage.as_view(),
        name = "comment_image"
    ),
    path(
        "<int:comment_id>/comments/",
        view = views.Comment.as_view(),
        name = "comment"
    ),
    
    
    # test codes
    
    # path(
    #     #all로 이동
    #     "all/",
    #     view = views.ListAllImages.as_view(),
    #     name = 'all image'
    # ),
    # path(
    #     #all로 이동
    #     "comments/",
    #     view = views.ListAllComments.as_view(),
    #     name = 'all image'
    # ),
    # path(
    #     #all로 이동
    #     "likes/",
    #     view = views.ListAllLikes.as_view(),
    #     name = 'all image'
    # ),
]
