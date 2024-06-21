from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Status(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Note(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', unique=True)
    text = models.TextField(verbose_name='Текст', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True)
    deadline = models.CharField(max_length=15, verbose_name='Срок выполнения задачи')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус', null=True)

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={'note_id':self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'


class Done(models.Model):
    user = models.ManyToManyField(User, related_name='done')
    note = models.OneToOneField(Note, on_delete=models.CASCADE, related_name='done', null=True, blank=True)

