from django.contrib import admin
from home.models import Setting


# , ContactMessage, Blog


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','company','update_at', 'status', 'icon']

# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ['name','subject','update_at', 'status']
#     readonly_fields = ('name','subject', 'email', 'message','ip')
#     list_filter = ['status']
#
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ['title', 'image_tag']

# admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Setting, SettingAdmin)