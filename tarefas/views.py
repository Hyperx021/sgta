from django.http import JsonResponse
from .models import tarefa

def listar_tarefas(request):
    tarefas = tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe = False)

def listar_tarefas_abertas(request):
    tarefas = tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_por_prioridade(request, prioridade):
    tarefas = tarefa.objects.filter(prioridades=prioridade.upper()).values()
    
    lista_tarefas = list(tarefas)
    
    if lista_tarefas:
        return JsonResponse(lista_tarefas, safe=False)
    else:
        return JsonResponse({'mensagem': 'Nenhuma tarefa encontrada'}, status=404)


def buscar_tarefa_id(request, id):
    try:
        t = tarefa.objects.get(id=id)
        return JsonResponse({
            'id': t.id,
            'titulo': t.titulo,
            'descricao': t.descricao,
            'prioridades': t.prioridades,
            'status': t.status,
            'data_entrega': t.data_entrega
        })
    except tarefa.DoesNotExist:
        return JsonResponse({'erro': 'Tarefa não encontrada.'}, status=404)


def listar_urgentes_abertas(request):
    tarefas = tarefa.objects.filter(status='ABERTA', prioridades='URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)


def listar_atrasadas(request):
    hoje = timezone.now()
    tarefas = tarefa.objects.filter(data_entrega__lt=hoje).exclude(status='CONCLUIDA').values()
    return JsonResponse(list(tarefas), safe=False)

def buscar_por_titulo(request, palavra):
    tarefas = tarefa.objects.filter(titulo__icontains=palavra).values()
    return JsonResponse(list(tarefas), safe=False)