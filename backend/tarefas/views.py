from django.http import JsonResponse
from .models import tarefa
from django.utils import timezone

def listar_tarefas(request):
    tarefas = tarefa.objects.all().values(
        'id', 
        'titulo', 
        'descricao', 
        'prioridades', 
        'status', 
        'data_entrega',
        'responsavel_'
    )
    
    lista = []
    for t in tarefas:
        t['responsavel'] = t.pop('responsavel_')
        lista.append(t)

    return JsonResponse(lista, safe=False)


def listar_tarefas_abertas(request):
    tarefas = tarefa.objects.filter(status='ABERTA').values(
        'id', 
        'titulo', 
        'descricao', 
        'prioridades', 
        'status', 
        'data_entrega',
        'responsavel_'
    )

    lista = []
    for t in tarefas:
        t['responsavel'] = t.pop('responsavel_')
        lista.append(t)

    return JsonResponse(lista, safe=False)


def listar_tarefas_por_prioridade(request, prioridade):
    tarefas = tarefa.objects.filter(prioridades=prioridade.upper()).values(
        'id', 
        'titulo', 
        'descricao', 
        'prioridades', 
        'status', 
        'data_entrega',
        'responsavel_'
    )
    
    lista_tarefas = []
    for t in tarefas:
        t['responsavel'] = t.pop('responsavel_')
        lista_tarefas.append(t)
    
    if lista_tarefas:
        return JsonResponse(lista_tarefas, safe=False)
    else:
        return JsonResponse({'mensagem': 'Nenhuma tarefa encontrada'}, status=404)


def buscar_tarefa_id(request, id):
    try:
        t = tarefa.objects.select_related('responsavel').get(id=id)
        return JsonResponse({
            'id': t.id,
            'titulo': t.titulo,
            'descricao': t.descricao,
            'prioridades': t.prioridades,
            'status': t.status,
            'data_entrega': t.data_entrega,
            'responsavel': t.responsavel.username if t.responsavel else None
        })
    except tarefa.DoesNotExist:
        return JsonResponse({'erro': 'Tarefa não encontrada.'}, status=404)


def listar_urgentes_abertas(request):
    tarefas = tarefa.objects.filter(status='ABERTA', prioridades='URGENTE').values(
        'id', 
        'titulo', 
        'descricao', 
        'prioridades', 
        'status', 
        'data_entrega',
        'responsavel_'
    )

    lista = []
    for t in tarefas:
        t['responsavel'] = t.pop('responsavel_')
        lista.append(t)

    return JsonResponse(lista, safe=False)


def listar_atrasadas(request):
    hoje = timezone.now()
    tarefas = tarefa.objects.filter(data_entrega__lt=hoje).exclude(status='CONCLUIDA').values(
        'id', 
        'titulo', 
        'descricao', 
        'prioridades', 
        'status', 
        'data_entrega',
        'responsavel_'
    )

    lista = []
    for t in tarefas:
        t['responsavel'] = t.pop('responsavel_')
        lista.append(t)

    return JsonResponse(lista, safe=False)


def buscar_por_titulo(request, palavra):
    tarefas = tarefa.objects.filter(titulo__icontains=palavra).values(
        'id', 
        'titulo', 
        'descricao', 
        'prioridades', 
        'status', 
        'data_entrega',
        'responsavel_'
    )

    lista = []
    for t in tarefas:
        t['responsavel'] = t.pop('responsavel_')
        lista.append(t)

    return JsonResponse(lista, safe=False)