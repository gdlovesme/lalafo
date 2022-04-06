from django.urls import path
from .views import CreateAdvertisementView, AdvertisementsListView, DeleteAdvertisementView

urlpatterns = [
    path('', AdvertisementsListView.as_view()),
    path('create/', CreateAdvertisementView.as_view()),
    path('delete/<int:pk>/', DeleteAdvertisementView.as_view()),


]
