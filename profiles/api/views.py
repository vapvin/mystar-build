from rest_framework import viewsets, mixins

# from rest_framework import status
# from rest_framework import generics
# from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from profiles.models import CustomGroup, CustomUser
from profiles.api.serializers import (
    # ProfileStatusSerializer,
    # ChangePasswordSerializer,
    # ProfileSerialzier,
    GroupSerializer,
    UserSerializer,
)
from django.contrib.auth.models import User

# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token


# class CustomObtainAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data["token"])
#         return Response({"token": token.key, "id": token.user_id})


# class ProfileList(viewsets.ViewSet):
#     queryset = Profile.objects.order_by("-date_created")
#     serializer_class = ProfileStatusSerializer
#     permission_classes = [IsAuthenticated]


class GroupListView(viewsets.ModelViewSet):
    queryset = CustomGroup.objects.all()
    pagination_class = None
    lookup_field = "id"
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class GroupDetailView(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CustomGroup.objects.all()
    serializer_class = GroupSerializer
    lookup_field = "name"
    permission_classes = [IsAuthenticated]


class UserListView(ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


class UserDetailView(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


# class ChangePasswordView(generics.UpdateAPIView):
#     """
#     An endpoint for changing password.
#     """

#     serializer_class = ChangePasswordSerializer
#     model = User
#     permission_classes = (IsAuthenticated,)

#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj

#     def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             # Check old password
#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response(
#                     {"old_password": ["Wrong password."]},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             response = {
#                 "status": "success",
#                 "code": status.HTTP_200_OK,
#                 "message": "Password updated successfully",
#                 "data": [],
#             }

#             return Response(response)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)