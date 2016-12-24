from django.core import serializers
from django.http import HttpResponse
from articles.models import Article, Category

def getTenLastArticles():
	return Article.objects.all().order_by('-pub_date')[:10]

def getAllCategories():
	return Category.objects.all()

def getArticlesOfCategory(id_category):
	return Article.objects.filter(category_id=id_category)

def jsonArticlesfromCategory(id_category):
	articles = Article.objects.filter(category_id=id_category)
	articles = serializers.serialize("json", articles)
	return HttpResponse(articles, content_type="application/json")


def getArticlesOfAuthor(id_auth):
	return Article.objects.filter(author_id=id_auth)
