from .models import FAQ, Category, Program, Teacher, Events, News, Description, AboutBIU, Manager, OurPartner, EnrollmentOrder
from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from .forms import ImgModelForm
from ckeditor.widgets import CKEditorWidget
from django.db import models
from .translation import CategoryTranslationOptions, ProgramTranslationOptions, TeacherTranslationOptions, FAQTranslationOptions, EventsTranslationOptions, NewsTranslationOptions

class ImageMixin(TranslationAdmin):
    list_display = ('title', 'image_tag')
    search_fields = ('title', 'description')
    exclude = ('img',)
    save_on_bottom = True
    form = ImgModelForm



    def image_tag(self, obj):
        if obj.img:
            return mark_safe('<img src="data:image/jpeg;base64,{}" width="50" height="50" />'.format(obj.img))
        return None

    image_tag.short_description = 'Изображение'

    class Media:
        js = ('aftotranslte.js',)

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

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
    list_display = ('full_name', 'image_tag')


@admin.register(Events)
class EventsAdmin(ImageMixin):
    list_display = ('title', 'image_tag', 'date')
    list_filter = ('date',)

@admin.register(News)
class NewsAdmin(ImageMixin):
    pass


@admin.register(Description)
class DescriptionAdmin(TranslationAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

    class Media:
        js = ('aftotranslte.js',)

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

@admin.register(AboutBIU)
class AboutBIUAdmin(ImageMixin):
    pass

@admin.register(Manager)
class ManagerAdmin(ImageMixin):
    list_display = ('full_name', 'post')

@admin.register(OurPartner)
class OurPartnerAdmin(ImageMixin):
    pass

@admin.register(EnrollmentOrder)
class EnrollmentOrderAdmin(ImageMixin):
    pass


admin.site.site_title = "Билимкана"


