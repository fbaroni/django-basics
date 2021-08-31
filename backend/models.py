from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, null=False, unique=False)
    content = models.CharField(max_length=20000, null=True, unique=False)

    def to_string(self):
        return self.title