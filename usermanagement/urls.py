from django.conf.urls import url
from usermanagement import views

urlpatterns = [
    url(r'^usermanagement$', views.UserManagement.as_view())
]