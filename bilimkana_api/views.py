from rest_framework import generics
from rest_framework.response import Response
from .models import FAQ, Category, Program, Teacher, News, Events
from .serializers import FAQSerializer, CategorySerializer, ProgramSerializer, TeacherSerializer, NewsSerializer, \
    EventsSerializer

from django.http import JsonResponse
from googletrans import Translator
import json
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(
    parameters=[
        OpenApiParameter(name='lang', type=str, location=OpenApiParameter.QUERY,
                         description='Language code (e.g. "ru", "en", "ky") default = ru'),
    ],
)
class LanguageContextListMixin(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'ru')
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True, context={'lang': lang})
        return Response(serializer.data)

@extend_schema(
    parameters=[
        OpenApiParameter(name='lang', type=str, location=OpenApiParameter.QUERY,
                         description='Language code (e.g. "ru", "en", "ky") default = ru'),
    ],
)
class LanguageContextDetailMixin(generics.RetrieveAPIView):
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'lang': self.request.query_params.get('lang', 'ru')
        })
        return context


"""Списки"""
@extend_schema(
    description='Часто задаваемые вопросы',
    tags=['FAQ']
)
class FAQListAPIView(LanguageContextListMixin):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


@extend_schema(
    description='Список категорий',
    tags=['Category']
)
class CategoryListAPIView(LanguageContextListMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(
    description='Список программ',
    tags=['Program']
)
class ProgramListAPIView(LanguageContextListMixin):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


@extend_schema(
    description='Список преподавателей',
    tags=['Teacher']
)
class TeacherListAPIView(LanguageContextListMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


@extend_schema(
    description='Список новостей',
    tags=['News']
)
class NewsListAPIView(LanguageContextListMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@extend_schema(
    description='Список Событий',
    tags=['Events']
)
class EventsListAPIView(LanguageContextListMixin):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


"""Детали"""


@extend_schema(
    description='Список программ связанные с категорий',
    tags=['Category']
)
class CategoryDetailAPIView(LanguageContextListMixin):
    serializer_class = ProgramSerializer
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        category_id = self.kwargs.get(self.lookup_url_kwarg)
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Program.objects.none()

        queryset = Program.objects.filter(category=category)
        return queryset


@extend_schema(
    description='Детали программы',
    tags=['Program']
)
class ProgramDetailAPIView(LanguageContextDetailMixin):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    lookup_field = 'id'


@extend_schema(
    description='Детали новостей',
    tags=['News']
)
class NewsDetailAPIView(LanguageContextDetailMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'


@extend_schema(
    description='Детали событий',
    tags=['Events']
)
class EventsDetailAPIView(LanguageContextDetailMixin):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    lookup_field = 'id'


"""Переводчик для админ панели"""
def translate_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text_to_translate = data.get('text_to_translate', '')
        target_languages = data.get('target_language', ['en'])

        if text_to_translate:
            translator = Translator()
            translated_texts = [translator.translate(text_to_translate, src='ru', dest=target_lang).text for target_lang
                                in target_languages]
            return JsonResponse({'translated_text': translated_texts})
        else:
            return JsonResponse({'error': 'No text to translate'})

    return JsonResponse({'error': 'Invalid request method'})
