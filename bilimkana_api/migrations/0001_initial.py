# Generated by Django 5.0.6 on 2024-07-20 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutBIU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField(blank=True, null=True, verbose_name='Изображение в base64')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Информация о нас в главной странице',
                'verbose_name_plural': 'Информация о нас в главной странице',
            },
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('number', models.CharField(max_length=150, verbose_name='Номер')),
                ('email', models.EmailField(max_length=100)),
                ('en_level', models.CharField(max_length=150)),
                ('date_of_birth', models.DateField(max_length=15)),
                ('program', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField(blank=True, null=True, verbose_name='Изображение в base64')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория программы',
                'verbose_name_plural': 'Категории программ',
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='EnrollmentOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField(blank=True, null=True, verbose_name='Изображение в base64')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Порядок зачисления',
                'verbose_name_plural': 'Порядок зачисления',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('question_ru', models.TextField(null=True, verbose_name='Вопрос')),
                ('question_en', models.TextField(null=True, verbose_name='Вопрос')),
                ('question_ky', models.TextField(null=True, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('answer_ru', models.TextField(null=True, verbose_name='Ответ')),
                ('answer_en', models.TextField(null=True, verbose_name='Ответ')),
                ('answer_ky', models.TextField(null=True, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'часто задаваемые вопросы',
                'verbose_name_plural': 'часто задаваемые вопросы',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField(blank=True, null=True, verbose_name='Изображение в base64')),
                ('full_name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('full_name_ru', models.CharField(max_length=50, null=True, verbose_name='ФИО')),
                ('full_name_en', models.CharField(max_length=50, null=True, verbose_name='ФИО')),
                ('full_name_ky', models.CharField(max_length=50, null=True, verbose_name='ФИО')),
                ('post', models.CharField(max_length=100, verbose_name='Должность')),
                ('post_ru', models.CharField(max_length=100, null=True, verbose_name='Должность')),
                ('post_en', models.CharField(max_length=100, null=True, verbose_name='Должность')),
                ('post_ky', models.CharField(max_length=100, null=True, verbose_name='Должность')),
                ('email', models.EmailField(max_length=100, verbose_name='Электронная почта')),
            ],
            options={
                'verbose_name': 'Руководитель',
                'verbose_name_plural': 'Руководители',
            },
        ),
        migrations.CreateModel(
            name='OurPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField(blank=True, null=True, verbose_name='Изображение в base64')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Наши партнеры',
                'verbose_name_plural': 'Наши партнеры',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField(blank=True, null=True, verbose_name='Изображение в base64')),
                ('full_name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('full_name_ru', models.CharField(max_length=50, null=True, verbose_name='ФИО')),
                ('full_name_en', models.CharField(max_length=50, null=True, verbose_name='ФИО')),
                ('full_name_ky', models.CharField(max_length=50, null=True, verbose_name='ФИО')),
                ('speciality', models.CharField(max_length=100, verbose_name='Специальность')),
                ('speciality_ru', models.CharField(max_length=100, null=True, verbose_name='Специальность')),
                ('speciality_en', models.CharField(max_length=100, null=True, verbose_name='Специальность')),
                ('speciality_ky', models.CharField(max_length=100, null=True, verbose_name='Специальность')),
                ('education', models.TextField(verbose_name='Образование')),
                ('education_ru', models.TextField(null=True, verbose_name='Образование')),
                ('education_en', models.TextField(null=True, verbose_name='Образование')),
                ('education_ky', models.TextField(null=True, verbose_name='Образование')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField(blank=True, null=True, verbose_name='Изображение в base64')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время события')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('extra', models.ManyToManyField(to='bilimkana_api.description', verbose_name='Допольнительная информация')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField(blank=True, null=True, verbose_name='Изображение в base64')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время события')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('extra', models.ManyToManyField(to='bilimkana_api.description', verbose_name='Допольнительная информация')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField(blank=True, null=True, verbose_name='Изображение в base64')),
                ('pdf', models.FileField(upload_to='pdfs/')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bilimkana_api.category')),
            ],
            options={
                'verbose_name': 'Программа',
                'verbose_name_plural': 'Программы',
            },
        ),
    ]
