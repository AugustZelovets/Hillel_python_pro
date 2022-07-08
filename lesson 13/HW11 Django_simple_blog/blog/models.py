from django.db import models
from django.db.models.functions import Lower
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.conf import settings

from blog.utils import generate_slug

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True, db_index=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('blog:get_posts_by_category', kwargs={'category_slug': self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        if not self.slug:
            self.slug = generate_slug(self, Category, self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    class Meta:
        ordering = [Lower('name')]
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    text = models.TextField()
    category = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=20, unique=True, db_index=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:get_one_post', kwargs={'slug': self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        if not self.slug:
            self.slug = generate_slug(self, Post, self.title)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    class Meta:
        ordering = ['-pk']
