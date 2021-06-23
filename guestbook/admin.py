from django.contrib import admin
from guestbook.models import Guestbook
# Register your models here.

class GuestbookAdmin(admin.ModelAdmin):
    list_display=('name','email','passwd','content')

admin.site.register(Guestbook, GuestbookAdmin)
