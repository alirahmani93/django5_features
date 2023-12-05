from django.contrib.postgres.fields import ArrayField, DateRangeField
from django.contrib.postgres.fields.array import ArrayLenTransform
from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.db import models
from django.db.models import F, Value


class Product(models.Model):
    slug = models.SlugField()
    data = models.JSONField()
    version = models.GeneratedField(
        expression=F("data__info__version"),
        output_field=models.TextField(),
        db_persist=True,
    )

    def __str__(self):
        return f"{self.slug} {self.version}"


# Search field
class Quote(models.Model):
    author = models.TextField()
    text = models.TextField()
    search = models.GeneratedField(
        db_persist=True,
        expression=SearchVector(
            "text", config="english"
        ),
        output_field=SearchVectorField(),
    )

    def __str__(self):
        return f"[{self.author}] {self.text}"


# Concat operations
class ConcatOp(models.Func):
    arg_joiner = " || "
    function = None
    output_field = models.TextField()
    template = "%(expressions)s"


class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    full_name = models.GeneratedField(
        expression=ConcatOp(
            "first_name", Value(" "), "last_name",
        ),
        output_field=models.TextField(),
        db_persist=True,
    )

    def __str__(self):
        return self.full_name


# Array
class Landmark(models.Model):
    name = models.TextField()
    reviews = ArrayField(
        models.SmallIntegerField()
    )
    count = models.GeneratedField(
        db_persist=True,
        expression=ArrayLenTransform(
            "reviews"
        ),
        output_field=models.IntegerField(),
    )

    def __str__(self):
        return (
            f"{self.name} "
            f"({self.count} reviews)"
        )


# DateRange
class DateRangeFunc(models.Func):
    function = "DATERANGE"
    output_field = DateRangeField()


class Booking(models.Model):
    start = models.DateField()
    end = models.DateField()
    span = models.GeneratedField(
        expression=DateRangeFunc(
            "start", "end"
        ),
        output_field=DateRangeField(),
        db_persist=True,
    )

    def __str__(self):
        return (
            # f"{self.span.bounds[0]}"
            f"{self.span.lower.isoformat()} -"
            f"> {self.span.upper.isoformat()}"
            # f"{self.span.bounds[1]}"
        )
