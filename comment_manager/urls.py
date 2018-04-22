from django.conf.urls import url
from comment_manager import views

urlpatterns = [
    url(r'^comment$', views.Comment.as_view()),
    url(r'^comment/(?P<id>[0-9]+)$', views.CommentDetails.as_view())
]