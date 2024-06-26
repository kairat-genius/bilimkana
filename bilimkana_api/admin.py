from .models import FAQ

from django.contrib import admin

from modeltranslation.translator import register, TranslationOptions

from modeltranslation.admin import TranslationAdmin

@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ('question', 'answer')


# @admin.register(Category)
# class CategoryAdmin(TranslatableAdmin):
#     pass

#
# @admin.register(Program)
# class ProgramAdmin(TranslatableAdmin):
#
#     pass
#
#
# @admin.register(Teacher)
# class TeacherAdmin(TranslatableAdmin):
#
#     pass
