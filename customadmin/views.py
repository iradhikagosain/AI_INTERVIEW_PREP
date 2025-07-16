

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta


def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')  
        else:
            messages.error(request, "Invalid credentials or not an admin.")
            return redirect('admin_login')
    return render(request, 'admin_login.html')


@login_required
def dashboard(request):
    today = timezone.now().date()
    last_30_days = today - timedelta(days=30)

    user_data = (
        User.objects.filter(date_joined__date__gte=last_30_days)
        .annotate(join_date=TruncDate('date_joined'))
        .values('join_date')
        .annotate(count=Count('id'))
        .order_by('join_date')
    )

    dates = [entry['join_date'].strftime('%Y-%m-%d') for entry in user_data]
    counts = [entry['count'] for entry in user_data]

    context = {
        'dates': dates,
        'counts': counts,
    }

    return render(request, 'customadmin/dashboard.html', context)



from django.contrib.auth.models import User

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'customadmin/user_list.html', {'users': users})