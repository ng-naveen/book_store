from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    isbn_no = models.PositiveIntegerField()
    published_date = models.DateField()
    price = models.CharField(max_length=250)
    cover_pic = models.ImageField(upload_to='cover_pics', null=True)

    def __str__(self):
        return self.name
    