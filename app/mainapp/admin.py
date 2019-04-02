
from django.conf import settings


from django.contrib import admin

# Register your models here.



from .models import Slider
from .models import Photo

from .models import calend_type

from .models import Page

from .models import calend_item
from .models import Template

from .models import calend_year
from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from django.forms import CharField

from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from suit_redactor.widgets import RedactorWidget

class PageForm(ModelForm):
    class Meta:
        widgets = {
            'text': RedactorWidget(editor_options={'lang': 'ru'})
        }

class PageAdmin(ModelAdmin):
    form = PageForm
    fieldsets = [
        (None, {'fields': ('title','seo_title','mainpage','slug','url','extraurl','order','image','template')
        }),

        ('Содержание', {'classes': ('full-width',), 'fields': ('text',)}),
      
        ]
    ...

admin.site.register(Page, PageAdmin)

admin.site.register(Slider)

admin.site.register(calend_type)

admin.site.register(calend_item)

admin.site.register(calend_year)

admin.site.register(Photo)

admin.site.register(Template)