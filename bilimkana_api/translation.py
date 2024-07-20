from .models import FAQ, Category, Program, Teacher, Events, News, Description, EnrollmentOrder, OurPartner, AboutBIU, Manager
from modeltranslation.translator import register, TranslationOptions


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Program)
class ProgramTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('full_name', 'speciality', 'education')


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

@register(AboutBIU)
class AboutBIUOptions(TranslationOptions):
    fields = ('title', 'description')

@register(EnrollmentOrder)
class EnrollmentOrderOptions(TranslationOptions):
    fields = ('title', 'description')

@register(OurPartner)
class OurPartnerOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Manager)
class ManagerOptions(TranslationOptions):
    fields = ('full_name', 'post')
