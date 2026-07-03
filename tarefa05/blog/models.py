from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="media/")
    texto = models.TextField(max_length=500)
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.titulo