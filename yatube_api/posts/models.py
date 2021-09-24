from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
        help_text='Дайте название группе')
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальный фрагмент URL-адреса страницы группы',
        help_text=('Укажите уникальный фрагмент URL-адреса '
                   'для страницы группы. Используйте только латиницу, '
                   'цифры, дефисы и знаки подчёркивания'),
    )
    description = models.TextField(
        verbose_name='Описание', help_text='Опишите вашу группу', )

    class Meta:
        ordering = ['title']

    def __repr__(self):
        return f'{self.title} :: {self.slug} :: {self.description[:15]} ...'


class Post(models.Model):
    text = models.TextField(
        verbose_name='Введите текст', help_text='Текст вашего поста здесь', )
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True, )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts', verbose_name='Автор', )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True, )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        blank=True, null=True, related_name='posts',
        verbose_name='Выбор группы', help_text='Выбор группы по желанию', )

    class Meta:
        ordering = ['-pub_date']

    def __repr__(self):
        return (f'{self.text[:15]} ... '
                f'({self.pub_date}, {self.author}, {self.group})')


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments', )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments', )
    text = models.TextField(
        verbose_name='Введите текст',
        help_text='Текст Вашего комментария здесь', )
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created']

    def __repr__(self):
        return (f'{self.text[:15]} ... '
                f'({self.created}, {self.author}, {self.post[:15]}...)')


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='follower', blank=True, null=True, )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following', blank=True, null=True, )
    created = models.DateTimeField(
        auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created']

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name="unique_followers")
        ]

    def __repr__(self):
        return f'{self.user} follows {self.following}'
