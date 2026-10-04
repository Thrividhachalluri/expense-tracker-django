from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm


def expense_list(request):

    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('expense_list')

    else:
        form = ExpenseForm()

    expenses = Expense.objects.all()
    total = sum(expense.amount for expense in expenses)

    return render(
        request,
        'expenseapp/expense_list.html',
        {
            'form': form,
            'expenses': expenses,
            'total': total
        }
    )


def expense_edit(request, id):

    expense = get_object_or_404(Expense, id=id)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)

        if form.is_valid():
            form.save()
            return redirect('expense_list')

    else:
        form = ExpenseForm(instance=expense)

    return render(
        request,
        'expenseapp/expense_edit.html',
        {
            'form': form,
            'expense': expense
        }
    )


def expense_delete(request, id):

    expense = get_object_or_404(Expense, id=id)

    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')

    return render(
        request,
        'expenseapp/expense_delete.html',
        {
            'expense': expense
        }
    )