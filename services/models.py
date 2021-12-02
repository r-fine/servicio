from django.urls import reverse
from django.db import models
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(
        verbose_name='Category Name',
        max_length=255,
        db_index=True,
    )
    slug = models.SlugField(max_length=255, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    description = models.TextField(
        verbose_name='Category Description',
        blank=True
    )
    image = models.ImageField(
        upload_to="images/category/",
        default="images/500_500.png"
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse(
            'services:category_detail',
            args=[self.slug]
        )

    def __str__(self):
        for i in range(3):
            if self.level == i:
                suff = '-'*i
                name = suff+self.name
        return name


class Service(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='category',
        null=True,
        on_delete=models.SET_NULL,
    )
    name = models.CharField(verbose_name='Service Name', max_length=255)
    summary = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/services/",
        default="images/500_500.png",
    )
    is_active = models.BooleanField(
        verbose_name="Service Visibility",
        default=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ReviewRating(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='review_category',
        on_delete=models.CASCADE,
        null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='review_user',
        on_delete=models.CASCADE
    )
    subject = models.CharField(
        verbose_name='Review Title',
        max_length=100,
        blank=True
    )
    review = models.TextField(
        verbose_name='Review Details',
        max_length=500,
        blank=True
    )
    rating = models.FloatField()
    status = models.BooleanField(
        verbose_name='Review Visibility',
        default=True
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
