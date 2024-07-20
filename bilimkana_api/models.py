from django.db import models
from django.utils.translation import gettext_lazy as _



class FAQ(models.Model):
    """F.A.Q. — «Frequently Asked Questions», «часто задаваемые вопросы»."""
    question = models.TextField(verbose_name=_('Вопрос'))
    answer = models.TextField(verbose_name=_('Ответ'))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "часто задаваемые вопросы"
        verbose_name_plural = "часто задаваемые вопросы"

class Description(models.Model):
    """Дополнительное информация"""
    title = models.CharField(max_length=150, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    """Категория программы"""
    img = models.TextField("Изображение в base64", blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория программы"
        verbose_name_plural = "Категории программ"


class Program(models.Model):
    """Программы"""
    img = models.TextField("Изображение в base64", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    pdf = models.FileField(upload_to='pdfs/')
    title = models.CharField(max_length=150, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"



class Teacher(models.Model):
    """Преподаватели"""
    img = models.TextField("Изображение в base64", blank=True, null=True)
    full_name = models.CharField(max_length=50, verbose_name=_('ФИО'))
    speciality = models.CharField(max_length=100, verbose_name=_('Специальность'))
    education = models.TextField(verbose_name=_('Образование'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

class Manager(models.Model):
    """Руководители"""
    img = models.TextField("Изображение в base64", blank=True, null=True)
    full_name = models.CharField(max_length=50, verbose_name=_('ФИО'))
    post = models.CharField(max_length=100, verbose_name=_('Должность'))
    email = models.EmailField(max_length=100, verbose_name="Электронная почта")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководители"


class News(models.Model):
    """Новости"""
    img = models.TextField("Изображение в base64", blank=True, null=True)
    extra = models.ManyToManyField(Description, verbose_name=("Допольнительная информация"))
    date = models.DateTimeField(verbose_name="Дата и время события", blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "Новости"



class Events(models.Model):
    """Событие"""
    img = models.TextField("Изображение в base64", blank=True, null=True)
    extra = models.ManyToManyField(Description, verbose_name=("Допольнительная информация"))
    date = models.DateTimeField(verbose_name="Дата и время события", blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


class AboutBIU(models.Model):
    """Информация в главной странице"""
    img = models.TextField("Изображение в base64", blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Информация о нас в главной странице"
        verbose_name_plural = "Информация о нас в главной странице"


# class ProgramHome(Program):
#     """Программы"""
#
#     class Meta:
#         verbose_name = "Программа в главной странице"
#         verbose_name_plural = "Программы в главной странице"


class OurPartner(models.Model):
    """Наши партнеры"""
    img = models.TextField("Изображение в base64", blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Наши партнеры"
        verbose_name_plural = "Наши партнеры"


class EnrollmentOrder(models.Model):
    """Порядок зачисления"""
    img = models.TextField("Изображение в base64", blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Порядок зачисления'
        verbose_name_plural = "Порядок зачисления"


class Applications(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="ФИО")
    number = models.CharField(max_length=150, verbose_name="Номер")
    email = models.EmailField(max_length=100)
    en_level = models.CharField(max_length=150)
    date_of_birth = models.DateField(max_length=15)
    program = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


# class AdditionalInfo(models.Model):
#