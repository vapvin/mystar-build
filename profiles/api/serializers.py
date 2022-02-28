# from rest_framework import serializers
# from profiles.models import Profile, ProfileStatus
# from rest_framework import serializers
# from django.contrib.auth.models import User

# class ChangePasswordSerializer(serializers.Serializer):
#     model = User

#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)

# class ProfileSerialzier(serializers.ModelSerializer):
#     user = serializers.StringRelatedField(read_only=True)
#     avatar = serializers.ImageField(read_only=True)

#     class Meta:
#         model = Profile
#         fields = "__all__"


# class ProfileAvatarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ("avatar",)


# class ProfileStatusSerializer(serializers.ModelSerializer):
#     user_profile = serializers.StringRelatedField(read_only=True)

#     class Meta:
#         model = Profile
#         fields = "__all__"

from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from profiles.models import CustomGroup, CustomUser

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomGroup
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = CustomUser
        fields = '__all__'


class MyRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=False, write_only=True)
    last_name = serializers.CharField(required=False, write_only=True)
    company = serializers.CharField(required=False, write_only=True)
    save_pass = serializers.CharField(required=False, write_only=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['first_name'] = self.validated_data.get('first_name', '')
        data_dict['last_name'] = self.validated_data.get('last_name', '')
        data_dict['company'] = self.validated_data.get('company', '')
        data_dict['save_pass'] = self.validated_data.get('save_pass', '')
        data_dict['password1'] = self.validated_data.get('password1', '')
        data_dict['email'] = self.validated_data.get('email', '')
        return data_dict

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user