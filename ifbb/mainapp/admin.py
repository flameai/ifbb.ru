from django.contrib import admin

# Register your models here.



from .models import Slider

from .models import calend_type

from .models import Page

from .models import calend_item
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
            'text': RedactorWidget(editor_options={'lang': 'en'})
        }

class PageAdmin(ModelAdmin):
    form = PageForm
    fieldsets = [
      ('Содержание', {'classes': ('full-width',), 'fields': ('title','text','slug','url','order')})
        ]
    ...

admin.site.register(Page, PageAdmin)

admin.site.register(Slider)

admin.site.register(calend_type)

admin.site.register(calend_item)

admin.site.register(calend_year)