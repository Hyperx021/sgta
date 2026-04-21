from django.db import models


class tarefa(models.Model):
    Status_Choices = [
        ("aberta", "aberta"),
        ("EM_Andamento", "em andamento"),
        ("Concluida","concluida"),
        ("Cancelada", "cancelada")
    ]
    
    prioridadee_choices = [
        ("Urgente","Urgente"),
        ("Nao_urgente","Nao_urgente")
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices= Status_Choices, default= "ABERTA")
    prioridades = models.CharField(max_length=20, choices= prioridadee_choices, default= "Nao_urgente")
    data_criacao = models.DateTimeField (auto_now_add=True)
    data_entrega = models.DateField()

    def __str__(Self):
        return Self.titulo