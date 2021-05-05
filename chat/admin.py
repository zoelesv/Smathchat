from django.contrib import admin
from chat.models import Record, User

# Register your models here.
admin.site.register(User)
admin.site.register(Record)