from django.contrib import admin
from .models import User

# Register your models here.

admin.site.site_header = 'Kinotic 관리자 페이지'
admin.site.site_title = 'Kinotic'
admin.site.register(User)