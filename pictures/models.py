from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from djmoney.models.fields import MoneyField

# from django.contrib.auth.models import User
from profiles.models import CustomUser
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from .validators import validate_file_size


class PictureModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="", unique=True)
    slug = models.SlugField()
    tag = models.CharField(max_length=50, default="")
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(
        upload_to="photos/%y/%m/%d",
        height_field="height",
        width_field="width",
        validators=[validate_file_size],
    )
    thumb = ImageSpecField(
        source="image",
        processors=[Thumbnail(100, 100)],
        format="PNG",
        options={"quality": 60},
    )
    owner = models.CharField(max_length=50, default="", null=True, blank=True)
    group = models.CharField(max_length=50, default="", null=True, blank=True)
    description = models.TextField()
    price = MoneyField(max_digits=19, decimal_places=4, default_currency="KRW")
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = PictureModel.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while queryset:
            slug = original_slug + "-" + str(count)
            count += 1
            queryset = PictureModel.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = PictureModel.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except PictureModel.DoesNotExist:
                pass
        super(PictureModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
