from django.contrib import admin

# Register your models here.
from .models import Join

class JoinAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','email', 'timestamp', 'updates', 'name', 'ip_address', 'ref_id']
	class Meta:
		model = Join

admin.site.register(Join, JoinAdmin)