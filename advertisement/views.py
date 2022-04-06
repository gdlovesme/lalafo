from django.shortcuts import render

# Create your views here.
#TODO: CRUD обьявления
#проверка прав: редактировать и удалять обьявления мог только автор
# категории может создавать, редактировать, удалять только админ
# фильтрация, поиск, пагинация
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Advertisement
from .serializers import CreateAdSerializer, AdvertisementListSerializer


class CreateAdvertisementView(CreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = CreateAdSerializer
    permission_classes = [IsAuthenticated]  #чтобы проверку мог делать только авторизованный польз-ль

#ListView означает, что нам будет возвр-ся список

class AdvertisementsListView(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementListSerializer

class AdvertisementDetailsView(RetrieveAPIView):
    pass

class UpdateAdvertisementView(UpdateAPIView):
    pass

class DeleteAdvertisementView(DestroyAPIView):
    queryset = Advertisement.objects.all()

