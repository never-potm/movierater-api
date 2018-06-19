from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    
    def avg_rating(self):
        sum = 0
        all_ratings = Rating.objects.filter(movie=self)
        for rating in all_ratings:
            sum += rating.stars
            
        if len(all_ratings) > 0:
            return sum/len(all_ratings)
        else:
            return 0
        
    def number_of_ratings(self):
        all_ratings = Rating.objects.filter(movie=self)
        return len(all_ratings)


class Rating(models.Model):
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Providing meta-data to restrict user to add adding only once
    class Meta:
        unique_together = (('user', 'movie'),) 
        index_together = (('user', 'movie'),) 