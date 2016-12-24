from django.shortcuts import render, render_to_response
from django.http import HttpResponse , HttpResponseRedirect,HttpResponseNotFound
from django.template.loader import get_template
from django.template import Context
from articles.models import Category, Article
from django.contrib.auth.models import User
from articles import rxp
from django.template.context_processors import csrf

def readArticle(request, id_art):
	t= get_template('article_to_read.html')
	articles = Article.objects.filter(author_id=request.user.id)
	displayed = Article()
	if articles.exists():
		displayed = Article.objects.get(id=id_art)
	else:
		displayed.id = -5
	html = t.render({'articles':articles, 'displayed':displayed}, request)
	return HttpResponse(html)

def notfound(request):
	t= get_template('noarticle.html')
	html = t.render(request)
	return HttpResponse(html)

def read(request):
	art =Article.objects.filter(author_id=request.user.id).first()
	if art is not None:
		id_art = art.id
	else:
		id_art = -5
	return readArticle(request, id_art)


def getMLartcile(request, id_art):
	article = Article.objects.get(id=id_art)
	t= get_template('mlarticle.html')
	content = rxp.toHTML(article.content)
	html = t.render({'article': article,'date':article.pub_date.strftime("%d/%m/%Y"), 'content': content}, request)
	return HttpResponse(html)


def add(request):
	c = {}
	c.update(csrf(request))
	categories = Category.objects.all()
	html = Context({'categories':categories})
	return render_to_response('Add.html', c, html)

def deleteArticle(request, id_art):
	art = Article.objects.get(id=id_art)
	art.delete()
	return read(request)
	

def addArticle(request):
	article = Article()
	article.title = request.POST.get('title', '')
	article.abstract = request.POST.get('abstract', '')
	article.category_id = request.POST.get('categorie');
	article.content = request.POST.get('content', '')
	article.author = User.objects.get(id=request.user.id)
	try:
		article.save()
		return HttpResponseRedirect('/articles/read')
	except:
		return HttpResponseRedirect('/')


def edit(request, id_art):
	c = {}
	c.update(csrf(request))
	categories = Category.objects.all()
	article = Article.objects.get(id=id_art)
	html = Context({'categories':categories, 'article': article})
	return render_to_response('Edit.html', c, html)




def getKeywords(mykeys):
	mykeys = mykeys.replace(' ','')
	keyCollection = mykeys.split(';')
	keyCollection = keyCollection.remove('')
	keywords = Keyword.objects.all()
	keyArray
	for key in keyCollection:
		if not key in keywords:
			newkey = Keyword()
			newkey.word = key
			newkey.save() 
			keyArray.append(newkey)
		else:
			keyArray.append(Keyword.objects.get(word=key))
	return keyArray



def viewArticle(request, id_art):
	t= get_template('article_to_view.html')
	displayed = Article.objects.get(id=id_art)
	html = t.render({'displayed':displayed}, request)
	return HttpResponse(html)












