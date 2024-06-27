from django.db import models
from django.utils.translation import gettext_lazy as _



class FAQ(models.Model):
    """F.A.Q. — «Frequently Asked Questions», «часто задаваемые вопросы»."""

    question = models.TextField(verbose_name=_('Question'))
    answer = models.TextField(verbose_name=_('Answer'))

    def __str__(self):
        return self.question


class Category(models.Model):
    """Категория программы"""
    img = models.TextField("Изображение в base64", blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return self.title

class Program(models.Model):
    """Программы"""
    img = models.TextField("Изображение в base64", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return self.title


class Teacher(models.Model):
    """Преподаватели"""
    img = models.TextField("Изображение в base64", blank=True, null=True)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    telegram = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=30)
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    speciality = models.CharField(max_length=100, verbose_name=_('Speciality'))
    education = models.TextField(verbose_name=_('Education'))

    def __str__(self):
        return self.name




