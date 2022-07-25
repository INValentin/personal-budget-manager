


from django.urls import path

from budgets.views import BudgetCreateView, BudgetDeleteView, BudgetDetailView, BudgetListView, ExpenseCreateView, ExpenseDeleteView, ExpenseUpdateView


urlpatterns = [
    path('home/', BudgetListView.as_view(), name="home"),
    path('create/', BudgetCreateView.as_view(), name="budget_create"),
    path('<int:pk>/', BudgetDetailView.as_view(), name="budget_detail"),
    path('<int:pk>/delete/', BudgetDeleteView.as_view(), name="budget_delete"),
    path('<int:budget_id>/expenses/create/', ExpenseCreateView.as_view(), name="expense_create"),
    path('expenses/<int:pk>/update/', ExpenseUpdateView.as_view(), name="expense_update"),
    path('expenses/<int:pk>/delete/', ExpenseDeleteView.as_view(), name="expense_delete"),
]
