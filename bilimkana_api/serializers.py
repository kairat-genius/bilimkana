from rest_framework import serializers
from .models import FAQ, Category, Program, Teacher, News, Events, Description, Manager, EnrollmentOrder, OurPartner, AboutBIU
from .mixin import TranslationSerializerMixin, TitleDescriptionMixin
class FAQSerializer(TranslationSerializerMixin):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']

    def get_question(self, obj):
        lang = self.context.get('lang', 'ru')
        return self.get_localized_field(obj, 'question', lang)

    def get_answer(self, obj):
        lang = self.context.get('lang', 'ru')
        return self.get_localized_field(obj, 'answer', lang)

class CategorySerializer(TranslationSerializerMixin, TitleDescriptionMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'img', 'title', 'description']

class ProgramSerializer(TranslationSerializerMixin, TitleDescriptionMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    category = CategorySerializer()

    class Meta:
        model = Program
        fields = ['id', 'img', 'category', 'title', 'description']

class TeacherSerializer(TranslationSerializerMixin):
    full_name = serializers.SerializerMethodField()
    speciality = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['id', 'img', 'full_name', 'speciality', 'education']

    def get_full_name(self, obj):
        lang = self.context.get('lang', 'ru')
        return self.get_localized_field(obj, 'full_name', lang)

    def get_speciality(self, obj):
        lang = self.context.get('lang', 'ru')
        return self.get_localized_field(obj, 'speciality', lang)

    def get_education(self, obj):
        lang = self.context.get('lang', 'ru')
        return self.get_localized_field(obj, 'education', lang)


class DescriptionSerializer(TranslationSerializerMixin, TitleDescriptionMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Description
        fields = ['id', 'title', 'description']


class EventsSerializer(TranslationSerializerMixin, TitleDescriptionMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    extra = DescriptionSerializer(many=True)

    class Meta:
        model = Events
        fields = ['id', 'img', 'title', 'description', 'date', 'extra']


class NewsSerializer(TranslationSerializerMixin, TitleDescriptionMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    extra = DescriptionSerializer(many=True)

    class Meta:
        model = News
        fields = ['id', 'img', 'title', 'description', 'date', 'extra']


class ManagerSerializer(TranslationSerializerMixin):
    full_name = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()

    class Meta:
        model = Manager
        fields = ['id', 'img', 'full_name', 'post', 'email']

    def get_full_name(self, obj):
        lang = self.context.get('lang', 'ru')
        return self.get_localized_field(obj, 'full_name', lang)

    def get_post(self, obj):
        lang = self.context.get('lang', 'ru')
        return self.get_localized_field(obj, 'post', lang)


class EnrollmentOrderSerializer(TranslationSerializerMixin, TitleDescriptionMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = EnrollmentOrder
        fields = ['id', 'img', 'title', 'description']

class OurPartnerSerializer(TranslationSerializerMixin, TitleDescriptionMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = OurPartner
        fields = ['id', 'img', 'title', 'description']

class AboutBIUSerializer(TranslationSerializerMixin, TitleDescriptionMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = AboutBIU
        fields = ['id', 'img', 'title', 'description']