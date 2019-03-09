from django.db import models
from django.conf import settings




#from ckeditor_uploader.fields import RichTextUploadingField
#from ckeditor.fields import RichTextField




# Create your models here.


class Slider(models.Model):
    image = models.ImageField(verbose_name=u'Изображение')
    title_internal = models.CharField(verbose_name=u'Название', max_length=200, help_text=u"Отображается только в адм.части")
    title_external = models.CharField(verbose_name=u'Оглавление на сайте', max_length=200, help_text=u"Отображается на сайте",default='')
    date_str=models.CharField(verbose_name=u'ДатаПроведения', max_length=40, help_text=u"Отображается на сайте под Оглавлением",default='')

    button_url = models.URLField(verbose_name=u'Ссылка', blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = u'слайдер'
        verbose_name_plural = u'слайдеры'

    def __str__(self):
        return "%s" % self.title_internal

    def __unicode__(self):
        return "%s" % self.title_internal



class calend_type(models.Model):
    image = models.ImageField(verbose_name=u'Изображение')
    title_internal = models.CharField(verbose_name=u'Название', max_length=200, help_text=u"Отображается только в адм.части")

    class Meta:
        verbose_name = u'Тип события в календаре'
        verbose_name_plural = u'Типы событий в календаре'
    
    def __str__(self):
        return "%s" % self.title_internal

    def __unicode__(self):
        return "%s" % self.title_internal


class calend_year(models.Model):
    title = models.CharField(verbose_name=u'Год',max_length=4,default='')
    
    class Meta:
        verbose_name = u'Год'
        verbose_name_plural = u'Годы'
    
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

    



class calend_item(models.Model):
    title = models.CharField(verbose_name=u'название',max_length=255)
    date_str = models.CharField(verbose_name=u'Дата',max_length=255)
    place_str = models.CharField(verbose_name=u'Место',max_length=255)
    calend_type = models.ForeignKey(calend_type, on_delete=models.DO_NOTHING, verbose_name=u'Тип')
    calend_year = models.ForeignKey(calend_year, on_delete=models.DO_NOTHING, verbose_name=u'Год')

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Соревнование в календаре'
        verbose_name_plural = u'Соревнования в календаре'



class Page(models.Model):
    title = models.CharField(u'заголовок', max_length=200)
    image = models.ImageField(verbose_name=u'Изображение')

    slug = models.SlugField(u'слаг', max_length=200, unique=True)
    url = models.URLField(u'URL', default='', blank=True)
    order = models.PositiveIntegerField()
    text = models.TextField(u'Текст',default='',help_text=u"Текст страницы")

    def __str__(self):
        return u"%s" % self.title

    def __unicode__(self):
        return u"%s" % self.title

    def save(self, *args, **kwargs):
        self.url = settings.PAGES_URL + self.slug + "/"
        super(Page, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u'страница'
        verbose_name_plural = u'страницы'
       