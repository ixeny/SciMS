from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

class Category(models.Model):
 cat_name = models.CharField(max_length=128)
 def __str__(self):
  return self.cat_name

class Keyword(models.Model):
 word = models.CharField(max_length=20)
 def value(self):
  return self.word


class Article(models.Model):
 pub_date = models.DateTimeField(auto_now_add=True)
 title = models.CharField(max_length=200)
 abstract = models.TextField()
 content = models.TextField()
 category = models.ForeignKey(Category, on_delete=models.CASCADE)
 author = models.ForeignKey(User, on_delete=models.CASCADE)
 keyword = models.ManyToManyField(Keyword)

 def getAuthor(self):
  author = User.objects.filter(id=self.author_id)[0]
  return author

 def getCapitalizedAuthor(self):
  author = User.objects.filter(id=self.author_id)[0]
  fn = author.first_name
  ln = author.last_name
  return fn.capitalize()+' '+ln.upper()

