from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.CharField(max_length=240, blank=True)
#     city = models.CharField(max_length=30, blank=True)
#     avatar = models.ImageField(null=True, blank=True)

#     def __str__(self):
#         return self.user.username


# class ProfileStatus(models.Model):
#     user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     status_content = models.CharField(max_length=240)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name_plural = "statuses"

#     def __str__(self):
#         return str(self.user_profile)

class CustomGroup(models.Model):

    name = models.CharField(max_length=50, default="Free")
    deps = models.IntegerField(default=1)
    child = models.CharField(max_length=50, default="---")

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    company = models.CharField(max_length=50, default="Free", null=True, blank=True)
    save_pass = models.CharField(max_length=50, default="", null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.email