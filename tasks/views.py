from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from tasks.models import Task
from tasks.serializacao import Serializacao

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(["GET"])
def get_tasks(request):
    """
    Lista tudo.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializacao = Serializacao(tasks, many=True)
        return JsonResponse(serializacao.data, safe=False)

@api_view(["POST"])
def post_task(request):    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializacao = Serializacao(data=data)
        if serializacao.is_valid():
            serializacao.save()
            return JsonResponse(serializacao.data, status=201)
        return JsonResponse(serializacao.errors, status=400)

@api_view(["DELETE"])
def delete_tasks(request):    
    if request.method == 'DELETE':
        task = Task.objects.all().delete()
        return JsonResponse({"status": 200, "message": "Tasks deletadas"}, status=200)
