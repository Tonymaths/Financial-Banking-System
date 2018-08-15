from django.db.models import Sum
from django.shortcuts import render,redirect
from django.contrib import messages

from transactions.models import Diposit, Withdrawal, Interest
from .forms import ContactForm
from .models import Contact


def home(request):
    if not request.user.is_authenticated:
        return render(request, "core/home.html", {})
    else:
        user = request.user
        deposit = Diposit.objects.filter(user=user)
        deposit_sum = deposit.aggregate(Sum('amount'))['amount__sum']
        withdrawal = Withdrawal.objects.filter(user=user)
        withdrawal_sum = withdrawal.aggregate(Sum('amount'))['amount__sum']
        interest = Interest.objects.filter(user=user)
        interest_sum = interest.aggregate(Sum('amount'))['amount__sum']

        context = {
                    "user": user,
                    "deposit": deposit,
                    "deposit_sum": deposit_sum,
                    "withdrawal": withdrawal,
                    "withdrawal_sum": withdrawal_sum,
                    "interest": interest,
                    "interest_sum": interest_sum,
                  }

        return render(request, "core/transactions.html", context)


def about(request):
    return render(request, "core/about.html", {})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            messages.success(request, 'Thanks, ANTHONY will get in touch')
            return render(request, 'core/home.html', {'form': form})

        else:
            messages.error(request, 'Ensure all fields are entered correctly')

        return render(request, 'core/home.html', {'form': form})
