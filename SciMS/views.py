from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from articles.dao import dao


def getSerializedArticlesfromCategory(request, id_category):
	
	return dao.jsonArticlesfromCategory(id_category)


def index(request):
	if request.user.is_authenticated():
		return redirect(request, request.user)
	else:
		t= get_template('index.html')
		categories = dao.getAllCategories()
		articles = dao.getTenLastArticles()
		artsbycat = dao.getArticlesOfCategory(categories.first())
		html = t.render(Context({'categories':categories,'artsbycat':artsbycat ,'articles':articles}))
		return HttpResponse(html)

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html',c)


def redirect(request, user):
	authorGroup = Group.objects.get(name="Authors").user_set.all()
	if user in authorGroup:
		return HttpResponseRedirect('/articles/read')
	else:
		return HttpResponseRedirect('/admin/')

def authent(request):
	usrname= request.POST.get('login', '')
	passwd= request.POST.get('passwd', '')
	user= auth.authenticate( username= usrname, password= passwd)
	if user is not None:
		auth.login(request, user)
		return redirect(request, user)
	else:
		c = {}
		c.update(csrf(request))
		return render_to_response('login.html',c)

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
