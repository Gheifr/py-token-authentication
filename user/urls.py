from django.urls import path

from user.views import CreateUser, UserDetail
from rest_framework.authtoken import views

urlpatterns = [
    path("register/", CreateUser.as_view(), name="create_user"),
    path("login/", views.obtain_auth_token, name="create_user_auth_token"),
    path("me/", UserDetail.as_view(), name="retrieve_user"),
]

app_name = "user"
