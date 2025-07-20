from django.urls import reverse
from django.db import models

class Genre(models.Model):
    genre_name = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.genre_name
    
    def get_absolute_url(self):
        return reverse('Genre', kwargs={"genre_id": self.pk})
    


class Seeds(models.Model):
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    s_name = models.CharField(max_length=50)
    specifications = models.CharField(max_length=5000)
    year  = models.IntegerField()
    image = models.ImageField(upload_to='seeds/')
    price = models.IntegerField()
    part_book = models.TextField(blank=True)
    

    def __str__(self):
        return f"{self.s_name}, {self.specifications},{self.year},{self.image}"
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})
    


class Sendletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField( max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}, {self.email},{self.message}"


class Post(models.Model):
    p_name = models.CharField(max_length=200)
    p_image = models.ImageField(upload_to='posts/')
    p_post = models.TextField(blank=True)
    p_url = models.URLField(max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.p_name}, {self.p_url}"