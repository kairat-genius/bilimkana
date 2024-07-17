from .views import (FAQListAPIView, CategoryListAPIView, TeacherListAPIView, ProgramListAPIView, NewsListAPIView,
                    EventsListAPIView,
                    EventsDetailAPIView, ProgramDetailAPIView, NewsDetailAPIView, CategoryDetailAPIView)

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include
from bilimkana_api.views import translate_text


urlpatterns = [

    path('admin/', admin.site.urls),
    path('translate/', translate_text, name='translate'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('faq/', FAQListAPIView.as_view(), name='Вопросы и ответы'),

    # Категории
    path('category/', CategoryListAPIView.as_view(), name='Категорий программы'),
    path('category/detail/<int:id>/', CategoryDetailAPIView.as_view(), name='Все программы связанные с категорией'),

    # Программы
    path('program/', ProgramListAPIView.as_view(), name='Программы'),
    path('program/detail/<int:id>/', ProgramDetailAPIView.as_view(), name='Детали программ'),

    # Преподаватели
    path('teacher/', TeacherListAPIView.as_view(), name='Преподаватели'),

    # Новости
    path('news/', NewsListAPIView.as_view(), name='Новости'),
    path('news/detail/<int:id>/', NewsDetailAPIView.as_view(), name='Детали новостей'),

    # События
    path('events/', EventsListAPIView.as_view(), name='События'),
    path('events/detail/<int:id>/', EventsDetailAPIView.as_view(), name='Детали событий'),
]
