from django.db import models

# Create your models here.
<<<<<<< HEAD

from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ("aberta", "aberta"),
        ("EM_Andamento", "em andamento"),
        ("Concluida", "concluida"),
        ("Cancelada", "cancelada")
    ]
    
    PRIORIDADE_CHOICES = [
        ("Urgente", "Urgente"),
        ("Nao_urgente", "Nao_urgente")
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="aberta")
    prioridades = models.CharField(max_length=20, choices=PRIORIDADE_CHOICES, default="Nao_urgente")
    
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='tarefas'
    )
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()

    def __str__(self):
        return self.titulo
=======
>>>>>>> 1c2d85c1dee8a741f5dadd80736979a3e3d89f04
