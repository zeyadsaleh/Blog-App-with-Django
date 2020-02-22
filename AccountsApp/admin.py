from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExtendedUser


class ExtendedUserAdmin(UserAdmin):
	#lists to be displayed 
	list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
	#fields to search with
	search_fields = ('email', 'username',)	
	# non-editable fields
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(ExtendedUser, ExtendedUserAdmin)