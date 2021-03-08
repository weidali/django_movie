from django.db import models


class Category(models.Model):
    """Categories"""
    name = models.CharField(max_length=150)
    description = models.TextField('Description')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Actor(models.Model):
    """Actors"""
    name = models.CharField('Name', max_length=100)
    age = models.PositiveSmallIntegerField('Age', default=0)
    description = models.TextField('Description')
    image = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('actor_detail', kwargs={'slug': self.name})


class Genre(models.Model):
    """Genres"""
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """Movies"""
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, default='')
    description = models.TextField('Description')
    country = models.CharField(max_length=30)
    directors = models.ManyToManyField(Actor, related_name='film_director')
    actors = models.ManyToManyField(Actor, related_name='film_actor')
    genres = models.ManyToManyField(Genre)
    budget = models.PositiveIntegerField(default=0, help_text='Set summ')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})

    def get_review(self):
        return self.review_set.filter(parrent_isnull=True)


class Review(models.Model):
    """Reviews"""
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'{self.name} - {self.movie}'

