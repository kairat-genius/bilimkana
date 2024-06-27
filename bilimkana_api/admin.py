from .models import FAQ, Category, Program, Teacher

from django.contrib import admin


from modeltranslation.admin import TranslationAdmin

from modeltranslation.translator import register, TranslationOptions


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


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass


@admin.register(Program)
class ProgramAdmin(TranslationAdmin):

    pass


@admin.register(Teacher)
class TeacherAdmin(TranslationAdmin):

    pass
