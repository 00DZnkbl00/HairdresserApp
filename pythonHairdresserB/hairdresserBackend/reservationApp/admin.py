from django.contrib import admin
from .models import Worker, Client, Service, Order, Session

# Register your models here.
# admin.site.register(Worker)
# admin.site.register(Client)
# admin.site.register(Session)
admin.site.register(Service)
admin.site.register(Order)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    fields = ['name', 'surname']
    list_display = ['name', 'surname']
    search_fields = ['name', 'surname']


@admin.register(Client)
class WorkerAdmin(admin.ModelAdmin):
    fields = ['name', 'surname', 'phoneNumber', 'email']
    list_display = ['name', 'surname']
    search_fields = ['name', 'surname']


@admin.register(Session)
class WorkerAdmin(admin.ModelAdmin):
    fields = ['date', 'time', 'worker', 'order']
    list_display = ['date', 'time', 'worker']
    list_filter = ['date', 'time', 'worker']
