from django.urls import path

from user.views import CreateUserView, UserDetailView, CreateTokenView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create_user"),
    path("login/", CreateTokenView.as_view(), name="obtain_user_auth_token"),
    path("me/", UserDetailView.as_view(), name="retrieve_user"),
]

app_name = "user"
