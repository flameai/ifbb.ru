from django.contrib import admin

# Register your models here.



from .models import Slider

from .models import calend_type


admin.site.register(Slider)

admin.site.register(calend_type)