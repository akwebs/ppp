from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce import models as tinymce_models

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='blog_category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'blog_category'
        verbose_name_plural = 'blog_categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('web:blog_category', args=[self.slug])

# Create your models here.
class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_category', blank=True, null=True)
    title = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')
    description = tinymce_models.HTMLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)


    def __str__(self):
        return self.title

    def summary(self):
        summary = self.description.split(' ')
        return ' '.join(summary[:20])

    def imageUrl(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    def absolute_url(self):
        return "/blog/%s/" % self.slug

    def pub_day(self):
        return self.date.strftime('%d')
    
    def pub_month(self):
        return self.date.strftime('%b')

    def pub_date_pretty(self):
        return self.date.strftime('%b %e %Y')

class Projects(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')
    description = tinymce_models.HTMLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        summary = self.description.split(' ')
        return ' '.join(summary[:20])

    def imageUrl(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    def absolute_url(self):
        return "/projects/%s/" % self.slug

    def pub_day(self):
        return self.date.strftime('%d')
    
    def pub_month(self):
        return self.date.strftime('%b')

    def pub_date_pretty(self):
        return self.date.strftime('%b %e %Y')

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    # gender_choices = (
    #     ('male','Male'),
    #     ('female','Female'),
    # )
    # gender = models.CharField(max_length=200, choices=gender_choices)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    message = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def summary(self):
        return self.message[:157]