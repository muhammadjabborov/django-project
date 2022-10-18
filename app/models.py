from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Model, DateTimeField, ImageField, FloatField, CharField, TextChoices, ForeignKey, CASCADE, \
    TextField, DateField


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Arrival(BaseModel):
    class Rate(TextChoices):
        GOOD = 'Good'
        BAD = 'Bad'
        FIFTY_TO_FIFTY = '50/50'

    image = ImageField(upload_to='image/')
    rating = CharField(max_length=255, choices=Rate.choices, default=Rate.GOOD)
    title = CharField(max_length=255)
    description = TextField()
    price = FloatField()

    def __str__(self):
        return self.title


class Product(BaseModel):
    class Rate(TextChoices):
        GOOD = 'Good'
        BAD = 'Bad'
        FIFTY_TO_FIFTY = '50/50'

    image = ImageField(upload_to='image/')
    rating = CharField(max_length=255, choices=Rate.choices, default=Rate.GOOD)
    title = CharField(max_length=255)
    price = FloatField()

    def __str__(self):
        return self.title


class Author(BaseModel):
    full_name = CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Blog(BaseModel):
    title = CharField(max_length=255)
    image = ImageField(upload_to='image/')
    author = ForeignKey(Author, on_delete=CASCADE)
    description = TextField()

    def __str__(self):
        return self.title
