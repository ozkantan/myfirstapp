from django.contrib import admin
from .models import TodoAppTheme

# Register your models here.

# class AuctionAdmin(admin.ModelAdmin):
#      list_display = ['title','completed','email','send_date']
     


admin.site.register(TodoAppTheme)