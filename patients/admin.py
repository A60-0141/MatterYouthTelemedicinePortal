from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Doctor, Patient, Appointment, GroupChat

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(GroupChat)


from .models import Progress

class ProgressAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date', 'health_score']
    search_fields = ['patient__user__username', 'health_score']

admin.site.register(Progress, ProgressAdmin)

