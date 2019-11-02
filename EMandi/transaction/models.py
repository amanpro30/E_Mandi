from django.db import models
from django.contrib.auth.models import User

class BankDetails(models.Model):
    BankHolder=models.OneToOneField(User,on_delete=models.CASCADE)
    BankName=models.CharField(max_length=50)
    BranchName=models.CharField(max_length=60)
    Ifsc=models.CharField(max_length=50)
    AccountNumber=models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'{self.BankHolder.username} BankDetails'

class Transaction(models.Model):
    Customer=models.ForeignKey(User,on_delete=models.CASCADE)
    TransDate=models.DateTimeField(auto_now=False,auto_now_add=True)
    Amount=models.PositiveIntegerField(default=None)
    TransType_choices = (
        ('Debited', 'Debited'),
        ('Credited', 'Credited'),
    )
    TransType = models.CharField(max_length=10, choices=TransType_choices,)
    def __str__(self):
        return f'{self.Customer.username} Transaction'
