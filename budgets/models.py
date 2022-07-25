from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Budget(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budget")
    budget_name = models.CharField(max_length=200, default="Budget for my event or plan!")
    description=models.TextField(verbose_name="Budget Description", blank=True, default="This will contain expenses for event or plan.")
    start_date = models.DateField(blank=False, help_text="Month/Day/Year")
    end_date = models.DateField(blank=False, help_text="Month/Day/Year")

class Expense(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="expenses")
    expense_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1, help_text="How much do you buy at once?")
    unit_price = models.PositiveIntegerField(blank=False)
    frequency = models.PositiveIntegerField(default=1, help_text="How many times will you buy this during your budget?")
    
    
        
    