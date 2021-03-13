from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ProductManager(models.Manager):
    def new_items(self):
        return self.all().order_by('-pk')[:12]
    def top_items(self):
        return self.all().order_by('-sell_count')[:12]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    mainimage = models.ImageField(upload_to='Products', blank=True, null=True)
    name = models.CharField(max_length=264)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Description')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    sell_count = models.IntegerField(default=0)

    objects = ProductManager()


    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ['-created', ]

class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='liker')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} : {}'.format(self.user, self.product)