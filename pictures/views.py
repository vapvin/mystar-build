from rest_framework.response import Response
from rest_framework import viewsets, permissions, mixins
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from pictures.models import PictureModel
from pictures.serializers import PictureSerializer, PictureUpdateSerializer
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication

class PictureListView(viewsets.ModelViewSet):
    search_fields = ['title', 'tag']
    filter_backends = (filters.SearchFilter,)
    queryset = PictureModel.objects.order_by("-date_created")
    serializer_class = PictureSerializer
    lookup_field = "id"
    permission_classes = [HasAPIKey | permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [HasAPIKey | permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PicureDetailView(mixins.UpdateModelMixin, 
                        mixins.ListModelMixin, 
                        mixins.DestroyModelMixin, 
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = PictureModel.objects.all()
    serializer_class = PictureSerializer
    lookup_field = "id"
    permission_classes = [HasAPIKey | permissions.IsAuthenticated]

    # def put(self, request, pk):
    #     picture = self.get_object(pk)
    #     serializer = PictureSerializer(picture, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PictureUpdateView(UpdateAPIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    queryset = PictureModel.objects.order_by("-date_created")
    serializer_class = PictureUpdateSerializer
    lookup_field = "id"
    permission_classes = [HasAPIKey | permissions.IsAuthenticated]


class PictureFeaturedView(ListAPIView):
    queryset = PictureModel.objects.all().filter(featured=True)
    serializer_class = PictureSerializer
    lookup_field = "id"
    permission_classes = [HasAPIKey | permissions.IsAuthenticated]


# class PictureSearchView(ListAPIView):
    


# class PictureCategoryView(APIView):
#     serializer_class = PictureSerializer
#     permission_classes = [HasAPIKey | permissions.IsAuthenticated]

#     def post(self, request, format=None):
#         data = self.request.data
#         category = data["category"]
#         queryset = PictureModel.objects.order_by("-date_created").filter(
#             category__iexact=category
#         )

#         serializer = PictureSerializer(queryset, many=True)
#         return Response(serializer.data)
