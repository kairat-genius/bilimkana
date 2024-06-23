from django.urls import path
from .views import FAQList

urlpatterns = [
    path('faq/', FAQList.as_view(), name='Вопросы и ответы')
]
