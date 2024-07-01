from django.contrib import admin
from .models import Item, ToDoList,Booking,Profile

from image_cropping import ImageCroppingMixin

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'audit','location','image','list','is_booked','booked_by','booked_at')  # Include 'id' in list display
     
class ProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)
admin.site.register(Booking)



admin.site.register(ToDoList)
admin.site.register(Profile,ProfileAdmin)