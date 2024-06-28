from django.urls import path
from .views import FAQListAPIView, CategoryListAPIView, TeacherListAPIView, ProgramListAPIView,NewsListAPIView, EventsListAPIView, ApplicationListAPIView, ApplicationCreateAPIView


urlpatterns = [
    path('faq/', FAQListAPIView.as_view(), name='Вопросы и ответы'),
    path('category/', CategoryListAPIView.as_view(), name='Категорий программы'),
    path('program/', ProgramListAPIView.as_view(), name='Программы'),
    path('teacher/', TeacherListAPIView.as_view(), name='Преподаватели'),
    path('news/', TeacherListAPIView.as_view(), name='Новости'),
    path('events/', EventsListAPIView.as_view(), name='События'),
    path('application/', ApplicationListAPIView.as_view(), name='Заявки'),
    path('create_appication/', ApplicationCreateAPIView.as_view(), name='Создать заявку'),
]
