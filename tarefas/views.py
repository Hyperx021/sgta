from django.http import JsonResponse
from .models import tarefa

def listar_tarefas(request):
    tarefas = tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe = False)

def listar_tarefas_abertas(request):
    tarefas = tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas), safe=False)
