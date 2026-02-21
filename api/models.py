from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)
    is_custom = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('INCOME', 'Income'), 
        ('EXPENSE', 'Expense'),
    ]

    # 
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES, default='EXPENSE'
    )
    
    date = models.DateField(auto_now_add=True)
