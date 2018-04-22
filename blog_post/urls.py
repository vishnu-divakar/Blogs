from django.conf.urls import url
from blog_post import views

urlpatterns = [
    url(r'^blog_post$', views.BlogPost.as_view()),
    url(r'^blog_post/(?P<id>[0-9]+)$', views.BlogPostDetails.as_view())
]