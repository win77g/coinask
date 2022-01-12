from django.contrib import admin
from .models import *

class StakingCoinAdmin (admin.ModelAdmin):

   list_display = ('name','logo','dayplan','procent','mindeposit','maxdeposit','is_active','updated')
#    readonly_fields = ['image_img',]
   # verbose_name_plural = 'Main'
   search_fields = ["name",]
   list_filter = ["name",]
   list_per_page = 15


class Meta:
    model = StakingCoin
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(StakingCoin,StakingCoinAdmin)
# Register your models here.
