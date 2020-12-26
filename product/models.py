from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length=222,unique=True)
    keywords = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=False, unique=True)
    description = models.CharField(max_length=255,blank=True)
    image = models.ImageField(upload_to='images/',blank=True)
    status = models.CharField(max_length=10, choices=STATUS)

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    # def get_absolute_url(self):
    #     return reverse('category_detail', kwargs={'slug':self.slug})

    # def __str__(self):
    #     full_path = [self.title]
    #     k = self.parent
    #     while k is not None:
    #         full_path.append(k.title)
    #         k=k.parent
    #     return '/'.join(full_path[::-1])


class Product(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=222,unique=True)
    keywords = models.CharField(max_length=222, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    size = models.CharField(max_length=100)
    price = models.FloatField()
    amount = models.IntegerField()
    minamount = models.IntegerField()
    slug = models.SlugField(null=False, unique=True)
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
       # ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('category_detail', kwargs={'slug': self.slug})

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description='Image'


    # def avaregereview(self):
    #     reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
    #     avg=0
    #     if reviews["avarage"] is not None:
    #         avg=float(reviews["avarage"])
    #     return avg
    #
    # def countreview(self):
    #     reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
    #     cnt=0
    #     if reviews["count"] is not None:
    #         cnt = int(reviews["count"])
    #     return cnt
#
# class ProductSlider(models.Model):
#     STATUS = (
#         ('True', 'Mavjud'),
#         ('False', 'Mavjud emas'),
#     )
#     # category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     title = models.CharField(max_length=222, unique=True)
#     # keywords = models.CharField(max_length=222, unique=True)
#     description = models.TextField(blank=True)
#     image = models.ImageField(upload_to='images/', blank=True)
#     # size = models.CharField(max_length=100)
#     # price = models.FloatField()
#     # amount = models.IntegerField()
#     # minamount = models.IntegerField()
#     slug = models.SlugField(null=False, unique=True)
#     status = models.CharField(max_length=10, choices=STATUS)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#        # ordering = ('name',)
#         verbose_name = 'productslider'
#         verbose_name_plural = 'productsslider'

    # def __str__(self):
    #     return self.title

    #
    # def image_tag(self):
    #     return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    # image_tag.short_description='Image'


class Images(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    title=models.CharField(max_length=50, blank=True)
    image=models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title