from rest_framework import serializers
from .models import FAQ, Category, Program, Teacher, News, Events

class TranslationSerializerMixin(serializers.ModelSerializer):
    """Миксин для сериализаторов, поддерживающих переводы полей."""

    def get_localized_field(self, obj, field_name, lang):
        """
        Получает локализованное поле в зависимости от языка.
        """
        default_field_name = f'{field_name}_ru'
        lang_field_name = f'{field_name}_{lang}'
        return getattr(obj, lang_field_name, getattr(obj, default_field_name))


class TitleDescriptionMixin:
    def get_title(self, obj):
        lang = self.context.get('lang', 'ru')
        return self.get_localized_field(obj, 'title', lang)

    def get_description(self, obj):
        lang = self.context.get('lang', 'ru')
        return self.get_localized_field(obj, 'description', lang)



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

class NewsSerializer(TranslationSerializerMixin, TitleDescriptionMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'img', 'title', 'description']

class EventsSerializer(TranslationSerializerMixin, TitleDescriptionMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'img', 'title', 'description']
