from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255
    )
    slug = AutoSlugField(
        populate_from='title',
        unique=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='изображение',
        upload_to='posts',
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True
    )
    publicate_date = models.DateTimeField(
        verbose_name='дата публикации',
        default=timezone.now
    )
    show = models.BooleanField(default=True)

    @property
    def short_description(self):
        return self.description[:10] + '...' if len(self.description) > 10 else self.description

    @property
    def count_comment(self):
        return self.comment_set.count()

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name='категория',
        on_delete=models.CASCADE
    )
    username = models.CharField(
        verbose_name='коментатор',
        max_length=255
    )
    text = models.TextField(
        verbose_name='комментарий',
        blank=True
    )
    publicate_date = models.DateTimeField(
        verbose_name='дата публикации',
        default=timezone.now
    )
