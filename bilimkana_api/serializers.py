from rest_framework import serializers
from .models import FAQ, Category, Program, Teacher, News, Events, Description
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
    name = serializers.SerializerMethodField()
    speciality = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['id', 'img', 'phone_number', 'email', 'telegram', 'whatsapp', 'name', 'speciality', 'education']

    def get_name(self, obj):
        lang = self.context.get('lang', 'ru')
        return self.get_localized_field(obj, 'name', lang)

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

    class Meta:
        model = News
        fields = ['id', 'img', 'title', 'description']