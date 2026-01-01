from user.views import CreateUser, UserDetail

app_name = "user"

urlpatterns = [
    ("register/", CreateUser.as_view(), "create_user"),
    ("login/", ..., "create_user_auth_token"),
    ("me/", UserDetail.as_view(), "retrieve_user"),
]