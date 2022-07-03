
from django.db import models
from django.db.models.functions import Lower
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True, db_index=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('blog:get_posts_by_category', kwargs={'category_slug': self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """slug generation from category name and <_number> if such slug already exists"""
        if not self.slug:
            slugs = [category.slug for category in Category.objects.all()]
            index_ = 0
            new_slug = slugify(self.name)
            if new_slug in slugs:
                while new_slug + '_' + str(index_) in slugs:
                    index_ += 1
                new_slug += '_' + str(index_)
            self.slug = new_slug
        super().save(force_insert, force_update, using, update_fields)

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
        return reverse('blog:get_one_post', kwargs={'post_slug': self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """slug generation from post title and <_number> if such slug already exists"""
        if not self.slug:
            slugs = [post.slug for post in Post.objects.all()]
            index_ = 0
            new_slug = slugify(self.title)
            if new_slug in slugs:
                while new_slug + '_' + str(index_) in slugs:
                    index_ += 1
                new_slug += '_' + str(index_)
            self.slug = new_slug
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ['-pk']
