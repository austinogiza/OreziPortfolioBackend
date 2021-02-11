from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings

# Create your models here.

CATEGORY = (
    ("All", "All"),
    ("Branding Identity", "Branding Identity"),
    ("Product Design", "Product Design"),
    ("Package", "Package"),
    ("Communication", "Communication"),
    ("Campaign", "Campaign"),
    ("Flyers", "Flyers"),
)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Work(models.Model):
    title = models.CharField(max_length=200)
    brief = models.CharField(max_length=30)
    challenges = models.TextField()
    category = models.CharField(
        choices=CATEGORY, max_length=200, blank=False, null=True)
    approach = models.TextField()
    image = models.ImageField()
    image1 = models.URLField(blank=True, null=True)
    image2 = models.URLField(blank=True, null=True)
    image3 = models.URLField(blank=True, null=True)
    image4 = models.URLField(blank=True, null=True)
    image5 = models.URLField(blank=True, null=True)
    image6 = models.URLField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    post = models.TextField()
    image = models.ImageField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    tags = TaggableManager()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=False, null=True)

    def __str__(self):
        return self.title

    def get_image_url(self):
        return self.image.url
