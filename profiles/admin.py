from django.contrib import admin
from profiles.models import CustomGroup, CustomUser

admin.site.register(CustomUser)
admin.site.register(CustomGroup)
# admin.site.register(Profile)
# admin.site.register(ProfileStatus)