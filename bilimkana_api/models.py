from parler.models import TranslatableModel, TranslatedFields
from django.db import models
from django.utils.translation import gettext_lazy as _



class FAQ(models.Model):
    """F.A.Q. — «Frequently Asked Questions», «часто задаваемые вопросы»."""

    question = models.TextField(verbose_name=_('Question'))
    answer = models.TextField(verbose_name=_('Answer'))

    def __str__(self):
        return self.question


class Category(TranslatableModel):
    """Категория программы"""
    img = models.TextField()
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        description=models.TextField(),
    )
    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

class Program(TranslatableModel):
    img = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        description=models.TextField(),
    )
    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

class Teacher(TranslatableModel):
    img = models.TextField()
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    telegram = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=30)
    translations = TranslatedFields(
        name=models.CharField(max_length=50),
        speciality=models.CharField(max_length=100),
        education=models.TextField(),
    )

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
