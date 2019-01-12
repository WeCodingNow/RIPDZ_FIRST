from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(AbstractUser):
    objects = UserManager()

    avatar = models.ImageField(upload_to='avatars', blank=True, null=True, default=None, verbose_name='Аватар')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')

    class Meta:
        db_table = 'Профиль'
        verbose_name = _('Профиль программиста')
        verbose_name = _('Профили программистов')


class Program(models.Model):
    programName = models.CharField(max_length=255, unique=True, verbose_name='Программа')
    description = models.CharField(max_length=255, verbose_name='Описание')
    programmers = models.ManyToManyField(Profile, verbose_name='Создатель')


class Site(models.Model):
    url = models.CharField(max_length=255, unique=True)
    siteName = models.CharField(max_length=255, blank=True, verbose_name='Название сайта')


class Screenshot(models.Model):
    filename = models.ImageField(upload_to='screenshots')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)


class Techfield(models.Model):
    naming = models.CharField(max_length=255, unique=True, verbose_name='Название сферы')


class Project(models.Model):
    projectName = models.CharField(max_length=255, unique=True, verbose_name='Название проекта')
    description = models.CharField(max_length=255, verbose_name='Описание проекта')
    techfield = models.ForeignKey(Techfield, on_delete=models.CASCADE, verbose_name='Сфера действий')
    site = models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name='Сайт проекта')
    programs = models.ManyToManyField(Program, verbose_name='ПО')
    projectManage = models.ForeignKey(Profile, verbose_name='Ведущий проекта', on_delete=models.CASCADE)


class Milestone(models.Model):
    date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
