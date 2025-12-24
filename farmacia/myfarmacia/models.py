from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed=models.BooleanField(default=False)

class TipoSangue(models.TextChoices):
    A_POSITIVO = "A+", "A positivo"
    A_NEGATIVO = "A-", "A negativo"
    B_POSITIVO = "B+", "B positivo"
    B_NEGATIVO = "B-", "B negativo"
    AB_POSITIVO = "AB+", "AB positivo"
    AB_NEGATIVO = "AB-", "AB negativo"
    O_POSITIVO = "O+", "O positivo"
    O_NEGATIVO = "O-", "O negativo"

class Dador(models.Model):
    nome = models.CharField(max_length=100)
    dataNascimento = models.DateField()
    nif = models.CharField(max_length=12)
    genero = models.CharField(max_length = 50)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    telefone = models.CharField(max_length=9)
    tipo = models.CharField(max_length=3, choices=TipoSangue.choices, default=TipoSangue.O_NEGATIVO)
    ativo = models.BooleanField(default=True)
    ultimaDoacao = models.DateField()
    
    def __str__(self):
        return f"{self.nome} - {self.dataNascimento} - {self.nif}- {self.genero} - {self.peso} - {self.telefone} - {self.tipo} - {self.ativo} - {self.ultimaDoacao}"

class Componente(models.TextChoices):
    SANGUE = "sangue", "Sangue"
    GLOBULOS_VERMELHOS = "globulos", "Globulos Vermelhos"
    PLASMA = "plasma", "plasma"

class PostoRecolha(models.Model):
    nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=100)
    codigoPostal = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.nome} - {self.morada} - {self.codigoPostal}"
    

class Doacao(models.Model):
    data = models.DateField()
    componente = models.CharField(max_length=20, choices=Componente.choices, default=Componente.SANGUE)
    valido = models.BooleanField(default=True)
    dador = models.ForeignKey(Dador, on_delete=models.DO_NOTHING, related_name='doacoes')
    posto = models.ForeignKey(PostoRecolha, on_delete=models.SET_NULL, null=True, related_name='doacoes')

    def __str__(self):
        return f"{self.data} - {self.componente} - {self.valido}- {self.dador} - {self.posto}"
