from .models import FAQ, Category, Program, Teacher, Events, News, Description
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

@register(Events)
class EventsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Description)
class DescriptionOptions(TranslationOptions):
    fields = ('title', 'description')