from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

class CallDetailRecord(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    caller_number = models.CharField(max_length=20)
    callee_number = models.CharField(max_length=20)
    call_duration = models.IntegerField()
    call_date = models.DateTimeField()
