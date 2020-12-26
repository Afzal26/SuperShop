from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.utils.safestring import mark_safe

class Setting(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length=222)
    keywords = models.CharField(max_length=222)
    description = models.TextField(max_length=255)
    company = models.CharField(max_length=150)
    address=models.CharField(max_length=155, blank=True)
    phone = models.CharField(max_length=155, blank=True)
    fax = models.CharField(max_length=155, blank=True)
    email = models.CharField(max_length=155, blank=True)
    smtserver = models.CharField(max_length=155, blank=True)
    smtemail = models.CharField(max_length=155, blank=True)
    smtpassword=models.CharField(max_length=155, blank=True)
    smtport = models.CharField(max_length=155, blank=True)
    icon = models.ImageField(upload_to='media/images/', blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    twitter = models.CharField(max_length=155, blank=True)
    youtube = models.CharField(max_length=155, blank=True)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
       # ordering = ('name',)
        verbose_name = 'setting'
        verbose_name_plural = 'settings'

    def __str__(self):
        return self.title

    # class Blog(models.Model):
    #     title = models.CharField(max_length=255)
    #     description = models.TextField()
    #     detail = models.TextField()
    #     image = models.ImageField(upload_to='images/')
    #     create_at = models.DateTimeField(auto_now_add=True)
    #     update_at = models.DateTimeField(auto_now=True)
    #
    #     def __str__(self):
    #         return self.title
    #
    #     def image_tag(self):
    #         return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    #
    #     image_tag.short_description = 'Image'