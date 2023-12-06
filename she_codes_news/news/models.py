from django.db import models
from django.contrib.auth import get_user_model



class NewsStory(models.Model):
#creating categories
    CategoryChoices = models.TextChoices(
        'blog', 'Blog','news', 'In the News',
        'wins', 'Wins Wall',
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    image_url = models.URLField(blank=True, null=True)
    content = models.TextField()

#field for category with choices and default
    category = models.CharField(
        max_length = 10,
        choices = [
        ('blog', 'Blog'),
        ('news', 'In the News'),
        ('wins', 'Wins Wall'),
        ],

        default = 'blog' #this is the default
    )

class StoryCategory (models.Model):
    class CategoryChoices(models.TextChoices):
        BLOG = "blog", ("Blog")
        NEWS = "news", ('In the News')
        WIN = "wins", ('Wins Wall')
    
    CatStory = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
        default=CategoryChoices.BLOG,
        
    )
    