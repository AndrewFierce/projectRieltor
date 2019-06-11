from django.db import models
from datetime import date
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from .choices import *

class Photo(models.Model):
	image = models.ImageField(upload_to='premises/%Y/%m/%d', null=True, blank=True, height_field=None, width_field=None, max_length=100)
	premises = models.ForeignKey('Premises', on_delete=models.CASCADE, related_name='photos')

	def __str__(self):
		"""
		String for representing the Model object (in Admin site etc.)
		"""
		return self.premises.address

	class Meta:
		ordering = ["premises",]
		permissions = (
			("can_see_photos", "Возможность просматривать фотографии"),
			("can_change_photos", "Возможность редактировать фотографии"),
			("can_delete_photos", "Возможность удалять фотографии"),
			("can_create_photos", "Возможность создавать фотографии"),
		)

	def get_absolute_url(self):
		"""
		Returns the url to access a particular book instance.
		"""
		return reverse('image-detail', args=[str(self.id)])

@receiver(post_delete, sender=Photo)
def submission_delete(sender, instance, **kwargs):
	instance.image.delete(False)

class Premises(models.Model):
	creater = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
	types = models.CharField(max_length=1, choices=typePremises, blank=True, default='1', help_text='Выберите тип помещения')
	address = models.CharField(max_length=100, help_text="Введите адрес")
	telephone = models.CharField(max_length=100, unique = True, validators="", help_text="Введите телефон")
	description = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
	date = models.DateField(null=True, blank=True, auto_now_add = True)

	"""база пользователей"""
	def __str__(self):
		"""
		String for representing the Model object (in Admin site etc.)
		"""
		return self.address

	class Meta:
		ordering = ["types", "-date"]
		permissions = (
			("can_see_premises", "Возможность просматривать записи"),
			("can_change_premises", "Возможность редактировать записи"),
			("can_delete_premises", "Возможность удалять записи"),
			("can_create_premises", "Возможность создавать записи"),
			("can_change_users", "Возможность редактировать пользователя"),
			("can_delete_users", "Возможность удалять пользователя"),
			("can_create_users", "Возможность создавать пользователя"),
			("can_view_premise1", "Просмотр 1-ек"),
			("can_view_premise2", "Просмотр 2-ек"),
			("can_view_premise3", "Просмотр 3-ек"),
			("can_view_premise4", "Просмотр 4-ек"),
			("can_view_premise_commercial", "Просмотр коммерческой недвижимости"),
		)

	def get_absolute_url(self):
		"""
		Returns the url to access a particular book instance.
		"""
		return reverse('premises-detail', args=[str(self.id)])