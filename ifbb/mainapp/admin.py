from django.contrib import admin

# Register your models here.



from .models import Slider

from .models import calend_type

from .models import Page

from .models import calend_item
from .models import calend_year


admin.site.register(Slider)

admin.site.register(calend_type)

admin.site.register(Page)

admin.site.register(calend_item)

admin.site.register(calend_year)