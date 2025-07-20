from django.contrib import admin
from .models import Seeds,Sendletter,Post
from .models import * 


class SeedAdmin(admin.ModelAdmin):
    list_display = ('s_name','year','image')
    list_display_links = ('s_name','year','image')
    search_fields = ('s_name','year','image')

admin.site.register(Seeds,SeedAdmin)


class SendletterAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
    list_display_links = ('name','email')
    search_fields = ('Username','email')

admin.site.register(Sendletter,SendletterAdmin)
admin.site.register(Genre)

class PostAdmin(admin.ModelAdmin):
    list_display = ('p_name','p_url')
    list_display_links = ('p_name','p_url')

admin.site.register(Post,PostAdmin)