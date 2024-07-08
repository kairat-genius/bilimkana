from .models import FAQ, Category, Program, Teacher, Events, News

from django.contrib import admin
from django.utils.safestring import mark_safe

from modeltranslation.admin import TranslationAdmin

from modeltranslation.translator import register, TranslationOptions
from .forms import ImgModelForm



@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Program)
class ProgramTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('name', 'speciality', 'education')


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')

@register(Events)
class EventsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')





class ImageMixin(TranslationAdmin):
    list_display = ('title', 'image_tag')
    exclude = ('img',)

    form = ImgModelForm

    def image_tag(self, obj):
        if obj.img:
            return mark_safe('<img src="data:image/jpeg;base64,{}" width="50" height="50" />'.format(obj.img))
        return None

    image_tag.short_description = 'Image'

    class Media:
        js = ('aftotranslte.js',)


@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ('question', 'answer')

    class Media:
        js = ('aftotranslte.js',)

@admin.register(Category)
class CategoryAdmin(ImageMixin):
    pass


@admin.register(Program)
class ProgramAdmin(ImageMixin):
    pass


@admin.register(Teacher)
class TeacherAdmin(ImageMixin):
    list_display = ('name', 'image_tag')

    prepopulated_fields = {"phone_number": ("whatsapp",)}


@admin.register(Events)
class EventsAdmin(ImageMixin):
    pass

@admin.register(News)
class NewsAdmin(ImageMixin):
    pass







