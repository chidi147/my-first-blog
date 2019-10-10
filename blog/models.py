from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# changes gotten from:https://www.valentinog.com/blog/django-missing-argument-on-delete/
    #Since Django 2.0 the ForeignKey field requires two positional arguments:

    #the model to map to
    #the on_delete argument

#You can find more about on_delete by reading the documentation.
#https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey.on_delete
#For a quick fix of “missing 1 required positional argument: on_delete” update the model:
#    from django.db import models
    #class Article(models.Model):
        #category = models.ForeignKey('Category', on_delete=models.PROTECT)
        #title =  models.CharField(max_length=55)
        # ...

        #def __str__(self):
            #return self.title

#After fixing ForeignKey you’ll be able to run migrations without any trouble:

    #python manage.py migrate"""
