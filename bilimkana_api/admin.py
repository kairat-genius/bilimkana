from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(TranslatableAdmin):
    """Административная панель для часто задаваемых вопросов (FAQ)"""

    list_display = ('get_question', 'get_answer')
    search_fields = ('translations__question', 'translations__answer')

    def get_question(self, obj):
        return obj.safe_translation_getter('question', any_language=True)
    get_question.short_description = 'Вопрос'

    def get_answer(self, obj):
        return obj.safe_translation_getter('answer', any_language=True)
    get_answer.short_description = 'Ответ'