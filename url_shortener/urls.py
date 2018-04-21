from django.conf.urls import url
from url_shortener import views

urlpatterns = [
    url(r'^url_short$', views.UrlView.as_view()),
    url(r'^url_details$', views.UrlDetails.as_view())
]
