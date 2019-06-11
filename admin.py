from django.contrib import admin

from .models import Premises, Photo

class PremisesAdmin (admin.ModelAdmin):
	list_display = ('types', 'telephone', 'date')

admin.site.register(Premises, PremisesAdmin)

class PhotoAdmin (admin.ModelAdmin):
	list_display = ('premises', 'image')

admin.site.register(Photo, PhotoAdmin)