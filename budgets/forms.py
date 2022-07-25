from django.forms import ModelForm
from budgets.models import Budget, Expense


class BudgetForm(ModelForm):
    
    class Meta:
        model = Budget
        exclude = ["owner"]
        
        
class ExpenseForm(ModelForm):
    
    class Meta:
        model = Expense
        exclude = ["budget"]