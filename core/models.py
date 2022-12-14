from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

class Evento(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.TextField(blank=True, null=True)
  data_evento = models.DateTimeField(verbose_name="Data do Evento")
  data_criacao = models.DateTimeField(auto_now=True)
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  local_evento = models.CharField(max_length=60)
  
  class Meta:
    db_table = 'evento' # define table name

  def __str__(self) -> str:
    return self.titulo

  def get_data_evento(self):
    return self.data_evento.strftime('%d/%m/%Y %H:%MHrs')

  def get_data_input_evento(self):
    return self.data_evento.strftime('%Y-%m-%dT%H:%M')

  def get_evento_atrasado(self):
    if self.data_evento < datetime.now():
      return True
    else:
      return False

  def get_evento_proximo(self):
    if (datetime.now() + timedelta(hours=1)) >= self.data_evento >= datetime.now():
      return True
    else:
      return False
