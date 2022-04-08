from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    ('open', 'Открытое'),
    ('closed', 'Закрытое')
)


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='ads')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    city = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads') #юзер мо ключу ads может достать все объявления

    def __str__(self):
        return self.title

class AdvertisementGallery(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE,
                                      related_name='images')
    picture = models.ImageField(upload_to='ads')


