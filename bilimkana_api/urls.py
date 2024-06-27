from django.urls import path
from .views import FAQListAPIView, CategoryListAPIView, TeacherListAPIView, ProgramListAPIView





urlpatterns = [
    path('faq/', FAQListAPIView.as_view(), name='Вопросы и ответы'),
    path('category/', CategoryListAPIView.as_view(), name='Категорий программы'),
    path('program/', ProgramListAPIView.as_view(), name='Программы'),
    path('teacher/', TeacherListAPIView.as_view(), name='Преподаватели'),
]
