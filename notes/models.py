from django.db import models

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        name = self.name
        return name

class Fact(models.Model):
    descricao = models.TextField()
    curtidas = models.IntegerField(default=0)
    
    def __str__(self):
        descricao = self.descricao
        curtidas = self.curtidas
        return f'{descricao}. {curtidas}'

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        id = self.id
        title = self.title
        return f'{id}. {title}'