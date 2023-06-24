from django.contrib import admin

# Register your models here.
from . models import DreamProduct,ResinProduct

admin.site.register(DreamProduct)
admin.site.register(ResinProduct)

