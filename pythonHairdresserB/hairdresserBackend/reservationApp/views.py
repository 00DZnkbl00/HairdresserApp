from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Worker


# Create your views here.
def testJson(request):
    workers = Worker.objects.all()
    data = serializers.serialize('json', workers)
    return HttpResponse(data, content_type="application/json")


def lista_napisow(request):
    napisy = ["Test", "Napisów", "Bez", "Sensu"]
    return JsonResponse(napisy, safe=False)
