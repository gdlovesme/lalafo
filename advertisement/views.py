import rest_framework
from django.shortcuts import render

# Create your views here.
#TODO: CRUD обьявления
#проверка прав: редактировать и удалять обьявления мог только автор
# категории может создавать, редактировать, удалять только админ
# фильтрация, поиск, пагинация
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Advertisement
from .permissions import IsAuthor
from .serializers import AdvertisementListSerializer, AdvertisementSerializer


#
# class CreateAdvertisementView(CreateAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = CreateAdSerializer
#     permission_classes = [IsAuthenticated]  #чтобы проверку мог делать только авторизованный польз-ль
#     def get_serializer_context(self):
#         return {'request': self.request}

#ListView означает, что нам будет возвр-ся список
# class AddPagination(rest_framework.pagination.PageNumberPagination):
#     page_size = 3
#
# class AdvertisementsListView(ListAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementListSerializer
#     # pagination_class = AddPagination
#
# class AdvertisementDetailsView(RetrieveAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementDetailsSerializer
#
#
# class UpdateAdvertisementView(UpdateAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = UpdateAdvertisementSerializer
#     permission_classes = [IsAuthor] # проверка
#
# class DeleteAdvertisementView(DestroyAPIView):
#     queryset = Advertisement.objects.all()
#     permission_classes = [IsAuthor]

class AdvertisementFilter(filters.FilterSet):
    price_from = filters.NumberFilter(field_name='price',
                                     lookup_expr='gte')   # gte- больше или равно
    price_to = filters.NumberFilter(field_name='price',
                                    lookup_expr='lte')


    class Meta:
        model = Advertisement
        fields = ['category', 'city']

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    ordering_fields = ['price', 'title']
    search_fields = ['title', 'text', 'city']
    filterset_class = AdvertisementFilter

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        if self.action == 'list':     #action описывает действие к-е происходит сейчас за счет метода в запросе
            serializer_class = AdvertisementListSerializer
        return serializer_class

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        return []

    # """
    # ads/             create ,list
    # ads/id/          details, update, destroy
    # """

    #listing derails проверок не надо
class CategoriesViewSet():
    pass
