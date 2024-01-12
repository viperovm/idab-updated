from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import truncatechars
from django.template.defaultfilters import slugify
from unidecode import unidecode
import os
from ckeditor_uploader.fields import RichTextUploadingField
from utils.image_crop import create_crop_3x1_wout_tmb, create_avatar


def rewiever_directory_path(instance, filename):
    name, extension = os.path.splitext(filename)
    folder = slugify(unidecode(instance.name))
    if len(folder) > 75:
        folder = folder[:75]
    return 'rewievers/{0}/{1}{2}'.format(folder, slugify(unidecode(name)), '.jpg')


def about_directory_path(instance, filename):
    title, extension = os.path.splitext(filename)
    folder = slugify(unidecode(instance.title))
    if len(folder) > 75:
        folder = folder[:75]
    return 'about/{0}/{1}{2}'.format(folder, slugify(unidecode(title)), extension)


def history_directory_path(instance, filename):
    title, extension = os.path.splitext(filename)
    folder = slugify(unidecode(instance.title))
    if len(folder) > 75:
        folder = folder[:75]
    return 'history/{0}/{1}{2}'.format(folder, slugify(unidecode(title)), extension)


def rating_directory_path(instance, filename):
    title, extension = os.path.splitext(filename)
    folder = slugify(unidecode(instance.title))
    if len(folder) > 75:
        folder = folder[:75]
    return 'rating/{0}/{1}{2}'.format(folder, slugify(unidecode(title)), extension)


class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    adress = models.CharField(max_length=255, verbose_name='Адрес')
    coords = models.CharField(max_length=20, verbose_name='Координаты на карте')
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
         return self.name

class AdmittanceDate(models.Model):
    name = models.CharField(max_length=150, verbose_name='Дата набора')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Дата набора'
        verbose_name_plural = 'Даты набора'

    def __str__(self):
         return self.name


class Phone(models.Model):
    phone = PhoneNumberField(null=True, blank=True, verbose_name='Телефон')
    contact = models.ForeignKey('Contact', related_name='phones', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Контакты')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class Social(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    link = models.URLField(verbose_name='Ссылка')
    contact = models.ForeignKey('Contact', related_name='links', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Контакты')

    class Meta:
        verbose_name = 'Соцсеть'
        verbose_name_plural = 'Соцсети'

    def __str__(self):
         return self.name


class Review(models.Model):
    name = models.CharField(max_length=150, verbose_name='Полное имя', blank=True, null=True)
    company = models.CharField(max_length=255, verbose_name='Компания', blank=True, null=True)
    position = models.CharField(max_length=255, verbose_name='Должность', blank=True, null=True)
    avatar = models.ImageField(upload_to=rewiever_directory_path, max_length=255, verbose_name='Аватар', blank=True, null=True)
    body =models.TextField(blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
         return self.name
    
    def save(self, *args, **kwargs):
        super(Review, self).save()
        if self.avatar:
            create_avatar(self.avatar, 75, 75)


class Faq(models.Model):
    question = models.CharField(max_length=150, verbose_name='Полное имя', blank=True, null=True)
    answer = RichTextUploadingField(verbose_name='Текст')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
         return truncatechars(self.question, 20)


class History(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок', blank=True, null=True)
    date = models.CharField(max_length=150, verbose_name='Дата', blank=True, null=True)
    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    image = models.ImageField(upload_to=history_directory_path, max_length=255, verbose_name='Изображение', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    my_order = models.PositiveIntegerField(verbose_name='Сорт.',
                                           default=0,
                                           blank=False,
                                           null=False,
                                           )

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Эл-т истории'
        verbose_name_plural = 'Эл-ты истории'

    def __str__(self):
        return truncatechars(self.title, 20)

    def save(self, *args, **kwargs):
        super(History, self).save()
        if self.image:
            create_crop_3x1_wout_tmb(self, crop_width=700, crop_heigth=394)


class Rating(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок', blank=True, null=True)
    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    url = models.TextField(verbose_name='Ссылка на статью', blank=True, null=True)
    image = models.ImageField(upload_to=rating_directory_path, max_length=255, verbose_name='Изображение', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    my_order = models.PositiveIntegerField(verbose_name='Сорт.',
                                           default=0,
                                           blank=False,
                                           null=False,
                                           )

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Эл-т рейтинга'
        verbose_name_plural = 'Эл-ты рейтинга'

    def __str__(self):
        return truncatechars(self.title, 20)

    def save(self, *args, **kwargs):
        super(Rating, self).save()
        if self.image:
            create_crop_3x1_wout_tmb(self, crop_width=700, crop_heigth=380)


class Page(models.Model):
    excerption = models.TextField(verbose_name='Цитата', blank=True, null=True)
    sub1 = models.CharField(max_length=150, verbose_name='Подпись1', blank=True, null=True)
    sub2 = models.CharField(max_length=150, verbose_name='Подпись2', blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name='Название', blank=True, null=True)
    image = models.ImageField(upload_to=about_directory_path, max_length=255, verbose_name='Титульное фото', blank=True, null=True)
    order_number = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order_number']
        abstract = True

    def __str__(self):
         return truncatechars(self.title, 20)

    def save(self, *args, **kwargs):
        super(Page, self).save()
        if self.image:
            create_crop_3x1_wout_tmb(self)


class Section(Page):
    body = RichTextUploadingField(verbose_name='Текст', blank=True, null=True)
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class SubSection(Page):
    section = models.ForeignKey('Section', related_name='subsections', on_delete=models.CASCADE, verbose_name='Раздел', blank=True, null=True)
    class Meta:
        verbose_name = 'Подраздел'
        verbose_name_plural = 'Подразделы'

