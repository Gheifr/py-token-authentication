from django.urls import path

from user.views import CreateUser, UserDetail, CreateTokenView

urlpatterns = [
    path("register/", CreateUser.as_view(), name="create_user"),
    path("login/", CreateTokenView.as_view(), name="obtain_user_auth_token"),
    path("me/", UserDetail.as_view(), name="retrieve_user"),
]

app_name = "user"
