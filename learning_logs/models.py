from django.db import models

class Topic(models.Model):
    """ Um assunto no qual o usuário esta apredendo """
    text = models.CharField(max_length = 200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Devolve uma representação em string do modelo """
        return self.text

class Entry(models.Model):
    """ Algo específico aprendido sobre o assunto """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """ Devolve uma representação em string do modelo """
        return self.descricao[:50] + '...'