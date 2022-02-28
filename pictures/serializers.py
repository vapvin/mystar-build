from rest_framework import serializers
from .models import PictureModel


class PictureSerializer(serializers.ModelSerializer):

    thumb = serializers.ImageField(read_only=True)

    class Meta:
        model = PictureModel
        fields = "__all__"
        lookup_field = "id"

    def __init__(self, *args, **kwargs):
        kwargs["partial"] = True
        super(PictureSerializer, self).__init__(*args, **kwargs)


class PictureUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PictureModel
        fields = ["title", "price", "tag"]
        lookup_field = "id"
