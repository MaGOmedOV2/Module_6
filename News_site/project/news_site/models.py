from django.db import models
class Post (models.Model):

    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    category = models.ForeignKey(to='Category',on_delete=models.CASCADE,related_name='news')

    def __str__(self):
        return f'{self.title.title()}: {self.time_in}({self.content})'

class Category(models.Model):

    category_name = models.CharField(max_length=50, unique = True)

    def __str__(self):
        return self.category_name.title()
