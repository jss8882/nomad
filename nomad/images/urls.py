from django.urls import path
from . import views

app_name = "images"

urlpatterns = [
    path(
        #all로 이동
        "feed/",
        view = views.Feed.as_view(),
        name = 'most recent five image'
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
        "<int:image_id>/comments/<int:comment_id>",
        view = views.MorderateComments.as_view(),
        name = "morderate_comment"
    ),
    path(
        "<int:comment_id>/comments/",
        view = views.Comment.as_view(),
        name = "comment"
    ),
    path(
        "<int:image_id>/",
        view = views.ImageDetail.as_view(),
        name = "photo_detail"
    ),
    path(
        "comments/<int:image_id>/",
        view = views.CommentOnImage.as_view(),
        name = "comment_image"
    ),
    path(
        "search/",
        view = views.Search.as_view(),
        name = "search"
    ),
    path(
        "",
        view = views.AllImages.as_view(),
        name = "all images"
    ),
]
