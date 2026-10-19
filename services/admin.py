from django.contrib import admin
from .models import Service, Post

# Hacemos que los campos de auditoría sean visibles pero de solo lectura
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)
admin.site.register(Post, PostAdmin)