from django.db import models
from django.contrib.auth import get_user_model



class NewsStory(models.Model):
#creating categories
    CategoryChoices = models.TextChoices(
        'blog', 'Blog','news', 'In the News',
        'case', 'Case Studies',
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
        ('case', 'Case Studies'),
        ],

        default = 'blog' #this is the default
    )

class StoryCategory (models.Model):
    class CategoryChoices(models.TextChoices):
        BLOG = "blog", ("Blog")
        NEWS = "news", ('In the News')
        CASE = "case", ('Case Studies')
    
    CatStory = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
        default=CategoryChoices.BLOG,
        
    )

class Comment(models.Model):
    name = models.CharField(max_length=80)
    created_on = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    story = models.ForeignKey(
        NewsStory,
        related_name= "comments",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

    

   
    
    