from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from budgets.models import Budget, Expense
from budgets.forms import BudgetForm, ExpenseForm

# Create your views here.


class BudgetCreateView(LoginRequiredMixin, FormView):
    template_name = "budgets/budget_create.html"
    form_class = BudgetForm
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        if form.is_valid():
            
            budget = form.save(commit=False)
            budget.owner = self.request.user
            budget.save()
        return super().form_valid(form)
        

class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = "budgets/list.html"
    
    
    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(owner=user)
    
class BudgetDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = Budget
    template_name = "budgets/detail.html"
    
    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(owner=user)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        budget = self.get_object()
        context["all_total"] = sum([e.unit_price*e.frequency*e.quantity for e in budget.expenses.all()])
        return context
    
    def test_func(self):
        return self.request.user == self.get_object().owner    

    

class BudgetDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Budget
    template_name = "budgets/budget_delete.html"
    success_url = reverse_lazy("home")
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        if (request.user != self.object.owner):
            return HttpResponseForbidden(content={"message": "Access Denied!"})
        
        return super().delete(request, *args, **kwargs)
    def test_func(self):
        return self.request.user == self.get_object().owner    

    
    
class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    queryset = Budget.objects.all()
    template_name = "budgets/expense_create.html" 
    form_class = ExpenseForm
    pk_url_kwarg = "budget_id"
    context_object_name = "budget"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["budget"] = self.get_object()
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            
            budget = self.get_object()
            expense = budget.expenses.create(**form.cleaned_data)
            print(expense.expense_name)
        return HttpResponseRedirect(reverse('budget_detail', args=(budget.id,)))
    

class ExpenseDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = "budgets/expense_delete.html"
    
    def get_success_url(self):
        self.success_url = reverse('budget_detail', args=(self.object.budget.id,))
        return super().get_success_url()
    
    def test_func(self):
        return self.request.user == self.get_object().budget.owner    

class ExpenseUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Expense
    template_name = "budgets/expense_update.html"
    fields = ["expense_name", "quantity", "unit_price", "frequency"]
    
    def get_success_url(self):
        self.success_url = reverse('budget_detail', args=(self.object.budget.id,))
        return super().get_success_url()

    
    def test_func(self):
        return self.request.user == self.get_object().budget.owner    

    
    

