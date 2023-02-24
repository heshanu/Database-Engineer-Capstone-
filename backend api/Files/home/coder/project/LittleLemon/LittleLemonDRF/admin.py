from django.contrib import admin
from .models import Menu,MenuItem,Cart,Order,OrderItem
from django.conf import settings

# Register your models here.
#admin.site.register(User)

# Register your models her1e.
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)