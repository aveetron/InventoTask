from django.db import models



# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title



class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='BlogImage/')

    def __str__(self):
        return self.image