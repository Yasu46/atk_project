# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ATKResultForm  # ATKResultForm は forms.py で定義します
from .models import ATKResult

@login_required
def submit_atk_result(request):
    if request.method == 'POST':
        form = ATKResultForm(request.POST, request.FILES)
        if form.is_valid():
            atk_result = form.save(commit=False)
            atk_result.user = request.user
            atk_result.save()
            return redirect('success')  # 成功時にリダイレクトするページ
    else:
        form = ATKResultForm()

    return render(request, 'accounts/dashboard.html', {'form': form})

def success(request):
    return render(request,'atk_html/success.html')
