from django.db import models

# Create your models here.

class BookStatus(models.TextChoices):
    COMPLETED = 'C', 'Completed'
    READING = 'R', 'Reading'
    WANT_TO_READ = 'W', 'Want to Read'

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank = False, null = False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Genre(models.Model):
    genre_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.genre_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = 'books')
    publication_year = models.IntegerField(null=True, blank = False)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    genre = models.ManyToManyField('Genre')
    status = models.CharField(max_length=1, choices=BookStatus.choices, default=BookStatus.WANT_TO_READ)
    

    def __str__(self):
        return f"{self.title} by {self.author.name}"
    
    class Meta:
        ordering=['-publication_year', 'title']

