from django.shortcuts import JsonResponse
from .models import usuarios

def listar_usuarios(request):
    usuarios = usuarios.objects.all().values()
    return JsonResponse(list(usuarios), safe = False)

def buscar_usuarios_id(request, id):
    try:
        U = usuarios.objects.get(id=id)
        return JsonResponse({
            'id': U.id,
            'nome': U.nome,
            'email': U.email,
            'ativo': U.ativo,
            'data_criacao': U.data_criacao
        })
    except usuarios.DoesNotExist:
        return JsonResponse({'erro': 'Usuario não encontrado(a).'}, status=404)