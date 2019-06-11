from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core.files.base import ContentFile
from .models import Premises, Photo
from .forms import NameForm
from .choices import *

# Create your views here.
@login_required()
def index(request):
	types = []
	if request.user.user_permissions.filter(codename='can_view_premise1'):
		types.append('1')
	if request.user.user_permissions.filter(codename='can_view_premise2'):
		types.append('2')
	if request.user.user_permissions.filter(codename='can_view_premise3'):
		types.append('3')
	if request.user.user_permissions.filter(codename='can_view_premise4'):
		types.append('4')
	if request.user.user_permissions.filter(codename='can_view_premise_commercial'):
		types.append('5')
	premises=Premises.objects.filter(creater__in=request.user.groups.all(), types__in=types).order_by('-date')
	premisesCount=Premises.objects.all().count()
	lastDate=Premises.objects.values('date').latest('date')

	# Отрисовка HTML-шаблона index.html с данными внутри
	# переменной контекста context
	form = NameForm()
	return render(
		request,
		'index.html',
		context = {'premises':premises, 'form': form, 'typePremises': typePremises, 'premisesCount': premisesCount, 'lastDate': lastDate['date']}, # num_visits appended
	)

def addinfo(request):
	if request.method == 'POST' and request.FILES:
		form = NameForm(request.POST, request.FILES)
		print(form)
		form = NameForm(request.POST)
		# check whether it's valid:
		types = request.POST.get('types', '')
		address = request.POST.get('address', '')
		telephone = request.POST.get('telephone', '')
		description = request.POST.get('description', '')
		premises = Premises.objects.create(types=types, address = address, telephone = telephone, description = description, creater=request.user.groups.all()[0])
		premises.refresh_from_db()
		premises.save()
		for file in request.FILES.getlist('photo'):
			data = file.read() #Если файл целиком умещается в памяти
			photo = Photo(premises=premises)
			photo.image.save(file.name, ContentFile(data))
			photo.save()
		return redirect('index')
	else:
		return redirect('index')

def addnewuser(request):
	if request.method == 'POST':
		login = request.POST.get('username', '')
		email = request.POST.get('email', '')
		password = request.POST.get('password', '')
		user = User.objects.create_user(username=login, email=email, password=password, is_staff=True, is_active=True)
		group = Group.objects.get(name=request.user.groups.all()[0])
		user.groups.add(group)
		for permission in Permission.objects.filter(user=request.user):
			user.user_permissions.add(permission)
		user.save
		return HttpResponse('Новый пользователь ' + login + ' с e-mail ' + email + ' создан!')
	else:
		return HttpResponse('Не удалось создать нового пользователя. Возможно у Вас нет прав на создание.')

def changeinfo(request):
	data = request.POST.get('name', '')
	value = request.POST.get('value', '')
	id = request.POST.get('id', '')
	if data == 'types':
		newData = Premises.objects.filter(id=id).update(types=value)
	elif data == 'address':
		newData = Premises.objects.filter(id=id).update(address=value)
	elif data == 'telephone':
		newData = Premises.objects.filter(id=id).update(telephone=value)
	elif data == 'description':
		newData = Premises.objects.filter(id=id).update(description=value)
	elif data == 'date':
		newData = Premises.objects.filter(id=id).update(date=value)
	return HttpResponse(request)

def deleteimage(request):
	Photo.objects.filter(id=request.POST.get('idImage', '')).delete()
	return HttpResponse("Картинка удалена!")

def addimage(request):
	premise = Premises.objects.get(id=request.POST.get('idPremise', ''))
	for file in request.FILES.getlist('photo'):
			data = file.read() #Если файл целиком умещается в памяти
			photo = Photo(premises=premise)
			photo.image.save(file.name, ContentFile(data))
			photo.save()
	return HttpResponse("Картинка добавлена!")

def typepremises(request):
	print(request.user.user_permissions.get(codename='can_change_users'))
	context = {
		"1": '1-ка',
		"2": '2-ка',
		"3": '3-ка',
		"4": '4-ка',
		"5": 'Коммерческая недвижимость'
	}
	return JsonResponse(context, safe=False)