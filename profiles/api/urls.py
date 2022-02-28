from django.urls import path
from profiles.api.views import GroupDetailView, GroupListView, UserDetailView, UserListView
# from .views import CustomObtainAuthToken
from django.views.decorators.csrf import ensure_csrf_cookie


group_list = GroupListView.as_view({"get": "list", "post": "create"})
group_detail = GroupDetailView.as_view({"get": "retrieve", "delete": "destroy"})
user_detail = UserDetailView.as_view({"get": "retrieve", "delete": "destroy"})

urlpatterns = [
    # path("log-in/", ensure_csrf_cookie(CustomObtainAuthToken.as_view()), name="log-in"),
    path("profiles/", UserListView.as_view(), name="profiles"),
    path("<id>", user_detail, name="profile"),
    # path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("group/list", group_list, name="custom-groups"),
    path("group/group-detail/<name>", group_detail, name="custom-groups-detail"),
]
