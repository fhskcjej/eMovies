from purchases.models import Purchase
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required


@login_required
def purchase_complete(request):
    purchases = Purchase.objects.filter(user=request.user).order_by('-purchased_at')[:5]
    return render(request, 'purchases/purchase_complete.html', {'purchases': purchases})


@login_required
def purchase_history_view(request):
    purchases = Purchase.objects.filter(user=request.user).order_by('-purchased_at')
    return render(request, 'purchases/purchase_history.html', {'purchases': purchases})






