from django.db import models

# Create your models here.


class Blog(models.Model):
    img = models.ImageField(upload_to = 'templates/images/')
    content = models.TextField()
    title = models.TextField()

    def __unicode__(self):
        return self.title
