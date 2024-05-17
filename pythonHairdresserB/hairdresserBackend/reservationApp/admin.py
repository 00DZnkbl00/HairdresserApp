from django.contrib import admin
from .models import Worker, Client, Service, Order, Session

# Register your models here.
admin.site.register(Worker)
admin.site.register(Client)
admin.site.register(Session)
admin.site.register(Service)
admin.site.register(Order)
