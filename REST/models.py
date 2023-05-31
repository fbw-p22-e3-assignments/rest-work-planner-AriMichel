
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)

class Shift(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.IntegerField(choices=[(0, '0-8'), (8, '8-16'), (16, '16-24')])
```