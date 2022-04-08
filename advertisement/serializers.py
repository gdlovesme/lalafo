from rest_framework import serializers
from .models import Advertisement, AdvertisementGallery


class ImageSerializer(serializers.ModelSerializer):
    class Meta: #класс создается для того чтобы указать что настройки относятся ко всему классу
        model = AdvertisementGallery
        fields = ['picture']


# class CreateAdSerializer(serializers.ModelSerializer):
#     images = serializers.ListField(
#         write_only=True,
#         child=serializers.ImageField()    # указываем, что будет список из картинок
#     )
#
#     class Meta:
#         model = Advertisement
#         exclude = ['author'] #исключая автора
#
#
#     def create(self, validated_data):  #т.е image из другой модельки идет
#         validated_data['author'] = self.context['request'].user  # в моем validate автор это тот, кто делает запрос (по ключу request получаем юзера)
#
#         images = validated_data.pop('images', [])
#         ad = super().create(validated_data)          #создаем само объявление
#         for picture in images:
#             AdvertisementGallery.objects.create(advertisement=ad,
#                                                 picture=picture) #создаем обьект класса ADV GALLERY
#         return ad

class AdvertisementListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField() #метод ,чтоюы достать картинку , тк она в другой модельке

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'city', 'price', 'image']

    def get_image(self, advertisement):
        first_image_obj = advertisement.images.first()
        if first_image_obj is not None:
            return first_image_obj.picture.url
        return ''
#
# class AdvertisementDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Advertisement
#         fields = '__all__'
#         # репр отдамт все поля к-е есть в обьявлении
#     def to_representation(self, instance):   #instance - обьявление. черезе него ополучим все его изображения
#         representation = super().to_representation(instance) #то.что будет на выходе в виде словаря
#         representation['images'] = ImageSerializer(instance.images.all(),
#                                                    many=True).data
#         return representation

# class UpdateAdvertisementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Advertisement
#         fields = ['title', 'text', 'city', 'price']

class AdvertisementSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        write_only=True,
        child=serializers.ImageField()  # указываем, что будет список из картинок
    )
    class Meta:
        model = Advertisement
        # fields = '__all__'
        exclude = ['user']

    def create(self, validated_data):  #т.е image из другой модельки идет
        validated_data['author'] = self.context['request'].user  # в моем validate автор это тот, кто делает запрос (по ключу request получаем юзера)

        images = validated_data.pop('images', [])
        ad = super().create(validated_data)          #создаем само объявление
        for picture in images:
            AdvertisementGallery.objects.create(advertisement=ad,
                                                picture=picture) #создаем обьект класса ADV GALLERY
        return ad

    def to_representation(self, instance):  # instance - обьявление. черезе него ополучим все его изображения
        representation = super().to_representation(instance)  # то.что будет на выходе в виде словаря
        representation['images'] = ImageSerializer(instance.images.all(),
                                                   many=True).data
        return representation








#1. чтобы принимать д-е и создавать обьекты  Createserializer
#2. чтобы отобразить обьявления которые у нас есть. сериал-р отвечает за то,  какие поля и в каком типе будут получены
#ModelSerializer -