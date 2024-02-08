from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        return self.title


class Thesis(models.Model):
    class Status(models.TextChoices):
        REJECTED = "RJ", "Rejected"
        PUBLISHED = "PB", "Published"
        UNDER_REVIEW = "UR", "Under Review"

    title = models.CharField(max_length=250)
    abstract = models.TextField()
    status = models.CharField(
        max_length=3, choices=Status.choices, default=Status.UNDER_REVIEW
    )

    authors = models.ManyToManyField("Author", related_name="theses")
    panelists = models.ManyToManyField("Panelist", related_name="theses")

    defense_date = models.DateTimeField()
    published_date = models.DateTimeField()
    paper_link = models.CharField(max_length=250)
    institution = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    adviser = models.CharField(max_length=250)
    keywords = models.ManyToManyField("Keyword", related_name="theses")

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Panelist(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    word = models.CharField(max_length=40)

    def __str__(self):
        return self.name
