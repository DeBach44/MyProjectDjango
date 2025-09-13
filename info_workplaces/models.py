from django.db import models
from info_employees.models import Employee

# Create your models here.
class Workplace(models.Model):
    '''Рабочие места'''
    number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Номер рабочего места'
        )
    employee = models.OneToOneField(Employee, 
        on_delete=models.SET_NULL, null=True,
        verbose_name='Сотрудник'
        )
    
    class Meta:
        verbose_name = 'Рабочее место'
        verbose_name_plural = 'Рабочие места'
    
    def __str__(self):
        return self.number