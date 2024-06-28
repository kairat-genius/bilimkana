from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import register, TranslationOptions

from .models import FAQ, Category, Program, Teacher, News, Events
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


@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ('answer', 'question')


class ImageMixin(TranslationAdmin):
    list_display = ('title', 'image_tag')
    exclude = ('img',)

    form = ImgModelForm

    def image_tag(self, obj):
        if obj.img:
            return mark_safe('<img src="data:image/jpeg;base64,{}" width="50" height="50" />'.format(obj.img))
        return None

    image_tag.short_description = 'Image'


@admin.register(Category)
class CategoryAdmin(ImageMixin):
    pass


@admin.register(Program)
class ProgramAdmin(ImageMixin):
    pass


@admin.register(Teacher)
class TeacherAdmin(ImageMixin):
    list_display = ('name', 'image_tag')








